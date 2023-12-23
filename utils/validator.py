class Validator:
    IMAGE_FORMATS = ["jpg", "jpeg", "png"]
    LENGTH_CODE = 11

    @staticmethod
    def validateImagePath(imagePath: str) -> bool:
        """
        Validate an image path.

        Args:
            imagePath (str): The path of the image to be validated.

        Returns:
            bool: True if the image path has a valid format, False otherwise.
        """
        if imagePath.split(".")[-1].lower() not in Validator.IMAGE_FORMATS:
            return False
        return True
    
    @staticmethod
    def validateCode(code: str) -> bool:
        """
        Validates the given code.

        Args:
            code (str): The code to be validated.

        Returns:
            bool: True if the code is valid, False otherwise.
        """
        if len(code) != Validator.LENGTH_CODE:
            return False
        if not code.isdigit():
            return False
        return True
