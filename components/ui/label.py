from typing import Literal, Tuple

from customtkinter import CTkBaseClass, CTkFont, CTkImage, CTkLabel

from components.ui.image import Image, imagesTupple
from config.settings import Color


class Label(CTkLabel):
    image: CTkImage | None = None

    def __init__(
        self,
        master: CTkBaseClass,
        text: str = "Label",
        textColor: str | Tuple[str, str] = Color.TEXT,
        height: int = 50,
        fontFamily: str = "Arial",
        fontSize: int = 12,
        fontWeight: Literal["normal", "bold"] = "normal",
        image: imagesTupple | str | None = None,
        imageSize: tuple = (20, 20),
        *args,
        **kwargs,
    ) -> None:
        self.master = master
        self.text = text
        self.height = height
        self.fontFamily = fontFamily
        self.fontSize = fontSize
        self.fontWeight = fontWeight
        self.image = image
        self.imageSize = imageSize

        argsDict = {
            "master": self.master,
            "text": self.text,
            "height": self.height,
            "font": CTkFont(family=self.fontFamily, size=self.fontSize, weight=self.fontWeight),
            "text_color": textColor,
        }

        self._image = Image(image=self.image, size=imageSize)
        if self._image.status == "ok":
            argsDict["image"] = self._image

        super().__init__(
            *args,
            **argsDict,
            **kwargs,
        )
