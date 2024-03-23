from abc import ABC, abstractmethod
from typing import Tuple

from httpx import Response

from models.types import CreditCardDictIn


class CreditCardService(ABC):
    @abstractmethod
    def addCreditCard(self, payload: CreditCardDictIn) -> Tuple[Response, bool]:
        raise NotImplementedError

    @abstractmethod
    def getAllCreditCards(self) -> Tuple[Response, bool]:
        raise NotImplementedError

    @abstractmethod
    def getCreditCard(self, id: str) -> Tuple[Response, bool]:
        raise NotImplementedError

    @abstractmethod
    def updateCreditCard(self, id: str, payload: CreditCardDictIn) -> Tuple[Response, bool]:
        raise NotImplementedError

    @abstractmethod
    def deleteCreditCard(self, id: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def extractCreditCard(self, path: str) -> Tuple[Response, bool]:
        raise NotImplementedError
