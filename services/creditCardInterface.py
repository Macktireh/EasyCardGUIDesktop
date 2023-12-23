from abc import ABC, abstractmethod
from typing import List

from models.creditCard import CreditCard
from models.types import CreditCardDictIn, ExtractCreditCardDict


class CreditCardInterface(ABC):
    @abstractmethod
    def addCreditCard(self, payload: CreditCardDictIn) -> CreditCard: ...

    @abstractmethod
    def getAllCreditCards(self) -> List[CreditCard]: ...

    @abstractmethod
    def getCreditCard(self, id: str) -> CreditCard: ...

    @abstractmethod
    def updateCreditCard(self, id: str, payload: CreditCardDictIn) -> CreditCard: ...

    @abstractmethod
    def deleteCreditCard(self, id: str) -> None: ...
    
    @abstractmethod
    def extractCreditCard(self, path: str) -> ExtractCreditCardDict: ...
