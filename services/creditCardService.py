from abc import ABC, abstractmethod
from typing import Callable, Tuple

from httpx import Response

from models.types import CreditCardDictIn


class CreditCardService(ABC):
    @abstractmethod
    def addCreditCard(
        self, payload: CreditCardDictIn, callback: Callable[[bool], None] | None = None
    ) -> Tuple[Response, bool]:
        raise NotImplementedError

    @abstractmethod
    def getAllCreditCards(self, callback: Callable[[bool], None] | None = None) -> Tuple[Response, bool]:
        raise NotImplementedError

    @abstractmethod
    def getCreditCard(self, id: str, callback: Callable[[bool], None] | None = None) -> Tuple[Response, bool]:
        raise NotImplementedError

    @abstractmethod
    def updateCreditCard(
        self, id: str, payload: CreditCardDictIn, callback: Callable[[bool], None] | None = None
    ) -> Tuple[Response, bool]:
        raise NotImplementedError

    @abstractmethod
    def deleteCreditCard(self, id: str, callback: Callable[[bool], None] | None = None) -> None:
        raise NotImplementedError

    @abstractmethod
    def extractCreditCard(self, path: str, callback: Callable[[bool], None] | None = None) -> Tuple[Response, bool]:
        raise NotImplementedError
