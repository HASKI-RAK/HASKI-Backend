from entrypoints import flask_app
from service_layer import unit_of_work


def test_health_endpoint_reports_ok(client, monkeypatch):
    monkeypatch.setitem(flask_app._last_successful_checks, "database", None)

    response = client.get("/health")
    body = response.get_json()

    assert response.status_code == 200
    assert body["status"] == "UP"
    assert body["dependencies"]["database"]["status"] == "UP"
    assert "message_queue" in body["dependencies"]
    assert isinstance(body["uptime_seconds"], int)
    assert body["service"]["version"]


def test_health_endpoint_reports_db_failure(client, monkeypatch):
    class BrokenSession:
        def execute(self, *args, **kwargs):
            raise RuntimeError("db down")

        def close(self):
            pass

    monkeypatch.setattr(
        unit_of_work, "DEFAULT_SESSION_FACTORY", lambda: BrokenSession()
    )

    response = client.get("/health")
    body = response.get_json()

    assert response.status_code == 503
    assert body["status"] == "DOWN"
    assert body["dependencies"]["database"]["status"] == "DOWN"
    assert body["dependencies"]["database"]["details"]
