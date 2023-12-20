from typing import Literal

from customtkinter import CTkBaseClass, CTkButton, CTkFont, CTkImage

from components.ui.image import Image, imagesTupple
from config.settings import Color


class Button(CTkButton):
    image: CTkImage | None = None

    def __init__(
        self,
        master: CTkBaseClass,
        text: str = "Button",
        fontFamily: str = "Arial",
        fontSize: int = 13,
        fontWeight: Literal["normal", "bold"] = "bold",
        width: int = 300,
        height: int = 50,
        image: imagesTupple | str | None = None,
        imageSize: tuple = (20, 20),
        *args,
        **kwargs,
    ) -> None:
        self.master = master
        self.text = text
        self.width = width
        self.height = height
        self.fontFamily = fontFamily
        self.fontSize = fontSize
        self.fontWeight = fontWeight
        self.image = image
        self.imageSize = imageSize

        argsDict = {
            "master": self.master,
            "width": self.width,
            "height": self.height,
            "text": self.text,
            "font": CTkFont(family=self.fontFamily, size=self.fontSize, weight=self.fontWeight),
            "text_color": Color.TEXT,
        }

        self._image = Image(image=self.image, size=imageSize)
        if self._image.status == "ok":
            argsDict["image"] = self._image

        super().__init__(
            *args,
            **argsDict,
            **kwargs,
        )
