import os
import unittest
from unittest import mock
from unittest.mock import MagicMock, patch

import service_layer.lti.config.ToolConfigJson as ToolConfigJson
from errors import errors as err
from service_layer.crypto import JWTKeyManagement
from service_layer.lti.OIDCLoginFlask import OIDCLoginFlask

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


# pytest tests\unit\lti\test_OIDCLoginFlask.py --cov


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
                # "(MissingParameterError(None, 'Missing parameters in request.', 400), 'Error in checking parameters', 400)", # noqa: E501
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
            # "target_link_uri invalid Inner Exception: (None, 'target_link_uri is not from the same host', 400)",  # noqa: E501
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

    from unittest.mock import patch

    def test_verify_state_successful(self):
        # Create a mock request object
        with patch.object(self.oidc_login, "_request", _request=MagicMock) as mock_form:
            mock_form.form = form.copy()
            mock_form.host = host
            mock_form.form = {"state": "valid_state_jwt"}

            # Mock the JWTKeyManagement.verify_jwt method
            # to return a valid state form
            with patch(
                "service_layer.crypto.JWTKeyManagement.verify_jwt"
            ) as mock_verify_jwt:
                mock_verify_jwt.return_value = {"nonce": "valid_nonce"}

                # Mock the JWTKeyManagement.verify_state_jwt_payload
                # method to return True
                with patch(
                    "service_layer.crypto.JWTKeyManagement.verify_state_jwt_payload"
                ) as mock_verify_state_jwt_payload:
                    mock_verify_state_jwt_payload.return_value = True

                    # Call the verify_state method
                    self.oidc_login.verify_state()

                    # Assert that the mock methods were
                    # called with the correct arguments
                    mock_verify_jwt.assert_called_once_with("valid_state_jwt")
                    mock_verify_state_jwt_payload.assert_called_once_with(
                        {"nonce": "valid_nonce"}
                    )

    def test_verify_state_invalid_jwt(self):
        with patch.object(self.oidc_login, "_request", _request=MagicMock) as mock_form:
            mock_form.form = form.copy()
            mock_form.host = host
            mock_form.form = {"state": "invalid_state_jwt"}

            # Mock the JWTKeyManagement.verify_jwt method to return a valid state form
            with patch(
                "service_layer.crypto.JWTKeyManagement.verify_jwt"
            ) as mock_verify_jwt:
                mock_verify_jwt.side_effect = err.InvalidJWTError()

                # Call the verify_state method
                with self.assertRaisesRegex(
                    err.InvalidJWTError, "Invalid state signature"
                ):
                    self.oidc_login.verify_state()

                    # Assert that the mock methods were
                    # called with the correct arguments
                    mock_verify_jwt.assert_called_once_with("invalid_state_jwt")

    def test_verify_state_invalid_payload(self):
        with patch.object(self.oidc_login, "_request", _request=MagicMock) as mock_form:
            mock_form.form = form.copy()
            mock_form.host = host
            mock_form.form = {"state": "invalid_state_jwt"}

            # Mock the JWTKeyManagement.verify_jwt method to return a valid state form
            with patch(
                "service_layer.crypto.JWTKeyManagement.verify_jwt"
            ) as mock_verify_jwt:
                mock_verify_jwt.return_value = {"nonce": "invalid_nonce"}

                # Mock the JWTKeyManagement.verify_state_jwt_payload
                # method to return True
                with patch.object(
                    JWTKeyManagement,
                    "verify_state_jwt_payload",
                ) as mock_verify_state_jwt_payload:
                    mock_verify_state_jwt_payload.side_effect = err.InvalidJWTError()

                    # Call the verify_state method
                    with self.assertRaises(err.InvalidJWTError):
                        self.oidc_login.verify_state()

                        # Assert that the mock methods were
                        # called with the correct arguments
                        mock_verify_jwt.assert_called_once_with("invalid_state_jwt")
                        mock_verify_state_jwt_payload.assert_called_once_with(
                            {"nonce": "invalid_nonce"}
                        )

    def test_verify_id_token_error_in_form(self):
        with patch.object(self.oidc_login, "_request", _request=MagicMock) as mock_form:
            mock_form.form = form.copy()
            mock_form.host = host
            mock_form.form = {"error": "error"}

            # Call the verify_id_token method
            with self.assertRaisesRegex(err.ErrorException, "error"):
                self.oidc_login.verify_id_token()

    def test_verify_id_token_unverified_header_fail(self):
        with patch.object(self.oidc_login, "_request", _request=MagicMock) as mock_form:
            mock_form.form = form.copy()
            mock_form.host = host
            mock_form.form = {"id_token": "valid_id_token_jwt"}

            # Mock the JWTKeyManagement.verify_jwt method to return a valid id_token
            with patch(
                "service_layer.crypto.JWTKeyManagement.verify_jwt"
            ) as mock_verify_jwt:
                mock_verify_jwt.return_value = {"sub": "valid_sub"}

                with self.assertRaisesRegex(
                    err.InvalidJWTError, "Error loading header"
                ):
                    # Call the verify_id_token method
                    self.oidc_login.verify_id_token()

                    # Assert that the mock method was called with the correct argument
                    mock_verify_jwt.assert_called_once_with("valid_id_token_jwt")

    def test_verify_id_token_successful(self):
        with patch.object(self.oidc_login, "_request", _request=MagicMock) as mock_form:
            mock_form.form = form.copy()
            mock_form.host = host
            mock_form.form = {"id_token": "valid_id_token_jwt"}

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
                        # self.oidc_login._tool_config.get_platform = MagicMock(
                        #     return_value=config_file["https://moodle.haski.app"]
                        # )
                        # Mock the JWTKeyManagement.verify_jwt
                        # method to return a valid id_token
                        with patch(
                            "service_layer.crypto.JWTKeyManagement.verify_jwt"
                        ) as mock_verify_jwt:
                            mock_verify_jwt.return_value = {
                                "sub": "valid_sub",
                                "iss": "https://moodle.haski.app",
                            }

                            # Call the verify_id_token method
                            self.oidc_login.verify_id_token()

                            # Assert that the mock method was called
                            # with the correct argument and jose object
                            mock_verify_jwt.assert_called_with(
                                "valid_id_token_jwt", mock.ANY
                            )
