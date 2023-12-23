from datetime import datetime
from typing import Literal

from models.types import CreditCardDictOut


class CreditCard:
    def __init__(
        self,
        id: str,
        code: str,
        cardType: Literal["500", "1000", "2000"],
        createdAt: datetime,
        updatedAt: datetime,
    ) -> None:
        self.id = id
        self.code = code
        self.cardType = cardType
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    @classmethod
    def fromDict(cls, dict: CreditCardDictOut) -> "CreditCard":
        return cls(**dict)

    def toDict(self) -> CreditCardDictOut:
        return {
            "id": self.id,
            "code": self.code,
            "cardType": self.cardType,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
        }
