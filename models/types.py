from datetime import datetime
from typing import Dict, List, Literal, TypedDict


class LoginDict(TypedDict):
    email: str
    password: str


class CreditCardDictIn(TypedDict):
    code: str
    cardType: Literal["500", "1000", "2000", "5000", "10000"]


class CreditCardDictOut(TypedDict):
    publicId: str
    code: str
    cardType: Literal["500", "1000", "2000", "5000", "10000"]
    isValid: bool
    createdAt: datetime
    updatedAt: datetime

    @staticmethod
    def columnNames() -> Dict[str, str]:
        return {
            "publicId": "id",
            "code": "code",
            "cardType": "Card type",
            "isValid": "Is valid",
            "createdAt": "Created at",
            "updatedAt": "Updated at",
        }


class ExtractCreditCardDict(TypedDict):
    cardNumbers: List[str]
    message: str


class RCParams(TypedDict):
    axesFaceColor: str
    figureFaceColor: str
    savefigFaceColor: str
    axesEdgecolor: str
    xTickColor: str
    yTickColor: str
