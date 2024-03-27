from typing import cast

from customtkinter import CTkBaseClass, CTkFrame

from components.animatedGif import AnimatedGif
from components.table import Table
from config.settings import AssetsImages, Color
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
            fg_color="transparent",
            corner_radius=0,
        )

        self.loader = AnimatedGif(self, gif_file=AssetsImages.LOADING_GIF, bg=Color.BG_CONTENT[1])

        colums = ["Day", "Week", "Month", "Year", "Hour", "Minute", "Second", "Weekday", "DayOfYear", "Daylight Saving"]
        rows = [
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20"],
            ["21", "22", "23", "24", "25", "26", "27", "28", "29", "30"],
        ]

        self.data = cast(list, self.master.data).copy()

        if not self.data:
            self.loader.pack(expand=True, padx=10, pady=10)
            self.loader.start_thread()
            return
        
        colums, rows = dataToTable(self.data)

        self.table = Table(self, colums=colums, rows=rows)
        self.table.pack(expand=True, fill="both", padx=10, pady=10)
        
