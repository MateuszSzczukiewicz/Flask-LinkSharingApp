import os

from dotenv import load_dotenv

from link_sharing_app import create_app

load_dotenv()


def test_app_health():
    app = create_app()
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data == {"status": "ok"}


def test_create_app_default_config(tmp_path):
    app = create_app({"DATABASE": str(tmp_path / "test_db.sqlite")})
    secret_key = os.getenv("SECRET_KEY")
    assert app.config["SECRET_KEY"] == secret_key
    assert app.config["DATABASE"] == str(tmp_path / "test_db.sqlite")


def test_create_app_with_test_config():
    test_config = {"SECRET_KEY": "test_secret", "DATABASE": "test_db.sqlite"}
    app = create_app(test_config)
    assert app.config["SECRET_KEY"] == "test_secret"
    assert app.config["DATABASE"] == "test_db.sqlite"


def test_create_app_os_makedirs_fails(monkeypatch):
    def fake_makedirs(path):
        raise OSError("Simulated error")

    monkeypatch.setattr(os, "makedirs", fake_makedirs)
    app = create_app()
    assert app is not None
