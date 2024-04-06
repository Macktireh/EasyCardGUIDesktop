from datetime import datetime
from typing import cast

from customtkinter import CTkBaseClass, CTkFrame

from components import AnimatedGif, BarChart, Card, PieChart
from components.ui import Label
from config.settings import AssetsImages, Color
from services.chartService import ChartService
from utils import getCardsCreatedWeekAgo


class DashboardScreen(CTkFrame):
    def __init__(self, master: CTkBaseClass, chartService: ChartService) -> None:
        self.master = master
        self.chartService = chartService
        self.currentTheme = self.master._get_appearance_mode()

        super().__init__(
            self.master,
            width=self.master._current_width,
            height=self.master._current_height,
            fg_color=Color.TRANSPARENT,
            corner_radius=0,
        )

        self.loader = AnimatedGif(self, gif_file=AssetsImages.LOADING_GIF, bg=Color.BG_CONTENT[1])

        self.data = cast(list, self.master.data).copy()

        if not self.data:
            self.loader.pack(expand=True, padx=10, pady=10)
            self.loader.start_thread()
            return

        Label(self, text="General Statistics", fontSize=26, fontWeight="bold").pack(pady=10)

        self.container = CTkFrame(self, fg_color=Color.TRANSPARENT)
        self.container.pack(fill="both", expand=True)

        _numCard = len(self.master.data)
        _numCardValid = len([card for card in self.master.data if card["isValid"]])
        _numCardInvalid = len([card for card in self.master.data if not card["isValid"]])
        _numNewCard = len(
            [
                card
                for card in self.master.data
                if card["createdAt"].split("T")[0] == datetime.now().strftime("%Y-%m-%d")
            ]
        )

        # Cards
        self.cardFrame = CTkFrame(self.container, fg_color=Color.TRANSPARENT, width=700)
        self.numCard = Card(self.cardFrame, text="Total cards", value=_numCard)
        self.numberRegisteredCard = Card(self.cardFrame, text="Valid cards", value=_numCardValid)
        self.numberRegisteredCard2 = Card(self.cardFrame, text="Invalid cards", value=_numCardInvalid)
        self.numberRegisteredCard3 = Card(self.cardFrame, text="New cards", value=_numNewCard)

        self.cardFrame.place(relx=0.005, rely=0.015, anchor="nw", relwidth=0.99, relheight=0.315)
        # self.numCard.pack(padx=5, pady=2, side="left", anchor="w", fill="both", expand=True)
        # self.numberRegisteredCard.pack(padx=5, pady=2, side="left", anchor="w", fill="both", expand=True)
        # self.numberRegisteredCard2.pack(padx=5, pady=2, side="left", anchor="w", fill="both", expand=True)
        # self.numberRegisteredCard3.pack(padx=5, pady=2, side="left", anchor="w", fill="both", expand=True)
        self.numCard.place(relx=0.005, rely=0.005, anchor="nw", relwidth=0.24, relheight=0.67)
        self.numberRegisteredCard.place(relx=0.255, rely=0.005, anchor="nw", relwidth=0.24, relheight=0.67)
        self.numberRegisteredCard2.place(relx=0.505, rely=0.005, anchor="nw", relwidth=0.24, relheight=0.67)
        self.numberRegisteredCard3.place(relx=0.755, rely=0.005, anchor="nw", relwidth=0.24, relheight=0.67)

        # Chart
        self.chartFrame = CTkFrame(master=self.container, fg_color=Color.TRANSPARENT)
        self.pieFrame = CTkFrame(master=self.chartFrame, fg_color=Color.BG_CARD)
        self.barFrame = CTkFrame(master=self.chartFrame, fg_color=Color.BG_CARD)

        self.chartFrame.place(relx=0.005, rely=0.24, anchor="nw", relwidth=0.99, relheight=0.74)
        self.pieFrame.place(relx=0.005, rely=0.005, anchor="nw", relwidth=0.49, relheight=0.99)
        self.barFrame.place(relx=0.505, rely=0.005, anchor="nw", relwidth=0.49, relheight=0.99)

        self.renderChart()

    def renderChart(self) -> None:
        # x_values = ["A", "B", "C", "D", "E"]
        # y_values_bar = [100, 200, 600, 400, 500]
        # y_values_donut = [10, 40, 30, 20, 50]
        pieData = [
            {"label": "500 fdj", "value": len([card for card in self.master.data if card["cardType"] == "500"])},
            {"label": "1000 fdj", "value": len([card for card in self.master.data if card["cardType"] == "1000"])},
            {"label": "2000 fdj", "value": len([card for card in self.master.data if card["cardType"] == "2000"])},
            {"label": "5000 fdj", "value": len([card for card in self.master.data if card["cardType"] == "5000"])},
            {"label": "10000 fdj", "value": len([card for card in self.master.data if card["cardType"] == "10000"])},
        ]
        dates, values = getCardsCreatedWeekAgo(self.master.data)
        self.pie = PieChart(
            master=self.pieFrame,
            chartService=self.chartService,
            y=list(map(lambda x: x["value"], pieData)),
            labels=list(map(lambda x: x["label"], pieData)),
            title="Percentage of cards by type",
            labelColor=Color.WHITE if self.currentTheme == "dark" else Color.BLACK,
            percentColor=Color.BLACK if self.currentTheme == "dark" else Color.WHITE,
            listColors=Color.LIST_BG_PIE[0] if self.currentTheme == "dark" else Color.LIST_BG_PIE[0],
        )
        self.bar = BarChart(
            master=self.barFrame,
            chartService=self.chartService,
            x=dates,
            y=values,
            title="Number of cards created this week",
            labelColor=(Color.WHITE, Color.WHITE) if self.currentTheme == "dark" else (Color.BLACK, Color.BLACK),
            barColor=Color.BG_ACTIVE_BUTTON_NAVIGATION[1]
            if self.currentTheme == "dark"
            else Color.BG_ACTIVE_BUTTON_NAVIGATION[0],
        )
        self.pie.pack(fill="both", expand=True, padx=5, pady=5)
        self.bar.pack(fill="both", expand=True, padx=5, pady=5)

    def updateCanvas(self) -> None:
        self.pie.updateThemeCanvas()
        self.bar.updateThemeCanvas()
        _currentTheme = self._get_appearance_mode()
        if self.currentTheme != _currentTheme:
            self.pie.destroy()
            self.bar.destroy()
            self.currentTheme = _currentTheme
            self.renderChart()
