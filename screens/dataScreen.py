from typing import cast

from customtkinter import CTkBaseClass, CTkFrame

from components import Loader, Table
from config.settings import Color
from services.creditCardService import CreditCardService
from utils import dataToTable


class DataScreen(CTkFrame):
    def __init__(self, master: CTkBaseClass, creditCardService: CreditCardService) -> None:
        self.master = master
        self.creditCardService = creditCardService

        super().__init__(
            self.master,
            width=self.master._current_width,
            height=self.master._current_height,
            fg_color=Color.TRANSPARENT,
            corner_radius=0,
        )

        self.data = cast(list, self.master.data).copy()

        if not self.data:
            loader = Loader(self)
            loader.show()
            return

        colums, rows = dataToTable(self.data)

        self.table = Table(self, colums=colums, rows=rows)
        self.table.pack(expand=True, fill="both", padx=10, pady=10)
