from typing import Tuple

from customtkinter import CTkBaseClass, CTkScrollableFrame

from components.ui import Separator
from components.updateCardRow import UpdateCardRow
from config.settings import AssetsImages, Color, imagesTupple


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

    def __init__(
        self,
        master: CTkBaseClass,
        width: int = 690,
        height: int = 300,
        fg_color: str | Tuple[str, str] | None = Color.BG_CARD,
        **kwargs,
    ) -> None:
        super().__init__(master=master, width=width, height=height, fg_color=fg_color, **kwargs)

        for _ in range(5):
            UpdateCardRow(self, width=width * 0.9).pack(padx=10, pady=8)

        self.render()

    def render(self) -> None:
        ...
