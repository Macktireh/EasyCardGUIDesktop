from typing import List, Tuple

from customtkinter import CTkBaseClass, CTkScrollableFrame

from components.updateCardRow import UpdateCardRow
from config.settings import AssetsImages, Color, imagesTupple
from models.types import CreditCardDictIn


class AddCardForm(CTkScrollableFrame):
    DELETE_IMAGE = imagesTupple(
        light=AssetsImages.DELETE_LIGHT,
        dark=AssetsImages.DELETE_DARK,
    )
    EXTRACT_IMAGE = imagesTupple(
        light=AssetsImages.EXTRACT_LIGHT,
        dark=AssetsImages.EXTRACT_DARK,
    )
    CROSS_IMAGE = imagesTupple(
        light=AssetsImages.CROSS_DARK,
        dark=AssetsImages.CROSS_DARK,
    )
    LIST_ROW_WIDGET_NAMES = []

    def __init__(
        self,
        master: CTkBaseClass,
        width: int = 690,
        height: int = 250,
        fg_color: str | Tuple[str, str] | None = Color.BG_CARD,
        **kwargs,
    ) -> None:
        super().__init__(master=master, width=width, height=height, fg_color=fg_color, **kwargs)
        self.master = master
        self.width = width

    def _render(self, cardNumbers: List[str]) -> None:
        _LIST_ROW_WIDGET_NAMES = []
        for i, code in enumerate(cardNumbers):
            u = UpdateCardRow(master=self, _id=i + 1, code=code, width=self.width * 0.9)
            u.pack(padx=10, pady=8)
            _LIST_ROW_WIDGET_NAMES.append(u.winfo_name())
        return _LIST_ROW_WIDGET_NAMES

    def render(self, cardNumbers: List[str]) -> None:
        self.LIST_ROW_WIDGET_NAMES = self._render(cardNumbers)

    def add(self, creditCardDictIn: CreditCardDictIn) -> None:
        u = UpdateCardRow(
            master=self,
            _id=len(self.LIST_ROW_WIDGET_NAMES) + 1,
            code=creditCardDictIn["code"],
            cardType=creditCardDictIn["cardType"],
        )
        u.pack(padx=10, pady=8)
        self.LIST_ROW_WIDGET_NAMES.append(u.winfo_name())

    def updateRender(self, cardNumbers: List[str]) -> None:
        for name in self.LIST_ROW_WIDGET_NAMES:
            self.nametowidget(name).destroy()

        self.LIST_ROW_WIDGET_NAMES = self._render(cardNumbers)

    def onDeleteForm(self, code: str, name) -> None:
        self.LIST_ROW_WIDGET_NAMES = [x for x in self.LIST_ROW_WIDGET_NAMES if x != name]
        self.master.onDelete(code)
