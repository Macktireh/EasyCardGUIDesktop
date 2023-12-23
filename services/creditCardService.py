from typing import List

from httpx import Client

from models.creditCard import CreditCard
from models.types import CreditCardDictIn, CreditCardDictOut, ExtractCreditCardDict
from services.creditCardInterface import CreditCardInterface


class CreditCardService(CreditCardInterface):
    baseUrl = "http://localhost:8000"

    def __init__(self, HTTPClient: Client) -> None:
        self.HTTPClient = HTTPClient

    def addCreditCard(self, payload: CreditCardDictIn) -> CreditCard:
        response: CreditCardDictOut = self.HTTPClient.post(f"{self.baseUrl}/cards", data=payload).json()
        return CreditCard.fromDict(response)

    def getAllCreditCards(self) -> List[CreditCard]:
        response: List[CreditCardDictOut] = self.HTTPClient.get(f"{self.baseUrl}/cards").json()
        return [CreditCard.fromDict(card) for card in response]

    def getCreditCard(self, id: str) -> CreditCard:
        response: CreditCardDictOut = self.HTTPClient.get(f"{self.baseUrl}/cards/{id}").json()
        return CreditCard.fromDict(response)

    def updateCreditCard(self, id: str, payload: CreditCardDictIn) -> CreditCard:
        response: CreditCardDictOut = self.HTTPClient.put(f"{self.baseUrl}/cards/{id}", data=payload).json()
        return CreditCard.fromDict(response)

    def deleteCreditCard(self, id: str) -> None:
        self.HTTPClient.delete(f"{self.baseUrl}/cards/{id}")

    def extractCreditCard(self, path: str) -> ExtractCreditCardDict:
        with open(path, "rb") as image:
            response = self.HTTPClient.post(f"{self.baseUrl}/api/v2/extract-card-number", files={"image": image})
        return response.json()
