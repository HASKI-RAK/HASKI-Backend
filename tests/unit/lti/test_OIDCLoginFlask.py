from service_layer.lti.OIDCLoginFlask import OIDCLoginFlask
from service_layer.lti.OIDCLogin import OIDCLogin
from service_layer.lti.config.ToolConfigJson import ToolConfigJson
from flask import Flask, abort, jsonify, request, session
from werkzeug.wrappers.response import Response

import html

tool_config = ToolConfigJson()
oidc_login = OIDCLoginFlask(request, tool_config, session=session)


# pytest tests\unit\lti\test_OIDCLoginFlask.py --cov

def test_check_params():
    assert oidc_login.check_params


def test_auth_redirect():
    assert oidc_login.auth_redirect


def test_verify_state():
    assert oidc_login.verify_state


def test_verify_id_token():
    assert oidc_login.verify_id_token


def test_lti_launch_from_id_token():
    assert oidc_login.lti_launch_from_id_token


def test_get_login():
    assert oidc_login.get_login


def test_get_loginstatus():
    assert oidc_login.get_loginstatus


def test_get_logout():
    assert oidc_login.get_logout
