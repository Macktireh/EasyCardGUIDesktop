from http import HTTPStatus
from typing import Tuple

from httpx import Client, ConnectError, Response, TimeoutException

from config.settings import BASE_API_URL
from models.types import CreditCardDictIn
from services.authServiceImpl import AuthServiceImpl
from services.creditCardService import CreditCardServiceImpl


class CreditCardServiceImpl(CreditCardServiceImpl):
    def __init__(self) -> None:
        self.HTTPClient = Client(base_url=BASE_API_URL)
        self.authService = AuthServiceImpl()

    def _make_request(
        self, method: str, endpoint: str, params: dict = None, json_data=None, files=None
    ) -> Tuple[Response, bool]:
        self.apiKey = self.authService.getAPIKey()
        if not self.apiKey:
            return None, False

        if params is None:
            params = {}

        params["apiKey"] = self.apiKey

        try:
            if method == "post":
                response = self.HTTPClient.post(endpoint, params=params, json=json_data, files=files)
            elif method == "get":
                response = self.HTTPClient.get(endpoint, params=params)
            elif method == "patch":
                response = self.HTTPClient.patch(endpoint, params=params, data=json_data)
            elif method == "delete":
                response = self.HTTPClient.delete(endpoint, params=params)
            else:
                return None, False
        except (ConnectError, TimeoutException):
            return None, False

        return response, response.status_code == HTTPStatus.UNAUTHORIZED

    def addCreditCard(self, payload: CreditCardDictIn) -> Tuple[Response, bool]:
        return self._make_request("post", "/cards", json_data=payload)

    def getAllCreditCards(self) -> Tuple[Response, bool]:
        return self._make_request("get", "/cards")

    def getCreditCard(self, id: str) -> Tuple[Response, bool]:
        return self._make_request("get", f"/cards/{id}")

    def updateCreditCard(self, id: str, payload: CreditCardDictIn) -> Tuple[Response, bool]:
        return self._make_request("patch", f"/cards/{id}", json_data=payload)

    def deleteCreditCard(self, id: str) -> Tuple[Response, bool]:
        return self._make_request("delete", f"/cards/{id}")

    def extractCreditCard(self, path: str) -> Tuple[Response, bool]:
        with open(path, "rb") as image:
            return self._make_request("post", "/cards/extract", files={"image": image}, params={"timeout": 10})
