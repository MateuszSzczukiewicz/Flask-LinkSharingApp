from link_sharing_app.db import get_db


def test_get_user_by_id(client, app):
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Success.",
        "data": {
            "email": "test@gmail.com",
            "first_name": "Test",
            "last_name": "Testowy",
            "image_url": "https://link_to_image.com",
        },
    }

    with app.app_context():
        assert dict(
            get_db()
            .execute(
                "SELECT email, first_name, last_name, image_url FROM users WHERE id = 1"
            )
            .fetchone()
        ) == {
            "email": "test@gmail.com",
            "first_name": "Test",
            "last_name": "Testowy",
            "image_url": "https://link_to_image.com",
        }


def test_get_edit_by_id(client, app):
    response = client.patch(
        "/users/1", json={"first_name": "Atest", "last_name": "Atestowy"}
    )
    assert response.status_code == 200
    assert response.get_json() == {"message": "User edited successfully."}

    with app.app_context():
        assert dict(
            get_db()
            .execute("SELECT first_name, last_name FROM users WHERE id = 1")
            .fetchone()
        ) == {"first_name": "Atest", "last_name": "Atestowy"}


def test_delete_user_by_id(client, app):
    response = client.delete("/users/1")

    assert response.status_code == 200
    assert response.get_json() == {"message": "User deleted successfully."}

    with app.app_context():
        assert get_db().execute("SELECT * FROM users WHERE id = 1").fetchone() is None
