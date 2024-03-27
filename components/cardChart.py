from numbers import Number

from CTkToolTip import CTkToolTip
from customtkinter import CTkBaseClass, CTkFrame

from components.ui import Label
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
            # width=self.width,
            # height=self.height,
            fg_color=Color.BG_CARD,
            corner_radius=10,
        )

        # Separator(self, width=15, height=15).pack()
        _value = Label(self, text=self.value, fontSize=32, fontWeight="bold")
        _value.place(relx=0.5, rely=0.38, anchor="center")
        # _value.pack(side="top", pady=(0, 15), expand=True)
        _text = Label(self, text=self.text, fontSize=14, fontWeight="bold", textColor=Color.TEXT_GRAY, height=20)
        _text.place(relx=0.5, rely=0.68, anchor="center")
        # _text.pack( side="top", pady=(0, 0), expand=True)
        # Separator(self, width=15, height=15).pack()

        CTkToolTip(self, delay=0.3, message=self.value)
        CTkToolTip(_value, delay=0.3, message=self.value)
        CTkToolTip(_text, delay=0.3, message=self.value)
