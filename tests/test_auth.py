import pytest
from flask import g
from flask import session
from link_sharing_app.db import get_db


def test_register(client, app):
    assert client.get("/auth/register").status_code == 200

    response = client.post("/auth/register", data={"email": "a@b.pl", "password": "a"})
    assert response.headers["Location"] == "/auth/login"

    with app.app_context():
        assert (
            get_db().execute("SELECT * FROM user WHERE email = 'a@b.pl'").fetchone()
            is not None
        )


@pytest.mark.parametrize(
    ("email", "password", "message"),
    (
        ("", "", b"Email is required."),
        ("a@b.pl", "", b"Password is required."),
        ("test@gmail.com", "a", b"already registered"),
    ),
)
def test_register_validate_input(client, email, password, message):
    response = client.post(
        "/auth/register", data={"email": email, "password": password}
    )
    assert message in response.data


def test_login(client, auth):
    assert client.get("/auth/login").status_code == 200

    response = auth.login()
    assert response.headers["Location"] == "/"

    with client:
        client.get("/")
        assert session["user_id"] == 1
        assert g.user["email"] == "test@gmail.com"


@pytest.mark.parametrize(
    ("email", "password", "message"),
    (
        ("bad@test.pl", "test", b"Incorrect email."),
        ("test@gmail.com", "bad", b"Incorrect password."),
    ),
)
def test_login_validate_input(auth, email, password, message):
    response = auth.login(email, password)
    assert message in response.data


def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert "user_id" not in session
