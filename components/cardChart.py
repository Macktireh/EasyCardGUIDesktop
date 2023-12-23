from numbers import Number

from CTkToolTip import CTkToolTip
from customtkinter import CTkBaseClass, CTkFrame

from components.ui import Label, Separator
from config.settings import Color


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

        Separator(self, width=15, height=15).pack()
        _value = Label(self, text=self.value, fontSize=40, fontWeight="bold")
        _value.pack()
        _text = Label(self, text=self.text, fontSize=14, fontWeight="bold")
        _text.pack()
        Separator(self, width=15, height=15).pack()

        CTkToolTip(self, delay=0.3, message=self.value)
        CTkToolTip(_value, delay=0.3, message=self.value)
        CTkToolTip(_text, delay=0.3, message=self.value)
