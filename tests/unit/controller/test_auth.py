from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestAuth:
    def test_register_user(self, mocker):
        # Mock the service function where it is used in the API
        mock_create_user = mocker.patch(
            "app.api.auth.createUser",
            return_value={"username": "testuser", "email": "testuser@example.com"},
        )

        payload = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpass",
        }
        response = client.post("/auth/register", json=payload)

        assert response.status_code == 200
        assert response.json() == {
            "username": "testuser",
            "email": "testuser@example.com",
        }
        mock_create_user.assert_called_once()

    def test_login_user(self, mocker):
        # Mock the service function where it is used in the API
        mock_login_user = mocker.patch(
            "app.api.auth.loginUser",
            return_value={"access_token": "fake-jwt-token", "token_type": "bearer"},
        )

        payload = {"email": "sample@gmail.com", "password": "samplepassword"}
        response = client.post("/auth/login", json=payload)
        assert response.status_code == 200
        assert response.json() == {
            "access_token": "fake-jwt-token",
            "token_type": "bearer",
        }
        mock_login_user.assert_called_once()
