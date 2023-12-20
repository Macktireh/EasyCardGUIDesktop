from numbers import Number

from customtkinter import CTkBaseClass, CTkFrame

from components.ui import Label, Seprater
from config.settings import Color

# from config.settings import Images


class Card(CTkFrame):
    def __init__(
        self,
        master: CTkBaseClass,
        text: str = "Card",
        value: Number = 150,
        width: int = 150,
        height: int = 80,
        **kwargs,
    ) -> None:
        self.master = master
        self.text = text
        self.value = value
        self.width = width
        self.height = height

        super().__init__(
            self.master,
            width=self.width,
            height=self.height,
            fg_color=Color.BG_CARD,
            corner_radius=10,
        )

        # Label(self, text="", image=Images.LOGO, imageSize=(40, 40)).pack()
        Seprater(self, width=15, height=15).pack()
        Label(self, text=self.value, fontSize=40, fontWeight="bold").pack()
        Label(self, text=self.text, fontSize=14, fontWeight="bold").pack()
        Seprater(self, width=15, height=15).pack()
