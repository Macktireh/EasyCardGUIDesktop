from abc import ABC, abstractmethod
from typing import Callable, Optional, Tuple

from httpx import Response

from models.types import AllCreditCardDictIn, CreditCardDictIn


class CreditCardService(ABC):
    @abstractmethod
    def addCreditCard(self, payload: CreditCardDictIn, callback: Optional[Callable[[], None]]) -> Tuple[Response, bool]:
        """
        Adds a credit card to the database.

        Args:
            payload (CreditCardDictIn): The credit card information to be added.
            callback (Callable[[bool], None] | None, optional): A callback function to be called after the credit card is added. Defaults to None.

        Returns:
            Tuple[Response, bool]: A tuple containing the response from the server and a boolean indicating if the credit card was added successfully.
        """  # noqa: E501
        raise NotImplementedError

    @abstractmethod
    def addAllCreditCards(
        self, payload: AllCreditCardDictIn, callback: Optional[Callable[[], None]]
    ) -> Tuple[Response, bool]:
        """
        Adds a list of credit cards to the database.

        Args:
            payload (List[CreditCardDictIn]): The list of credit card information to be added.
            callback (Callable[[bool], None] | None, optional): A callback function to be called after the credit cards are added. Defaults to None.

        Returns:
            Tuple[Response, bool]: A tuple containing the response from the server and a boolean indicating if the credit cards were added successfully.
        """  # noqa: E501
        raise NotImplementedError

    @abstractmethod
    def getAllCreditCards(self, callback: Optional[Callable[[], None]]) -> Tuple[Response, bool]:
        """
        Retrieves all credit cards from the database.

        Args:
            callback (Callable[[bool], None] | None, optional): A callback function to be called after the credit cards are retrieved. Defaults to None.

        Returns:
            Tuple[Response, bool]: A tuple containing the response from the server and a boolean indicating if the credit cards were retrieved successfully.
        """  # noqa: E501
        raise NotImplementedError

    @abstractmethod
    def getCreditCard(self, id: str, callback: Optional[Callable[[], None]]) -> Tuple[Response, bool]:
        """
        Retrieves a specific credit card from the database.

        Args:
            id (str): The ID of the credit card to retrieve.
            callback (Callable[[bool], None] | None, optional): A callback function to be called after the credit card is retrieved. Defaults to None.

        Returns:
            Tuple[Response, bool]: A tuple containing the response from the server and a boolean indicating if the credit card was retrieved successfully.
        """  # noqa: E501
        raise NotImplementedError

    @abstractmethod
    def updateCreditCard(
        self, id: str, payload: CreditCardDictIn, callback: Optional[Callable[[], None]]
    ) -> Tuple[Response, bool]:
        """
        Updates a credit card in the database.

        Args:
            id (str): The ID of the credit card to update.
            payload (CreditCardDictIn): The updated credit card information.
            callback (Callable[[bool], None] | None, optional): A callback function to be called after the credit card is updated. Defaults to None.

        Returns:
            Tuple[Response, bool]: A tuple containing the response from the server and a boolean indicating if the credit card was updated successfully.
        """  # noqa: E501
        raise NotImplementedError

    @abstractmethod
    def deleteCreditCard(self, id: str, callback: Optional[Callable[[], None]]) -> None:
        """
        Deletes a credit card from the database.

        Args:
            id (str): The ID of the credit card to delete.
            callback (Callable[[bool], None] | None, optional): A callback function to be called after the credit card is deleted. Defaults to None.
        """  # noqa: E501
        raise NotImplementedError

    @abstractmethod
    def extractCreditCard(self, path: str, callback: Optional[Callable[[], None]]) -> Tuple[Response, bool]:
        """
        Extracts credit card information from an image file.

        Args:
            path (str): The path to the image file.
            callback (Callable[[bool], None] | None, optional): A callback function to be called after the credit card information is extracted. Defaults to None.

        Returns:
            Tuple[Response, bool]: A tuple containing the response from the server and a boolean indicating if the credit card information was extracted successfully.
        """  # noqa: E501
        raise NotImplementedError
