import os
import unittest
from unittest.mock import MagicMock, patch

from errors import errors as err
from service_layer.lti.config.ToolConfigJson import ToolConfigJson
from service_layer.lti.OIDCLoginFlask import OIDCLoginFlask

# ignore E501
config_file = {
    "https://moodle.haski.app": {
        "default": True,
        "client_id": "VRCKkhKlZtHNHtD",
        "tool_url": "https://backend.haski.app",
        "frontend_login_url": "https://haski.app/login",
        "target_link_uri": "https://backend.haski.app/lti_launch",
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
    "target_link_uri": "https://backend.haski.app/lti_launch",
    "lti_deployment_id": "1",
}


# pytest tests\unit\lti\test_OIDCLoginFlask.py --cov


class TestOIDCLoginFlask(unittest.TestCase):
    @patch.multiple(
        ToolConfigJson,
        load_config=MagicMock(return_value=config_file),
    )
    @patch.multiple(os.path, isfile=MagicMock(return_value=True))
    def setUp(self):
        self.request = MagicMock()
        self.oidc_login = OIDCLoginFlask(self.request, ToolConfigJson())
        self.tool_config = ToolConfigJson()
        # self.tool_config = MagicMock()
        # self.self.oidc_login = OIDCLoginFlask(self.request, self.tool_config)

    def test_tool_config_decode_platform(self):
        # dont need to check every value, just one
        # with patch.multiple(
        #     ToolConfigJson,
        #     get_platform=MagicMock(
        #         return_value=config_file["https://moodle.haski.app"]
        #     ),
        # ):
        # with patch.object(os.path, "isfile", return_value=True):
        #     with patch.object(
        #         ToolConfigJson,
        #         "load_config",
        #         return_value=config_file,
        #     ):
        platform = self.tool_config.decode_platform(
            self.tool_config.get_platform("https://moodle.haski.app")
        )
        self.assertEqual(
            platform.platform_name,
            "HASKI",
        )

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
            with self.assertRaises(
                err.ErrorException,
            ):
                # "(MissingParameterError(None, 'Missing parameters in request.', 400), 'Error in checking parameters', 400)", # noqa: E501
                self.oidc_login.check_params()

    def test_check_params_missing_platform(self):
        # _iss_conf_dict remove the platform
        # self.self.oidc_login._tool_config._iss_conf_dict.pop(
        #     "https://moodle.haski.app", None
        # )
        with patch.object(
            ToolConfigJson,
            "get_platform",
            return_value=None,
        ):
            with patch.object(self.oidc_login, "_request", _request=MagicMock):
                with self.assertRaises(
                    err.ErrorException,
                ):
                    self.oidc_login.check_params()

    def test_check_params_wrong_target_link_uri(self):
        with patch.object(self.oidc_login, "_request", _request=MagicMock) as mock_form:
            mock_form.form = form.copy()
            mock_form.form["target_link_uri"] = "wrong_uri"
            # "target_link_uri invalid Inner Exception: (None, 'target_link_uri is not from the same host', 400)",  # noqa: E501
            with self.assertRaises(
                err.ErrorException,
            ):
                self.oidc_login.check_params()
