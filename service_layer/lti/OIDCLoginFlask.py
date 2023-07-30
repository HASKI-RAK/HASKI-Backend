import json
import os
import time
import urllib.parse

from flask import redirect
from flask.wrappers import Request
from werkzeug.wrappers.response import Response

import service_layer.crypto.JWTKeyManagement as JWTKeyManagement
import service_layer.service.SessionServiceFlask as SessionServiceFlask
from errors import errors as err
from service_layer import services, unit_of_work
from service_layer.crypto.cryptorandom import CryptoRandom
from service_layer.lti.config.ToolConfigJson import ToolConfigJson
from service_layer.lti.Messages import LTIIDToken
from service_layer.lti.OIDCLogin import OIDCLogin
from service_layer.lti.Roles import RoleMapper
from service_layer.service.CookieServiceFlask import CookieServiceFlask


class OIDCLoginFlask(OIDCLogin):
    """Flask implementation of OIDC login"""

    LEARNING_LOOKUP_URL = "https://purl.imsglobal.org/spec/lti/claim/"
    UNIVERSITY_LOOKUP_URL = f"{LEARNING_LOOKUP_URL}tool_platform"
    ROLE_LOOKUP_URL = f"{LEARNING_LOOKUP_URL}roles"
    MOODLE_URL = "https://moodle.haski.app"
    BACKEND_URL = "https://backend.haski.app"

    COOKIE_EXPIRATION = 43200

    def __init__(
        self, request: Request, tool_config: ToolConfigJson, cookie_service=None
    ):
        self._request = request
        self._cookie_service = (
            cookie_service if cookie_service else CookieServiceFlask(request)
        )
        self.oidc_login_params = {
            "iss",
            "client_id",
            "login_hint",
            "lti_message_hint",
            "target_link_uri",
            "lti_deployment_id",
        }
        super(OIDCLoginFlask, self).__init__(request, tool_config)

    def check_params(self) -> "OIDCLoginFlask":
        """Validate given parameters"""
        try:
            self._check_required_params()
            self._load_oidc_login_params()
            self._verify_platform()
            self._verify_target_link_uri()
        except Exception as e:
            self._raise_err_400("Error in checking parameters", e=e)

        return self

    def _check_required_params(self) -> None:
        """Check if all required parameters are present"""
        if not self.oidc_login_params.issubset(self._request.form.keys()):
            raise err.MissingParameterError(status_code=400)

    def _load_oidc_login_params(self) -> None:
        """Store subset with values from request form in object"""
        self._oidc_login_params_dict = {
            key: self._request.form.get(key) for key in self.oidc_login_params
        }

    def _verify_platform(self) -> None:
        """Get the platform settings (same scheme as in the tool config json).
        HTTP_ORIGIN is a safe way to get the origin of the request and
         a way to avoid CSRF attacks.
        When redirected from http it doesn't work anymore
        """
        try:
            self._platform = self._tool_config.decode_platform(
                self._tool_config.get_platform(self._get_frontend_url())
            )
            if not self._platform:
                self._raise_err_400("No platform found")
        except Exception as e:
            self._raise_err_400("Error in check_auth", e=e)

    def _verify_target_link_uri(self) -> None:
        """Verify if the target_link_uri is valid and uses https in production
        and does not redirect to other domain than our tool"""
        try:
            parsed_target_link_url = (
                urllib.parse.urlparse(
                    self._oidc_login_params_dict.get("target_link_uri")
                )
                or None
            )

            if os.environ.get("FLASK_ENV") == "production":
                if parsed_target_link_url.scheme != "https":
                    self._raise_err_400("target_link_uri is not HTTPS")

            if (
                parsed_target_link_url.netloc
                != urllib.parse.urlparse(self._request.host_url).netloc
            ):
                self._raise_err_400("target_link_uri is not from the same host")

            if (
                self._oidc_login_params_dict.get("target_link_uri")
                != self._platform.target_link_uri
            ):
                self._raise_err_400("target_link_uri may be malicious")

        except ValueError as e:
            self._raise_err_400("target_link_uri is invalid", e=e)

    def auth_redirect(self) -> Response:
        """Login to OIDC provider from LMS.
        Crafts the redirect URL by adding the necessary parameters
        """
        # Generate a unique nonce
        nonce = self._generate_nonce()
        # Generate the state JWT
        state_jwt = self._build_set_state_jwt(nonce)
        # Generate the URL parameters
        redirect_url = self._generate_redirect_url(state_jwt, nonce)
        # Generate response
        response = redirect(redirect_url)
        return response

    @staticmethod
    def _generate_nonce() -> str:
        """Generates a unique nonce."""
        return CryptoRandom().getrandomstring(32)

    def _build_set_state_jwt(self, nonce: str) -> str:
        """Generates the JWT for the state."""
        return SessionServiceFlask.set_state_jwt(
            nonce,
            self._platform.auth_login_url,
            self._tool_config.get_tool_url(
                self._request.environ.get("HTTP_ORIGIN", "")
            ),
        )

    def _generate_redirect_url(self, state_jwt: str, nonce: str) -> str:
        """Generates the redirect URL with the necessary parameters."""
        platform = self._tool_config.get_platform(self._get_frontend_url())
        ru = self.make_url_accept_param(platform["auth_login_url"])
        params = self._build_redirect_params(nonce, state_jwt, platform)
        return "".join([ru, urllib.parse.urlencode(params)])

    def _build_redirect_params(self, nonce: str, state_jwt: str, platform):
        return {
            "client_id": platform["client_id"],
            "response_mode": "form_post",
            "redirect_uri": self._oidc_login_params_dict.get("target_link_uri"),
            "response_type": "id_token",
            "scope": "openid",
            "nonce": nonce,
            "state": state_jwt,
            "login_hint": self._oidc_login_params_dict.get("login_hint"),
            # resource link id or deep link idc
            "lti_message_hint": self._oidc_login_params_dict.get("lti_message_hint"),
        }

    def verify_state(self) -> "OIDCLoginFlask":
        """Verify the state parameter
        If the state parameter is not valid, the request
         is rejected with a 403 Forbidden response.
        """
        # 🔑 check auth

        # verify state parameter signature
        try:
            state_form_jwt = self._request.form.get("state", type=str) or ""
            state_form = JWTKeyManagement.verify_jwt(state_form_jwt)
            self._verify_state_params(state_form)
        except Exception as e:
            self._raise_err_403("No state found", e=e)

        return self

    def _verify_state_params(self, state_form):
        """Check whether state signature or payload are invalid.
        If the state parameter is not valid, the request
         is rejected with a 403 Forbidden response.
        """
        if not state_form:
            self._raise_err_403("Invalid state signature")
        if not JWTKeyManagement.verify_state_jwt_payload(state_form):
            self._raise_err_403("Invalid state payload")

    def verify_id_token(self) -> "OIDCLoginFlask":
        """Verify the id_token
        If the id_token is not valid, the request
         is rejected with a 403 Forbidden response.
        """
        self._check_request_error()
        self._decode_id_token()
        self._verify_id_token_signature()
        self._validate_id_token()
        self._save_id_token_in_session()

        return self

    def _check_request_error(self) -> None:
        """Check if there is an error in the request."""
        if self._request.form.get("error"):
            self._raise_err_400(self._request.form.get("error") or "Unknown error")
        if not self._request.form.get("id_token"):
            self._raise_err_400("No id_token found")

    def _decode_id_token(self) -> None:
        """Decode the id_token."""
        id_token_jwt = self._request.form.get("id_token", type=str) or ""
        if not id_token_jwt:
            self._raise_err_400(
                "Invalid id_token, crypto key\
                 signature or lti config data of LMS may have changed"
            )

        id_token_header_unverified = JWTKeyManagement.get_unverified_header(
            id_token_jwt
        )
        id_token_unverified = JWTKeyManagement.load_jwt(id_token_jwt)

        platform = self._tool_config.get_platform(id_token_unverified["iss"])
        hmac_key: str = next(
            (
                key
                for key in platform["key_set"]["keys"]
                if key["kid"] == id_token_header_unverified["kid"]
            ),
            "",
        )
        if not hmac_key:
            self._raise_err_400("Invalid decryption key")

        self.id_token = JWTKeyManagement.verify_jwt(
            id_token_jwt, JWTKeyManagement.construct_key(hmac_key)
        )

    def _verify_id_token_signature(self) -> None:
        """Verify the id_token signature."""
        if not self.id_token:
            self._raise_err_403("Invalid id_token signature")

    def _validate_id_token(self) -> None:
        """Validate the id_token."""
        try:
            self.id_token = LTIIDToken(**self.id_token)
        except Exception as e:
            self._raise_err_403("Invalid id_token", e=e)

    def _save_id_token_in_session(self) -> None:
        """Save the id_token in the session."""
        SessionServiceFlask.set(self.id_token.nonce, "id_token", self.id_token)

    def lti_launch_from_id_token(self) -> Response:
        """Launch LTI from id_token. Redirects to Frontend with nonce jwt in URL."""
        state_form_jwt = self._request.form.get("state", type=str) or ""
        self._verify_state_payload(state_form_jwt)
        nonce_jwt = self._generate_nonce_jwt()
        response = self._redirect_to_frontend(nonce_jwt)
        self._create_and_store_user_wrapper()

        return response

    def _verify_state_payload(self, state_jwt: str) -> None:
        """Verify the state payload."""
        state_form = JWTKeyManagement.verify_jwt(state_jwt)
        if not JWTKeyManagement.verify_state_jwt_payload(state_form):
            self._raise_err_403("Invalid state payload")

    def _generate_nonce_jwt(self) -> str:
        """Generate nonce and obtain cookie in the next request."""
        nonce_jwt = JWTKeyManagement.generate_nonce_jwt(
            self.id_token.nonce, self._request.referrer, self._get_backend_url()
        )
        SessionServiceFlask.set(self.id_token.nonce, "nonce_jwt", nonce_jwt)
        return nonce_jwt

    def _get_backend_url(self):
        return os.environ.get("BACKEND_URL", self.BACKEND_URL)

    def _get_frontend_url(self):
        return os.environ.get("LMS_URL", self.MOODLE_URL)

    def _redirect_to_frontend(self, nonce_jwt: str) -> Response:
        """Redirect to the frontend login URL."""
        platform = self._get_platform_from_origin()
        self._platform = platform
        response = "".join(
            [
                self._platform.frontend_login_url,
                "?",
                urllib.parse.urlencode({"nonce": nonce_jwt}),
            ]
        )
        response = redirect(response)
        return response

    def _create_and_store_user_wrapper(self) -> None:
        try:
            self._create_and_store_user()
        except Exception as e:
            self._raise_err_400("User could not be created", e=e)

    def _create_and_store_user(self) -> None:
        """Create and store the user if it doesn't exist."""
        user = services.get_user_by_lms_id(
            unit_of_work.SqlAlchemyUnitOfWork(), self.id_token.sub
        )
        if not user:
            user = self._create_user()
        if user["role"] == "student":
            user = services.get_student_by_user_id(
                unit_of_work.SqlAlchemyUnitOfWork(), user["id"]
            )
        SessionServiceFlask.set(self.id_token.nonce, "user", user)

    def _create_user(self):
        return services.create_user(
            unit_of_work.SqlAlchemyUnitOfWork(),
            name=self.id_token.name,
            university=self.id_token[self.UNIVERSITY_LOOKUP_URL]["name"],
            lms_user_id=self.id_token.sub,
            role=RoleMapper(self.id_token[self.ROLE_LOOKUP_URL]).get_role(),
        )

    def _get_platform_from_origin(self):
        """Get the platform from the origin."""
        try:
            platform = self._tool_config.decode_platform(
                self._tool_config.get_platform(
                    self._request.environ.get("HTTP_ORIGIN", "")
                )
            )
            if not platform:
                self._raise_err_400("No platform found")
            return platform
        except Exception as e:
            self._raise_err_400("Error in check_auth", e=e)

    def get_cookie_expiration(self) -> Response:
        # Verify nonce jwt in request
        json_data = self._request.get_json() or {}
        nonce_payload = self._verify_nonce(json_data)
        # Get user based on id_token
        token, user = self._get_token_and_user(nonce_payload)
        # Generate state JWT and create the response
        response = self._generate_response(token, user, nonce_payload)

        return response

    def _verify_nonce(self, json_data: dict[str, any]) -> str:
        """Verify the nonce in the JSON data and return the nonce_jwt."""
        if not json_data.get("nonce"):
            self._raise_err_403("No nonce found")
        nonce_jwt = json_data["nonce"] or ""
        nonce_payload = JWTKeyManagement.verify_jwt(nonce_jwt)
        if not nonce_payload:
            self._raise_err_403("Invalid nonce signature")
        if not JWTKeyManagement.verify_jwt_payload(nonce_payload):
            self._raise_err_403("Invalid nonce payload")

        return nonce_payload

    def _get_token_and_user(self, nonce_payload):
        """Get the token and user based on the nonce_jwt."""
        token = SessionServiceFlask.get(nonce_payload["nonce"], "id_token")
        if not token:
            self._raise_err_403("Invalid nonce")

        user = SessionServiceFlask.get(nonce_payload["nonce"], "user")
        if not user:
            self._raise_err_403("Invalid state")

        return token, user

    def _generate_response(self, token, user, nonce_payload) -> Response:
        """Generate the state JWT and create the response."""
        cookie_exp = self.COOKIE_EXPIRATION
        state_jwt = self._generate_state_jwt_for_response(
            token, cookie_exp, user, nonce_payload
        )
        # Response object to attach a cookie
        response = self._generate_response_object(cookie_exp)
        # Set 🔑 auth 🍪 cookie
        domain = urllib.parse.urlparse(self._request.referrer).hostname
        secure = self._request.referrer.startswith("https")
        self._set_cookie(response, domain, val=state_jwt, sec=secure, exp=cookie_exp)

        return response

    @staticmethod
    def _generate_response_object(cookie_exp, status=200):
        """Generate a Response object to attach a cookie with status 200"""
        return Response(
            response=json.dumps(
                {
                    # UNIX time
                    "expiration": int(time.time())
                    + cookie_exp * 60,
                }
            ),
            status=status,
            mimetype="application/json",
        )

    def _generate_state_jwt_for_response(self, token, cookie_exp, user, payload):
        role_mapper = RoleMapper(token[self.ROLE_LOOKUP_URL])
        role = role_mapper.get_role().lower()
        permissions = role_mapper.get_permissions()
        return JWTKeyManagement.generate_state_jwt(
            nonce=CryptoRandom.createuniqueid(32),
            state=CryptoRandom.createuniqueid(32),
            audience=self._request.referrer,
            issuer=self._get_backend_url(),
            expiration=cookie_exp,
            additional_claims={
                "id": user.get("id"),
                "user_id": user.get("user_id"),
                "lms_user_id": user["lms_user_id"],
                "university": user["university"],
                "role": role,
                "role_id": user["role_id"],
                "session_nonce": payload["nonce"],
                "permissions": [permission.value for permission in permissions],
            },
        )

    def get_logout(self) -> Response:
        # Create the logout response with a 204 status code
        response = Response(status=204)
        # Extract the domain from the referrer URL
        domain = urllib.parse.urlparse(self._request.referrer).hostname
        # Set the haski_state cookie to an empty value with max_age=0 to expire it
        self._set_cookie(response, domain)

        return response

    def _set_cookie(
        self,
        response: Response,
        domain,
        val="",
        sec=False,
        exp=0,
    ) -> None:
        """Set the haski_state cookie.
        Defaults to logout cookie (empty value with max_age=0 to expire it)"""
        self._cookie_service.set_cookie(
            response=response,
            key="haski_state",
            value=val,
            secure=sec,
            httponly=True,
            samesite="Lax",
            max_age=exp,
            domain=domain,
        )

    def _raise_err_400(self, msg: str, e=None):
        raise err.ErrorException(e, message=msg, status_code=400)

    def _raise_err_403(self, msg: str, e=None):
        raise err.ErrorException(e, message=msg, status_code=403)
