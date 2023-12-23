from typing import Tuple

from customtkinter import CTkBaseClass, CTkFrame, CTkOptionMenu

from components.ui import Button, Input, Separator
from config.settings import AssetsImages, Color, imagesTupple


class UpdateCardRow(CTkFrame):
    EDIT_IMAGE = imagesTupple(
        light=AssetsImages.EDIT_DARK,
        dark=AssetsImages.EDIT_DARK,
    )
    CROSS_IMAGE = imagesTupple(
        light=AssetsImages.CROSS_DARK,
        dark=AssetsImages.CROSS_DARK,
    )

    def __init__(
        self, master: CTkBaseClass, width: int = 680, fg_color: str | Tuple[str, str] | None = Color.BG_CARD, **kwargs
    ) -> None:
        super().__init__(master=master, width=width, fg_color=fg_color, **kwargs)

        self.inputCode = Input(self, label="Code", width=200, entryBgColor=Color.BG_CONTENT, state="readonly")
        self.cardType = CTkOptionMenu(
            self,
            values=[
                "500 FDJ",
                "1000 FDJ",
                "2000 FDJ",
                "5000 FDJ",
                "10000 FDJ",
            ],
            text_color=Color.TEXT,
            fg_color=Color.BG_CONTENT,
            button_color=Color.BG_ACTIVE_BUTTON_NAVIGATION,
            button_hover_color=Color.BG_HOVER_BUTTON_NAVIGATION,
        )
        self.editButton = Button(
            self,
            text="",
            image=self.EDIT_IMAGE,
            width=30,
            height=30,
            imageSize = (18, 18),
            fg_color=Color.BG_ACTIVE_BUTTON_NAVIGATION,
            hover_color=Color.BG_HOVER_BUTTON_NAVIGATION,
        )
        self.deleteButton = Button(
            self,
            text="",
            image=self.CROSS_IMAGE,
            width=30,
            height=30,
            imageSize = (18, 18),
            fg_color=Color.BG_ACTIVE_BUTTON_NAVIGATION,
            hover_color=Color.BG_HOVER_BUTTON_NAVIGATION,
        )

        self.render()

    def render(self) -> None:
        # self.pack(padx=10, pady=5)
        self.inputCode.grid(row=1, column=0)
        Separator(self, width=30).grid(row=1, column=1)
        self.cardType.grid(row=1, column=2)
        Separator(self, width=120).grid(row=1, column=3)
        self.editButton.grid(row=1, column=4)
        Separator(self, width=15).grid(row=1, column=5)
        self.deleteButton.grid(row=1, column=6)

