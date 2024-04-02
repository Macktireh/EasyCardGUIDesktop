from http import HTTPStatus
from typing import Any, Callable, Dict, Optional, Tuple

from httpx import USE_CLIENT_DEFAULT, Client, ConnectError, Response, TimeoutException
from httpx._types import QueryParamTypes, RequestFiles, TimeoutTypes

from config.settings import BASE_API_URL
from models.types import AllCreditCardDictIn, CreditCardDictIn
from services.authServiceImpl import AuthServiceImpl
from services.creditCardService import CreditCardService


class CreditCardServiceImpl(CreditCardService):
    def __init__(self, callback: Optional[Callable[[], None]] = None) -> None:
        self.HTTPClient = Client(base_url=BASE_API_URL)
        self.authService = AuthServiceImpl()
        self.callback = callback

    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: QueryParamTypes | None = None,
        json_data: Dict[str, Any] | None = None,
        files: RequestFiles | None = None,
        timeout: TimeoutTypes = USE_CLIENT_DEFAULT,
        callback: Optional[Callable[[], None]] = None,
    ) -> Tuple[Response, bool]:
        self.apiKey = self.authService.getAPIKey()
        if not self.apiKey:
            return Response(HTTPStatus.INTERNAL_SERVER_ERROR, json={"message": "Server error"}), False

        if params is None:
            params = {}

        params["apiKey"] = self.apiKey

        try:
            match method:
                case "post":
                    response = self.HTTPClient.post(
                        endpoint, params=params, json=json_data, files=files, timeout=timeout
                    )
                case "get":
                    response = self.HTTPClient.get(endpoint, params=params, timeout=timeout)
                case "patch":
                    response = self.HTTPClient.patch(endpoint, params=params, data=json_data, timeout=timeout)
                case "delete":
                    response = self.HTTPClient.delete(endpoint, params=params, timeout=timeout)
                case _:
                    return None, False
        except (ConnectError, TimeoutException):
            return Response(HTTPStatus.INTERNAL_SERVER_ERROR, json={"message": "Server error"}), False

        isAuthorized = response.status_code != HTTPStatus.UNAUTHORIZED

        if not isAuthorized and callback:
            callback()
        elif not isAuthorized and self.callback:
            self.callback()

        return response, isAuthorized

    def addCreditCard(
        self, payload: CreditCardDictIn, callback: Optional[Callable[[], None]] = None
    ) -> Tuple[Response, bool]:
        return self._make_request(method="post", endpoint="/cards", json_data=payload, callback=callback)

    def addAllCreditCards(
        self, payload: AllCreditCardDictIn, callback: Optional[Callable[[], None]] = None
    ) -> Tuple[Response, bool]:
        return self._make_request(method="post", endpoint="/cards/all", json_data=payload, callback=callback)

    def getAllCreditCards(self, callback: Optional[Callable[[], None]] = None) -> Tuple[Response, bool]:
        return self._make_request(method="get", endpoint="/cards", callback=callback)

    def getCreditCard(self, id: str, callback: Optional[Callable[[], None]] = None) -> Tuple[Response, bool]:
        return self._make_request(method="get", endpoint=f"/cards/{id}", callback=callback)

    def updateCreditCard(
        self, id: str, payload: CreditCardDictIn, callback: Optional[Callable[[], None]] = None
    ) -> Tuple[Response, bool]:
        return self._make_request(method="patch", endpoint=f"/cards/{id}", json_data=payload, callback=callback)

    def deleteCreditCard(self, id: str, callback: Optional[Callable[[], None]] = None) -> Tuple[Response, bool]:
        return self._make_request(method="delete", endpoint=f"/cards/{id}", callback=callback)

    def extractCreditCard(self, path: str, callback: Optional[Callable[[], None]] = None) -> Tuple[Response, bool]:
        with open(path, "rb") as image:
            return self._make_request(
                method="post",
                endpoint="/cards/extract",
                files={"image": image},
                timeout=10,
                callback=callback,
            )
