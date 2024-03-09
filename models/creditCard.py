from dataclasses import dataclass
from datetime import datetime
from typing import Literal

from models.types import CreditCardDictOut


@dataclass
class CreditCard:
    id: str
    code: str
    cardType: Literal["500", "1000", "2000", "5000", "10000"]
    createdAt: datetime
    updatedAt: datetime

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
