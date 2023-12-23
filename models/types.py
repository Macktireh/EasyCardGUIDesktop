from datetime import datetime
from typing import List, Literal, TypedDict


class CreditCardDictIn(TypedDict):
    code: str
    cardType: Literal["500", "1000", "2000"]


class CreditCardDictOut(TypedDict):
    id: str
    code: str
    cardType: Literal["500", "1000", "2000"]
    createdAt: datetime
    updatedAt: datetime


class ExtractCreditCardDict(TypedDict):
    cardNumbers: List[str]
    status: Literal["success", "fail"]
    message: str


class RCParams(TypedDict):
    axesFaceColor: str
    figureFaceColor: str
    savefigFaceColor: str
    axesEdgecolor: str
    xTickColor: str
    yTickColor: str
