from abc import ABC, abstractmethod

from httpx import Response

from models.types import LoginDict


class AuthService(ABC):
    """
    Service class for handling authentication-related operations.

    Attributes:
        apiKeyPath (Path): Path to the file containing the API key.

    Methods:
        login: Performs user login and saves the API key if successful.
        verifyAPIKey: Verifies the API key by making a request to the server.
        getAPIKey: Retrieves the API key from the file.
        saveAPIKey: Saves the provided API key to the file.
        logout: Removes the API key file, logging the user out.
    """

    @abstractmethod
    def login(self, payload: LoginDict) -> Response:
        """
        Performs user login and saves the API key if successful.

        Args:
            payload (LoginDict): Dictionary containing user credentials (email and password).

        Returns:
            Response: HTTP response containing the result of the login attempt.
        """
        raise NotImplementedError

    @abstractmethod
    def verifyAPIKey(self) -> Response:
        """
        Verifies the API key by making a request to the server.

        Returns:
            Response: HTTP response containing the result of the API key verification.
        """
        raise NotImplementedError

    @abstractmethod
    def getAPIKey(self) -> str | None:
        """
        Retrieves the API key from the file.

        Returns:
            str | None: The API key if found, otherwise None.
        """
        raise NotImplementedError

    @abstractmethod
    def saveAPIKey(self, apiKey: str) -> None:
        """
        Saves the provided API key to the file.

        Args:
            apiKey (str): The API key to be saved.
        """
        raise NotImplementedError

    @abstractmethod
    def logout(self) -> None:
        """
        Removes the API key file, logging the user out.
        """
        raise NotImplementedError
