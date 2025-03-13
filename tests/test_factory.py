import os
from link_sharing_app import create_app


def test_create_app_default_config(tmp_path):
    app = create_app({"DATABASE": str(tmp_path / "test_db.sqlite")})
    assert app.config["SECRET_KEY"] == "dev"
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
