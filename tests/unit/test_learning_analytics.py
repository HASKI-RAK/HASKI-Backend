from typing import Any

import pytest

from service_layer import learning_analytics as la

_TOKEN_ENV_VARS = (
    "LAAC_BEARER_TOKEN",
    "LAAC_API_TOKEN",
    "LAAC_DEV_JWT",
    "DEV_JWT",
)


def _clear_token_env(monkeypatch: pytest.MonkeyPatch) -> None:
    for var in _TOKEN_ENV_VARS:
        monkeypatch.delenv(var, raising=False)


def test_laac_base_url_and_verify_ssl_respects_env(monkeypatch):
    monkeypatch.delenv("LAAC_BASE_URL", raising=False)
    monkeypatch.delenv("LAAC_VERIFY_SSL", raising=False)

    assert la._laac_base_url() == "https://laac.haski.app/api/v1"
    assert la._laac_verify_ssl() is True

    monkeypatch.setenv("LAAC_BASE_URL", "https://custom.example/api")
    monkeypatch.setenv("LAAC_VERIFY_SSL", "no")

    assert la._laac_base_url() == "https://custom.example/api"
    assert la._laac_verify_ssl() is False


@pytest.mark.parametrize("token_env", _TOKEN_ENV_VARS)
def test_laac_headers_support_multiple_token_variables(monkeypatch, token_env):
    _clear_token_env(monkeypatch)
    monkeypatch.delenv("LAAC_API_KEY", raising=False)

    monkeypatch.setenv(token_env, "secret-token")
    headers = la._laac_headers()

    assert headers["Accept"] == "application/json"
    assert headers["Authorization"] == "Bearer secret-token"
    assert "x-api-key" not in headers


def test_laac_headers_include_api_key(monkeypatch):
    _clear_token_env(monkeypatch)
    monkeypatch.setenv("LAAC_API_KEY", "api-key-123")

    headers = la._laac_headers()

    assert headers["x-api-key"] == "api-key-123"
    assert "Authorization" not in headers


def test_fetch_element_clicks_success_uses_env_config(monkeypatch):
    class DummyResponse:
        def __init__(self):
            self.status_code = 200
            self.text = "ok"

        def json(self) -> dict[str, Any]:
            return {"result": {"value": [{"type": "CT", "dimensionScore": 11}]}}

    captured = {}

    def fake_get(url, *, params, headers, timeout, verify):
        captured["url"] = url
        captured["params"] = params
        captured["headers"] = headers
        captured["timeout"] = timeout
        captured["verify"] = verify
        return DummyResponse()

    _clear_token_env(monkeypatch)
    monkeypatch.setenv("DEV_JWT", "dev-token")
    monkeypatch.setenv("LAAC_API_KEY", "api-key")
    monkeypatch.setenv("LAAC_BASE_URL", "https://api.example.com/base/")
    monkeypatch.setenv("LAAC_VERIFY_SSL", "false")
    monkeypatch.setattr(la.requests, "get", fake_get)

    result = la.fetch_element_clicks("user-1", course_id=7, topic_id=3)

    assert result == [{"type": "CT", "dimensionScore": 11}]
    assert captured["url"] == "https://api.example.com/base/metrics/element-clicks"
    assert captured["params"] == {"userId": "user-1", "courseId": 7, "topicId": 3}
    assert captured["headers"]["Authorization"] == "Bearer dev-token"
    assert captured["headers"]["x-api-key"] == "api-key"
    assert captured["verify"] is False
    assert captured["timeout"] == 5


def test_fetch_element_clicks_logs_warning_on_failure(monkeypatch):
    class DummyResponse:
        status_code = 502
        text = "bad gateway"

        def json(self):  # pragma: no cover - not used
            return {}

    def fake_get(*_, **__):
        return DummyResponse()

    captured: dict[str, str] = {}

    monkeypatch.setattr(la.requests, "get", fake_get)
    monkeypatch.setattr(
        la.logger,
        "warning",
        lambda *args, **kwargs: captured.setdefault(
            "message",
            args[0] % args[1:] if len(args) > 1 else args[0],
        ),
    )

    result = la.fetch_element_clicks("user-2")

    assert result == []
    assert "element-clicks request failed" in captured.get("message", "")


def test_fetch_element_clicks_requires_user_id():
    assert la.fetch_element_clicks(None) == []


def test_map_clicks_to_classification_filters_invalid_entries():
    payload = [
        {"type": "CT", "dimensionScore": 5},
        {"type": "UNKNOWN", "dimensionScore": 99},
        {"type": "SE", "dimensionScore": "oops"},
    ]

    result = la.map_clicks_to_classification(payload)

    assert result == {"KÜ": 5.0}


def test_get_click_scores_for_learning_path_invokes_fetch(monkeypatch):
    captured = {}

    def fake_fetch(*, user_id, course_id, topic_id):
        captured.update(
            {
                "user_id": user_id,
                "course_id": course_id,
                "topic_id": topic_id,
            }
        )
        return [
            {"type": "CT", "dimensionScore": 4},
            {"type": "SE", "dimensionScore": 3},
        ]

    monkeypatch.setattr(la, "fetch_element_clicks", fake_fetch)

    scores = la.get_click_scores_for_learning_path("student", 10, 5)

    assert captured == {"user_id": "student", "course_id": 10, "topic_id": 5}
    assert scores == {"KÜ": 4.0, "SE": 3.0}
