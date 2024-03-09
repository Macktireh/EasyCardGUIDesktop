from datetime import datetime
from typing import List, Literal, TypedDict


class LoginDict(TypedDict):
    email: str
    password: str


class CreditCardDictIn(TypedDict):
    code: str
    cardType: Literal["500", "1000", "2000", "5000", "10000"]


class CreditCardDictOut(TypedDict):
    id: str
    code: str
    cardType: Literal["500", "1000", "2000", "5000", "10000"]
    createdAt: datetime
    updatedAt: datetime


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
