from typing import Tuple

from customtkinter import CTkBaseClass, CTkFrame, CTkOptionMenu, StringVar

from components.ui import Button, Input, Separator
from config.settings import LIST_CARD_TYPES, AssetsImages, Color, imagesTupple


class UpdateCardRow(CTkFrame):
    EDIT_IMAGE = imagesTupple(
        light=AssetsImages.EDIT_DARK,
        dark=AssetsImages.EDIT_DARK,
    )
    CROSS_IMAGE = imagesTupple(
        light=AssetsImages.CROSS_DARK,
        dark=AssetsImages.CROSS_DARK,
    )
    IS_EDITING = False
    NAME = "!!updatecardrow"

    def __init__(
        self,
        master: CTkBaseClass,
        _id: int,
        code: str,
        cardType: str = LIST_CARD_TYPES[0],
        width: int = 680,
        fg_color: str | Tuple[str, str] | None = Color.BG_CARD,
        **kwargs,
    ) -> None:
        super().__init__(master=master, width=width, fg_color=fg_color, **kwargs)
        self.master = master
        self._id = _id

        self.inputCode = Input(self, label=f"Code {_id}", defaultValue=code, width=200, entryBgColor=Color.BG_CONTENT)
        self.cardTypeVar = StringVar(self, value=cardType)
        self.cardTypeInput = CTkOptionMenu(
            self,
            values=LIST_CARD_TYPES,
            text_color=Color.TEXT,
            fg_color=Color.BG_CONTENT,
            button_color=Color.BG_ACTIVE_BUTTON_NAVIGATION,
            button_hover_color=Color.BG_HOVER_BUTTON_NAVIGATION,
            variable=self.cardTypeVar,
            command=lambda value: self.cardTypeVar.set(value),
        )
        # self.editButton = Button(
        #     self,
        #     text="",
        #     image=self.EDIT_IMAGE,
        #     width=30,
        #     height=30,
        #     imageSize = (18, 18),
        #     fg_color=Color.BG_ACTIVE_BUTTON_NAVIGATION,
        #     hover_color=Color.BG_HOVER_BUTTON_NAVIGATION,
        #     command=self.editCard,
        # )
        self.deleteButton = Button(
            self,
            text="",
            image=self.CROSS_IMAGE,
            width=30,
            height=30,
            imageSize=(18, 18),
            fg_color=Color.BG_ACTIVE_BUTTON_NAVIGATION,
            hover_color=Color.BG_HOVER_BUTTON_NAVIGATION,
            command=self.deleteCard,
        )

        self.render()

    def render(self) -> None:
        # self.pack(padx=10, pady=5)
        self.inputCode.grid(row=1, column=0)
        Separator(self, width=30).grid(row=1, column=1)
        self.cardTypeInput.grid(row=1, column=2)
        Separator(self, width=160).grid(row=1, column=3)
        # self.editButton.grid(row=1, column=4)
        # Separator(self, width=15).grid(row=1, column=5)
        self.deleteButton.grid(row=1, column=6)

    def editCard(self) -> None:
        if self.IS_EDITING:
            self.inputCode.setState("normal")
            self.inputCode.entry.configure(fg_color=Color.BG_CONTENT)
            self.IS_EDITING = False
        else:
            self.inputCode.setState("readonly")
            self.inputCode.entry.configure(fg_color=Color.BG_BUTON_DND)
            self.IS_EDITING = True

    def deleteCard(self) -> None:
        self.master.onDeleteForm(self.inputCode.getValue(), self.winfo_name())
        self.destroy()
