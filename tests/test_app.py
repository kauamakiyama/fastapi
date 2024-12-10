from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get("/")  # ação

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {"message": "Olá Mundo!"}


def test_create_user(client):
    response = client.post(  # envia o UserSchema
        "/users/",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "secret",
        },
    )

    # valida o status code
    assert response.status_code == HTTPStatus.CREATED
    # valida o UserPublic
    assert response.json() == {
        "username": "alice",
        "email": "alice@example.com",
        "id": 1,
    }


def test_read_users(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "username": "alice",
                "email": "alice@example.com",
                "id": 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "password": "123",
            "username": "teste2",
            "email": "test@test.com",
            "id": 1,
        },
    )

    assert response.json() == {
        "username": "teste2",
        "email": "test@test.com",
        "id": 1,
    }


def test_delete_user(client):
    response = client.delete("/users/1")

    assert response.json() == {"message": "User deleted"}
