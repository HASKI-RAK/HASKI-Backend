import datetime
import os
import unittest
from unittest import mock
from unittest.mock import MagicMock, patch

import service_layer.lti.config.ToolConfigJson as ToolConfigJson
from errors import errors as err
from service_layer.crypto import JWTKeyManagement
from service_layer.lti.OIDCLoginFlask import OIDCLoginFlask
from utils.auth.permissions import Permissions

# ignore E501
config_file = {
    "https://moodle.haski.app": {
        "default": True,
        "client_id": "VRCKkhKlZtHNHtD",
        "tool_url": "https://backend.ke.haski.app",
        "frontend_login_url": "https://ke.haski.app/login",
        "target_link_uri": "https://backend.ke.haski.app/lti_launch",
        "auth_login_url": "https://moodle.haski.app/mod/lti/auth.php",
        "auth_token_url": "https://moodle.haski.app/mod/lti/token.php",
        "key_set_url": "https://moodle.haski.app/mod/lti/certs.php",
        "haski_lti_activity": "https://moodle.haski.app/mod/lti/view.php?id=138",
        "platform_name": "HASKI",
        "key_set": {
            "keys": [
                {
                    "kty": "RSA",
                    "alg": "RS256",
                    "kid": "5e58bef6fa8030be050b",
                    "e": "AQAB",
                    # pylint: disable=line-too-long
                    "n": "z8uwIpHep-dGbqqutVqQPsXdwJk8ESoXPw1UD-9PmlTm06Q6PmXl5jHT9J6hTuW-9OjiycuBs07DW1At6LEAEBOJbFw2H6aflmPyhq09Cwernuk6OzekRRmnPdmfYeOcjpHAGaZ3qwaU0E6zPt_Ki1ZqdtLnB53ytO1fuYTmK1FVSbnexK9i4OkLk6OHMCHkInQTndRMWOiKWwrAoc591LlNSzgvlW_S9s-Vj2N4sHAcikKobzMMD8ixsV84Lx3mZyb13qph9qXUMJB9It-5WXa-FfsbUQZ6MeC0ks9_XSyl7tI7Q2eHUqenPimZL15uQnWek-gaE61IAK7ihKSMew",  # noqa: E501
                    "use": "sig",
                }
            ]
        },
        "private_key_file": "private.key",
        "public_key_file": "public.key",
        "deployment_ids": ["1"],
    }
}

host = config_file["https://moodle.haski.app"]["tool_url"].split("//")[1]


form = {
    "iss": "https://moodle.haski.app",
    "client_id": "VRCKkhKlZtHNHtD",
    "login_hint": "student",
    "lti_message_hint": "message_hint",
    "target_link_uri": "https://backend.ke.haski.app/lti_launch",
    "lti_deployment_id": "1",
}


# Test cases for OIDCLoginFlask
class TestOIDCLoginFlask(unittest.TestCase):
    @patch.multiple(os.path, isfile=MagicMock(return_value=True))
    def setUp(self):
        self.request = MagicMock()
        self.oidc_login = OIDCLoginFlask(self.request)
        ToolConfigJson._iss_conf_dict = config_file

    def test_tool_config_decode_platform(self):
        platform = ToolConfigJson.decode_platform(
            ToolConfigJson.get_platform("https://moodle.haski.app")
        )
        self.assertEqual(
            platform.platform_name,
            "HASKI",
        )

    def test_no_platform(self):
        """check_params but decode_platform returns None"""
        with patch.object(self.oidc_login, "_request", _request=MagicMock) as mock_form:
            mock_form.form = form.copy()
            mock_form.host = host
            with patch.object(
                ToolConfigJson,
                "decode_platform",
                return_value=None,
            ):
                with self.assertRaisesRegex(
                    err.ErrorException,
                    "No platform found",
                ):
                    self.oidc_login.check_params()

    def test_check_params_successful(self):
        # expect not to raise an exception
        with patch.object(self.oidc_login, "_request", _request=MagicMock) as mock_form:
            mock_form.form = form.copy()
            mock_form.host = host
            self.assertTrue(self.oidc_login.check_params())

    def test_check_params_missing_iss(self):
        # object clone without iss:
        with patch.object(self.oidc_login, "_request", _request=MagicMock) as mock_form:
            mock_form.form = form.copy()
            mock_form.form.pop("iss", None)
            with self.assertRaisesRegex(
                err.ErrorException, "Missing parameters in request"
            ):
                self.oidc_login.check_params()

    def test_check_params_missing_platform(self):
        with patch.object(
            ToolConfigJson,
            "get_platform",
            return_value=None,
        ):
            with patch.object(self.oidc_login, "_request", _request=MagicMock):
                with self.assertRaisesRegex(
                    err.ErrorException, "Missing parameters in request"
                ):
                    self.oidc_login.check_params()

    def test_check_params_wrong_target_link_uri(self):
        with patch.object(self.oidc_login, "_request", _request=MagicMock) as mock_form:
            mock_form.form = form.copy()
            mock_form.form["target_link_uri"] = "wrong_uri"
            with self.assertRaisesRegex(
                err.ErrorException, "target_link_uri is not from the same host"
            ):
                self.oidc_login.check_params()

    def test_prod_no_https(self):
        """targetlink has no https and environ is production"""

        with patch.object(self.oidc_login, "_request", _request=MagicMock) as mock_form:
            mock_form.form = form.copy()
            mock_form.host = host
            mock_form.form["target_link_uri"] = "http://backend.haski.app/lti_launch"
            with patch.dict(
                os.environ,
                {"FLASK_ENV": "production"},
            ):
                with self.assertRaisesRegex(
                    err.ErrorException, "target_link_uri is not HTTPS"
                ):
                    self.oidc_login.check_params()

    def test_verify_state_successful(self):
        with patch.object(self.oidc_login, "_request", _request=MagicMock) as mock_form:
            mock_form.form = form.copy()
            mock_form.host = host
            mock_form.form["state"] = "valid_state_jwt"

            with patch(
                "service_layer.crypto.JWTKeyManagement.verify_jwt"
            ) as mock_verify_jwt:
                mock_verify_jwt.return_value = {"nonce": "valid_nonce"}

                with patch(
                    "service_layer.crypto.JWTKeyManagement.verify_state_jwt_payload"
                ) as mock_verify_state_jwt_payload:
                    mock_verify_state_jwt_payload.return_value = True

                    self.oidc_login.verify_state()

                    mock_verify_jwt.assert_called_once_with("valid_state_jwt")
                    mock_verify_state_jwt_payload.assert_called_once_with(
                        {"nonce": "valid_nonce"}
                    )

    def test_verify_state_invalid_jwt(self):
        with patch.object(self.oidc_login, "_request", _request=MagicMock) as mock_form:
            mock_form.form = form.copy()
            mock_form.host = host
            mock_form.form["state"] = "invalid_state_jwt"

            with patch(
                "service_layer.crypto.JWTKeyManagement.verify_jwt"
            ) as mock_verify_jwt:
                mock_verify_jwt.side_effect = err.InvalidJWTError()

                with self.assertRaisesRegex(
                    err.InvalidJWTError, "Invalid state signature"
                ):
                    self.oidc_login.verify_state()

                    mock_verify_jwt.assert_called_once_with("invalid_state_jwt")

    def test_verify_state_invalid_payload(self):
        with patch.object(self.oidc_login, "_request", _request=MagicMock) as mock_form:
            mock_form.form = form.copy()
            mock_form.host = host
            mock_form.form["state"] = "invalid_state_jwt"

            with patch(
                "service_layer.crypto.JWTKeyManagement.verify_jwt"
            ) as mock_verify_jwt:
                mock_verify_jwt.return_value = {"nonce": "invalid_nonce"}

                with patch.object(
                    JWTKeyManagement,
                    "verify_state_jwt_payload",
                ) as mock_verify_state_jwt_payload:
                    mock_verify_state_jwt_payload.side_effect = err.InvalidJWTError()

                    with self.assertRaises(err.InvalidJWTError):
                        self.oidc_login.verify_state()

                        mock_verify_jwt.assert_called_once_with("invalid_state_jwt")
                        mock_verify_state_jwt_payload.assert_called_once_with(
                            {"nonce": "invalid_nonce"}
                        )

    def test_verify_id_token_error_in_form(self):
        with patch.object(self.oidc_login, "_request", _request=MagicMock) as mock_form:
            mock_form.form = form.copy()
            mock_form.host = host
            mock_form.form["error"] = "error"

            with self.assertRaisesRegex(err.ErrorException, "error"):
                self.oidc_login.verify_id_token()

    def test_verify_id_token_unverified_header_fail(self):
        with patch.object(self.oidc_login, "_request", _request=MagicMock) as mock_form:
            mock_form.form = form.copy()
            mock_form.host = host
            mock_form.form["id_token"] = "valid_id_token_jwt"

            with patch(
                "service_layer.crypto.JWTKeyManagement.verify_jwt"
            ) as mock_verify_jwt:
                mock_verify_jwt.return_value = {"sub": "valid_sub"}

                with self.assertRaisesRegex(
                    err.InvalidJWTError, "Error loading header"
                ):
                    self.oidc_login.verify_id_token()

                    mock_verify_jwt.assert_called_once_with("valid_id_token_jwt")

    def test_verify_id_token_successful(self):
        with patch.object(self.oidc_login, "_request", _request=MagicMock) as mock_form:
            mock_form.form = form.copy()
            mock_form.host = host
            mock_form.form["id_token"] = "valid_id_token_jwt"

            with patch.object(
                JWTKeyManagement,
                "get_unverified_header",
                return_value={
                    "kid": config_file["https://moodle.haski.app"]["key_set"]["keys"][
                        0
                    ]["kid"],
                },
            ):
                with patch(
                    "service_layer.crypto.JWTKeyManagement.load_jwt",
                ) as mock_load_jwt:
                    mock_load_jwt.return_value = {
                        "sub": "valid_sub",
                        "iss": "https://moodle.haski.app",
                    }
                    with patch.object(
                        ToolConfigJson,
                        "get_platform",
                        return_value=config_file["https://moodle.haski.app"],
                    ):
                        with patch(
                            "service_layer.crypto.JWTKeyManagement.verify_jwt"
                        ) as mock_verify_jwt:
                            mock_verify_jwt.return_value = {
                                "sub": "valid_sub",
                                "iss": "https://moodle.haski.app",
                            }

                            self.oidc_login.verify_id_token()

                            mock_verify_jwt.assert_called_with(
                                "valid_id_token_jwt", mock.ANY
                            )

    def test_lti_launch_from_id_token_user_does_not_exist_in_db(self):
        # Create a mock request with the necessary attributes
        request_mock = MagicMock()
        request_mock.form = MagicMock()
        request_mock.form.get = MagicMock(
            side_effect=lambda k, type=str: {
                "state": "valid_state_jwt",
                "iss": "https://moodle.haski.app",
                "client_id": "VRCKkhKlZtHNHtD",
                "login_hint": "student",
                "lti_message_hint": "message_hint",
                "target_link_uri": "https://backend.ke.haski.app/lti_launch",
                "id_token": "valid_id_token_jwt",
            }.get(k, "")
        )
        request_mock.referrer = "https://example.com"
        self.oidc_login._request = request_mock

        jwt_payload = {
            "nonce": "valid_nonce",
            "iat": (
                datetime.datetime.utcnow() - datetime.timedelta(minutes=5)
            ).timestamp(),
            "exp": (
                datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
            ).timestamp(),
            "iss": os.environ.get("BACKEND_URL", "https://backend.haski.app"),
            "kid": "backendprivatekey",
            "state": "valid_state",
            "sub": "user123",
            "name": "Test User",
            "https://purl.imsglobal.org/spec/lti/claim/tool_platform": {
                "name": "Test University"
            },
            "https://purl.imsglobal.org/spec/lti/claim/roles": ["student"],
        }

        with patch(
            "service_layer.crypto.JWTKeyManagement.verify_jwt", return_value=jwt_payload
        ):
            with patch(
                "service_layer.crypto.JWTKeyManagement.generate_nonce_jwt",
                return_value="mocked_nonce_jwt",
            ):
                with patch("service_layer.service.SessionServiceFlask.set"):
                    with patch(
                        "service_layer.service.SessionServiceFlask.get"
                    ) as mock_get_session:
                        mock_get_session.side_effect = (
                            lambda nonce, key: "valid_state"
                            if key == "state" and nonce == "valid_nonce"
                            else None
                        )
                        with patch(
                            "service_layer.services.get_user_by_lms_id",
                            return_value={},
                        ):
                            with patch(
                                "service_layer.services.create_user",
                                return_value={
                                    "id": 1,
                                    "name": "Test User",
                                    "role": "student",
                                    "university": "HS-KE",
                                },
                            ):
                                with patch(
                                    "service_layer.services." "get_courses_by_uni",
                                    return_value={
                                        "courses": [
                                            {
                                                "id": 1,
                                                "name": "course-1",
                                                "university": "HS-KE",
                                            }
                                        ],
                                    },
                                ):
                                    with patch(
                                        "service_layer.services."
                                        "get_student_by_user_id",
                                        return_value={
                                            "id": 1,
                                            "name": "Test User",
                                            "role": "student",
                                            "university": "HS-KE",
                                        },
                                    ):
                                        with patch(
                                            "service_layer.services."
                                            "add_student_to_course",
                                            return_value={
                                                "state": "ok",
                                            },
                                        ):
                                            with patch("flask.redirect"):
                                                with patch(
                                                    "service_layer."
                                                    "lti.config."
                                                    "ToolConfigJson.get_platform",
                                                    return_valule="moodle",
                                                ):
                                                    with patch(
                                                        "service_layer."
                                                        "lti.config."
                                                        "ToolConfigJson."
                                                        "decode_platform",
                                                        return_valule="moodle_decoded",
                                                    ):
                                                        with patch(
                                                            "service_layer."
                                                            "services."
                                                            "get_student_by_user_id",
                                                            return_value={
                                                                "id": 1,
                                                                "name": "Test User",
                                                                "role": "student",
                                                            },
                                                        ):
                                                            self.oidc_login.id_token = (
                                                                MagicMock()
                                                            )  # noqa: E501
                                                            self.oidc_login.id_token.nonce = (  # noqa: E501
                                                                "valid_nonce"
                                                            )
                                                            self.oidc_login.id_token.sub = (  # noqa: E501
                                                                "user123"
                                                            )
                                                            self.oidc_login.id_token.name = "Test User"  # noqa: E501
                                                            self.oidc_login.id_token.__getitem__.side_effect = (  # noqa: E501
                                                                jwt_payload.__getitem__
                                                            )

                                                            response = (
                                                                self.oidc_login.lti_launch_from_id_token()  # noqa: E501
                                                            )

                                                            assert (
                                                                response.status
                                                                == "302 FOUND"
                                                            )  # noqa: E501

    def test_lti_launch_from_id_token_user_exists_in_db(self):
        # Create a mock request with the necessary attributes
        request_mock = MagicMock()
        request_mock.form = MagicMock()
        request_mock.form.get = MagicMock(
            side_effect=lambda k, type=str: {
                "state": "valid_state_jwt",
                "iss": "https://moodle.haski.app",
                "client_id": "VRCKkhKlZtHNHtD",
                "login_hint": "student",
                "lti_message_hint": "message_hint",
                "target_link_uri": "https://backend.ke.haski.app/lti_launch",
                "id_token": "valid_id_token_jwt",
            }.get(k, "")
        )
        request_mock.referrer = "https://example.com"
        self.oidc_login._request = request_mock

        jwt_payload = {
            "nonce": "valid_nonce",
            "iat": (
                datetime.datetime.utcnow() - datetime.timedelta(minutes=5)
            ).timestamp(),
            "exp": (
                datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
            ).timestamp(),
            "iss": os.environ.get("BACKEND_URL", "https://backend.haski.app"),
            "kid": "backendprivatekey",
            "state": "valid_state",
            "sub": "user123",
            "name": "Test User",
            "https://purl.imsglobal.org/spec/lti/claim/tool_platform": {
                "name": "Test University"
            },
            "https://purl.imsglobal.org/spec/lti/claim/roles": ["student"],
        }

        with patch(
            "service_layer.crypto.JWTKeyManagement.verify_jwt",
            return_value=jwt_payload,  # noqa: E501
        ):
            with patch(
                "service_layer.crypto.JWTKeyManagement.generate_nonce_jwt",
                return_value="mocked_nonce_jwt",
            ):
                with patch("service_layer.service.SessionServiceFlask.set"):
                    with patch(
                        "service_layer.service.SessionServiceFlask.get"
                    ) as mock_get_session:
                        mock_get_session.side_effect = (
                            lambda nonce, key: "valid_state"
                            if key == "state" and nonce == "valid_nonce"
                            else None
                        )
                        with patch(
                            "service_layer.services.get_user_by_lms_id",
                            return_value={
                                "id": 1,
                                "name": "Test User",
                                "role": "student",
                            },
                        ):
                            with patch("flask.redirect"):
                                with patch(
                                    "service_layer."
                                    "lti.config.ToolConfigJson.get_platform",
                                    return_valule="moodle",
                                ):
                                    with patch(
                                        "service_layer.lti.config."
                                        "ToolConfigJson.decode_platform",
                                        return_valule="moodle_decoded",
                                    ):
                                        with patch(
                                            "service_layer.services."
                                            "get_student_by_user_id",
                                            return_value={
                                                "id": 1,
                                                "name": "Test User",
                                                "role": "student",
                                            },
                                        ):
                                            self.oidc_login.id_token = MagicMock()
                                            self.oidc_login.id_token.nonce = (
                                                "valid_nonce"
                                            )
                                            self.oidc_login.id_token.sub = "user123"
                                            self.oidc_login.id_token.name = "Test User"
                                            self.oidc_login.id_token.__getitem__.side_effect = (  # noqa: E501
                                                jwt_payload.__getitem__
                                            )

                                            response = (
                                                self.oidc_login.lti_launch_from_id_token()  # noqa: E501
                                            )

                                            assert response.status == "302 FOUND"

    def test_get_cookie_expiration_successful(self):
        # Mock request data
        json_data = {"nonce": "valid_nonce_jwt"}

        # Mock nonce payload and user data
        nonce_payload = {"nonce": "valid_nonce"}
        id_token = {"https://purl.imsglobal.org/spec/lti/claim/roles": ["student"]}
        user_data = {
            "id": 1,
            "user_id": "user_123",
            "lms_user_id": "lms_user_456",
            "university": "Test University",
            "role_id": 1,
        }

        # Mock methods and services
        with patch.object(self.oidc_login, "_request") as mock_request:
            mock_request.get_json.return_value = json_data
            mock_request.referrer = "https://backend.haski.app"

            with patch(
                "service_layer.crypto.JWTKeyManagement.verify_jwt",
                return_value=nonce_payload,
            ):
                with patch(
                    "service_layer.crypto.JWTKeyManagement.verify_jwt_payload",
                    return_value=True,
                ):
                    with patch(
                        "service_layer." "service." "SessionServiceFlask.get"
                    ) as mock_get_session:
                        mock_get_session.side_effect = lambda nonce, key: {
                            ("valid_nonce", "id_token"): id_token,
                            ("valid_nonce", "user"): user_data,
                        }.get((nonce, key), None)

                        with patch(
                            "service_layer."
                            "crypto."
                            "JWTKeyManagement."
                            "generate_state_jwt",
                            return_value="mocked_state_jwt",
                        ):
                            with patch(
                                "service_layer."
                                "lti."
                                "Roles."
                                "RoleMapper."
                                "get_role",
                                return_value="course creator",
                            ):
                                with patch(
                                    "service_layer."
                                    "lti."
                                    "Roles."
                                    "RoleMapper."
                                    "get_permissions",
                                    return_value=[Permissions.READ, Permissions.WRITE],
                                ):
                                    response = self.oidc_login.get_cookie_expiration()
                                    assert response.status == "200 OK"

    def test_lti_launch_from_id_token_user_does_not_exist_in_db_role_course_creator(self):
        # Create a mock request with the necessary attributes
        request_mock = MagicMock()
        request_mock.form = MagicMock()
        request_mock.form.get = MagicMock(
            side_effect=lambda k, type=str: {
                "state": "valid_state_jwt",
                "iss": "https://moodle.haski.app",
                "client_id": "VRCKkhKlZtHNHtD",
                "login_hint": "student",
                "lti_message_hint": "message_hint",
                "target_link_uri": "https://backend.ke.haski.app/lti_launch",
                "id_token": "valid_id_token_jwt",
            }.get(k, "")
        )
        request_mock.referrer = "https://example.com"
        self.oidc_login._request = request_mock

        jwt_payload = {
            "nonce": "valid_nonce",
            "iat": (
                    datetime.datetime.utcnow() - datetime.timedelta(minutes=5)
            ).timestamp(),
            "exp": (
                    datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
            ).timestamp(),
            "iss": os.environ.get("BACKEND_URL", "https://backend.haski.app"),
            "kid": "backendprivatekey",
            "state": "valid_state",
            "sub": "user123",
            "name": "Test User",
            "https://purl.imsglobal.org/spec/lti/claim/tool_platform": {
                "name": "Test University"
            },
            "https://purl.imsglobal.org/spec/lti/claim/roles": ["student"],
        }

        with patch(
                "service_layer.crypto.JWTKeyManagement.verify_jwt", return_value=jwt_payload
        ):
            with patch(
                    "service_layer.crypto.JWTKeyManagement.generate_nonce_jwt",
                    return_value="mocked_nonce_jwt",
            ):
                with patch("service_layer.service.SessionServiceFlask.set"):
                    with patch(
                            "service_layer.service.SessionServiceFlask.get"
                    ) as mock_get_session:
                        mock_get_session.side_effect = (
                            lambda nonce, key: "valid_state"
                            if key == "state" and nonce == "valid_nonce"
                            else None
                        )
                        with patch(
                                "service_layer.services.get_user_by_lms_id",
                                return_value={},
                        ):
                            with patch(
                                    "service_layer.services.create_user",
                                    return_value={
                                        "id": 1,
                                        "name": "Test User",
                                        "role": "course creator",
                                        "lms_user_id": "2",
                                        "university": "HS-KE",
                                    },
                            ):
                                with patch(
                                        "service_layer.services." "get_courses_by_uni",
                                        return_value={
                                            "courses": [
                                                {
                                                    "id": 1,
                                                    "name": "course-1",
                                                    "university": "HS-KE",
                                                }
                                            ],
                                        },
                                ):
                                    with patch(
                                            "service_layer.services."
                                            "get_student_by_user_id",
                                            return_value={
                                                "id": 1,
                                                "name": "Test User",
                                                "role": "course creator",
                                                "university": "HS-KE",
                                            },
                                    ):
                                        with patch(
                                                "service_layer.services."
                                                "add_student_to_course",
                                                return_value={
                                                    "state": "ok",
                                                },
                                        ):
                                            with patch("flask.redirect"):
                                                with patch(
                                                        "service_layer."
                                                        "lti.config."
                                                        "ToolConfigJson.get_platform",
                                                        return_valule="moodle",
                                                ):
                                                    with patch(
                                                            "service_layer."
                                                            "lti.config."
                                                            "ToolConfigJson."
                                                            "decode_platform",
                                                            return_valule="moodle_decoded",
                                                    ):
                                                        with patch(
                                                                "service_layer."
                                                                "services."
                                                                "get_student_by_user_id",
                                                                return_value={
                                                                    "id": 1,
                                                                    "name": "Test User",
                                                                    "role": "course creator",
                                                                },
                                                        ):
                                                            with patch(
                                                                "service_layer."
                                                                "services."
                                                                "get_default_learning_path_by_university",
                                                                return_value=[
                                                                    {'id': 1, 'classification': 'LZ', 'position': 1, 'disabled': False, 'university': 'HS-KE'},
                                                                    {'id': 2, 'classification': 'FO', 'position': 2, 'disabled': False, 'university': 'HS-KE'},
                                                                    {'id': 3, 'classification': 'BE', 'position': 3, 'disabled': False, 'university': 'HS-KE'},
                                                                    {'id': 4, 'classification': 'AB', 'position': 4, 'disabled': False, 'university': 'HS-KE'},
                                                                    {'id': 5, 'classification': 'ÜB', 'position': 5, 'disabled': False, 'university': 'HS-KE'},
                                                                    {'id': 6, 'classification': 'ZF', 'position': 6, 'disabled': False, 'university': 'HS-KE'},
                                                                    {'id': 7, 'classification': 'ZL', 'position': 7, 'disabled': False, 'university': 'HS-KE'}, 
                                                                    {'id': 8, 'classification': 'EK', 'position': 9000, 'disabled': True, 'university': 'HS-KE'}, 
                                                                    {'id': 9, 'classification': 'KÜ', 'position': 9001, 'disabled': True, 'university': 'HS-KE'}, 
                                                                    {'id': 10, 'classification': 'AN', 'position': 9002, 'disabled': True, 'university': 'HS-KE'}, 
                                                                    {'id': 11, 'classification': 'RQ', 'position': 9003, 'disabled': True, 'university': 'HS-KE'}, 
                                                                    {'id': 12, 'classification': 'SE', 'position': 9004, 'disabled': True, 'university': 'HS-KE'}]
                                                            ):
                                                                with patch(
                                                            "service_layer."
                                                                  "services."
                                                                  "get_topics_by_student_and_course_id",
                                                                    return_value={
                                                                        'topics':
                                                                            [
                                                                                {
                                                                                    'id': 1,
                                                                                    'lms_id': 1,
                                                                                    'is_topic': True,
                                                                                    'parent_id': None,
                                                                                    'contains_le': True,
                                                                                    'name': 'General',
                                                                                    'university': 'New Site',
                                                                                    'created_by': 'muster student',
                                                                                    'created_at': datetime.datetime(2025, 6, 17, 0, 0),
                                                                                    'last_updated': None,
                                                                                    'student_topic': {'id': 4, 'student_id': 4, 'topic_id': 1, 'done': False, 'done_at': None, 'visits': []}
                                                                                }
                                                                            ]
                                                                    }
                                                                ):
                                                                    with patch(
                                                                        "service_layer."
                                                                        "services."
                                                                        "get_student_lpath_le_algorithm",
                                                                        return_value={
                                                                            'id': 7,
                                                                            'student_id': 5,
                                                                            'topic_id': 1,
                                                                            'algorithm_id': 4
                                                                        }

                                                                    ):
                                                                        with patch(
                                                                            "service_layer."
                                                                            "services."
                                                                            "get_learning_path_algorithm_by_id",
                                                                            return_value={
                                                                                'id': 4,
                                                                                'short_name': 'graf',
                                                                                'full_name': 'Graf et al.'
                                                                            }
                                                                        ):
                                                                            with patch(
                                                                                "service_layer."
                                                                                "services."
                                                                                "create_learning_path",
                                                                                return_value={
                                                                                    'id': 5,
                                                                                    'student_id': 5,
                                                                                    'course_id': 1,
                                                                                    'topic_id': 1, 'based_on': 'graf',
                                                                                    'path': 'FO',
                                                                                    'calculated_on': datetime.datetime(2025, 6, 17, 16, 4, 4, tzinfo=datetime.timezone(datetime.timedelta(seconds=7200)))
                                                                                }
                                                                            ):
                                                                                self.oidc_login.id_token = (
                                                                                    MagicMock()
                                                                                )  # noqa: E501
                                                                                self.oidc_login.id_token.nonce = (  # noqa: E501
                                                                                    "valid_nonce"
                                                                                )
                                                                                self.oidc_login.id_token.sub = (  # noqa: E501
                                                                                    "user123"
                                                                                )
                                                                                self.oidc_login.id_token.name = "Test User"  # noqa: E501
                                                                                self.oidc_login.id_token.__getitem__.side_effect = (  # noqa: E501
                                                                                    jwt_payload.__getitem__
                                                                                )

                                                                                response = (
                                                                                    self.oidc_login.lti_launch_from_id_token()  # noqa: E501
                                                                                )

                                                                                assert (
                                                                                        response.status
                                                                                        == "302 FOUND"
                                                                                )  # noqa: E501

    def test_get_logout(self):
        with patch.object(
            self.oidc_login, "_request", _request=MagicMock
        ) as mock_request:
            mock_request.referrer = "https://example.com"

            response = self.oidc_login.get_logout()

            self.assertEqual(response.status_code, 204)
            set_cookie_header = response.headers.get("Set-Cookie", "")
            self.assertIn("haski_state=", set_cookie_header)  # Check for empty value
            self.assertIn("Max-Age=0", set_cookie_header)
            self.assertIn("Domain=example.com", set_cookie_header)
            self.assertIn("HttpOnly", set_cookie_header)
            self.assertIn("SameSite=Lax", set_cookie_header)
            self.assertIn("Path=/", set_cookie_header)

            expires_part = next(
                (
                    part
                    for part in set_cookie_header.split("; ")
                    if part.startswith("Expires=")
                ),
                None,
            )
            self.assertIsNotNone(
                expires_part, "Expires attribute not found in Set-Cookie header"
            )
            expires_date = expires_part.split("=", 1)[1]
            from email.utils import parsedate_to_datetime

            expires_datetime = parsedate_to_datetime(expires_date)
            self.assertLess(
                expires_datetime,
                datetime.datetime.now(datetime.timezone.utc),
                "Expires date should be in the past",
            )
