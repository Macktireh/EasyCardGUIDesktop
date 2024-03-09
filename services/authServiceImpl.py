from http import HTTPStatus
from pathlib import Path

from httpx import Client, ConnectError, Response, TimeoutException

from config.settings import BASE_API_URL
from models.types import LoginDict
from services.authService import AuthService


class AuthServiceImpl(AuthService):
    apiKeyPath = Path.home() / ".easycard" / "key.txt"

    def __init__(self) -> None:
        self.httpClient = Client(base_url=BASE_API_URL)

    def login(self, payload: LoginDict) -> Response:
        if not payload["email"] or not payload["password"]:
            return Response(HTTPStatus.BAD_REQUEST, json={"message": "Email and password are required"})
        try:
            response = self.httpClient.post("/auth/login", json=payload)
        except (ConnectError, TimeoutException):
            return Response(HTTPStatus.INTERNAL_SERVER_ERROR, json={"message": "Server error"})
        if response.is_success:
            self.saveAPIKey(response.json()["apiKey"])
        return response

    def verifyAPIKey(self) -> Response:
        apiKey = self.getAPIKey()
        if not apiKey:
            return Response(HTTPStatus.UNAUTHORIZED, json={"message": "API key not found"})
        try:
            response = self.httpClient.get(f"/auth/verify?apiKey={apiKey}")
        except (ConnectError, TimeoutException):
            return Response(HTTPStatus.INTERNAL_SERVER_ERROR, json={"message": "Server error"})
        return response

    def getAPIKey(self) -> str | None:
        if self.apiKeyPath.exists():
            return self.apiKeyPath.read_text().strip()
        return None

    def saveAPIKey(self, apiKey: str) -> None:
        self.apiKeyPath.parent.mkdir(parents=True, exist_ok=True)
        self.apiKeyPath.write_text(apiKey)

    def logout(self) -> None:
        self.apiKeyPath.unlink()
