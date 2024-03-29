from http import HTTPStatus
from typing import Callable, Tuple

from httpx import Client, ConnectError, Response, TimeoutException

from config.settings import BASE_API_URL
from models.types import CreditCardDictIn
from services.authServiceImpl import AuthServiceImpl
from services.creditCardService import CreditCardService


class CreditCardServiceImpl(CreditCardService):
    def __init__(self) -> None:
        self.HTTPClient = Client(base_url=BASE_API_URL)
        self.authService = AuthServiceImpl()

    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: dict = None,
        json_data=None,
        files=None,
        callback: Callable[[bool], None] | None = None,
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
            return Response(HTTPStatus.INTERNAL_SERVER_ERROR, json={"message": "Server error"}), False

        isAuthorized = response.status_code != HTTPStatus.UNAUTHORIZED

        if not isAuthorized and callback:
            callback()

        return response, isAuthorized

    def addCreditCard(
        self, payload: CreditCardDictIn, callback: Callable[[bool], None] | None = None
    ) -> Tuple[Response, bool]:
        return self._make_request("post", "/cards", json_data=payload, callback=callback)

    def getAllCreditCards(self, callback: Callable[[bool], None] | None = None) -> Tuple[Response, bool]:
        return self._make_request("get", "/cards", callback=callback)

    def getCreditCard(self, id: str, callback: Callable[[bool], None] | None = None) -> Tuple[Response, bool]:
        return self._make_request("get", f"/cards/{id}", callback=callback)

    def updateCreditCard(
        self, id: str, payload: CreditCardDictIn, callback: Callable[[bool], None] | None = None
    ) -> Tuple[Response, bool]:
        return self._make_request("patch", f"/cards/{id}", json_data=payload, callback=callback)

    def deleteCreditCard(self, id: str, callback: Callable[[bool], None] | None = None) -> Tuple[Response, bool]:
        return self._make_request("delete", f"/cards/{id}", callback=callback)

    def extractCreditCard(self, path: str, callback: Callable[[bool], None] | None = None) -> Tuple[Response, bool]:
        with open(path, "rb") as image:
            return self._make_request(
                "post", "/cards/extract", files={"image": image}, params={"timeout": 10}, callback=callback
            )
