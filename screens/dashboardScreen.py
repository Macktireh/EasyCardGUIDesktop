from customtkinter import CTkBaseClass, CTkFrame

from components import BarChart, Card, PieChart
from components.ui import Label
from config.settings import Color
from services.chartService import ChartService


class DashboardScreen(CTkFrame):
    def __init__(self, master: CTkBaseClass, chartService: ChartService) -> None:
        self.master = master
        self.chartService = chartService
        self.currentTheme = self.master._get_appearance_mode()

        super().__init__(
            self.master,
            width=self.master._current_width,
            height=self.master._current_height,
            fg_color="transparent",
            corner_radius=0,
        )

        self.label = Label(self, text="General Statistics", fontSize=26, fontWeight="bold").pack(pady=10)

        self.container = CTkFrame(self, fg_color="transparent")
        self.container.pack(fill="both", expand=True)

        # Cards
        self.cardFrame = CTkFrame(self.container, fg_color="transparent", width=700)
        self.numCard = Card(self.cardFrame, width=180, height=80)
        self.numberRegisteredCard = Card(self.cardFrame, width=180, height=80)
        self.numberRegisteredCard2 = Card(self.cardFrame, width=180, height=80)
        self.numberRegisteredCard3 = Card(self.cardFrame, width=180, height=80)

        self.cardFrame.place(relx=0.005, rely=0.015, anchor="nw", relwidth=0.99)
        self.numCard.pack(padx=5, pady=2, side="left", anchor="w", fill="both", expand=True)
        self.numberRegisteredCard.pack(padx=5, pady=2, side="left", anchor="w", fill="both", expand=True)
        self.numberRegisteredCard2.pack(padx=5, pady=2, side="left", anchor="w", fill="both", expand=True)
        self.numberRegisteredCard3.pack(padx=5, pady=2, side="left", anchor="w", fill="both", expand=True)

        # Chart
        self.chartFrame = CTkFrame(master=self.container, fg_color="transparent", width=700, height=400)
        self.pieFrame = CTkFrame(master=self.chartFrame, fg_color=Color.BG_CARD)
        self.barFrame = CTkFrame(master=self.chartFrame, fg_color=Color.BG_CARD)

        self.chartFrame.place(relx=0.005, rely=0.24, anchor="nw", relwidth=0.99, relheight=0.74)
        self.pieFrame.place(relx=0.005, rely=0.005, anchor="nw", relwidth=0.49, relheight=0.99)
        self.barFrame.place(relx=0.505, rely=0.005, anchor="nw", relwidth=0.49, relheight=0.99)

        self.showChart()

    def showChart(self) -> None:
        x_values = ["A", "B", "C", "D", "E"]
        y_values_bar = [100, 200, 600, 400, 500]
        y_values_donut = [10, 40, 30, 20, 50]
        self.pie = PieChart(
            master=self.pieFrame,
            chartService=self.chartService,
            y=y_values_donut,
            labels=x_values,
            labelColor=Color.WHITE if self.currentTheme == "dark" else Color.BLACK,
            percentColor=Color.BLACK if self.currentTheme == "dark" else Color.WHITE,
            listColors=Color.LIST_BG_PIE[0] if self.currentTheme == "dark" else Color.LIST_BG_PIE[0],
        )
        self.bar = BarChart(
            master=self.barFrame,
            chartService=self.chartService,
            x=x_values,
            y=y_values_bar,
            labelColor=(Color.WHITE, Color.WHITE) if self.currentTheme == "dark" else (Color.BLACK, Color.BLACK),
            barColor=Color.BG_ACTIVE_BUTTON__NAVIGATION[1]
            if self.currentTheme == "dark"
            else Color.BG_ACTIVE_BUTTON__NAVIGATION[0],
        )
        self.pie.pack(fill="both", expand=True, padx=5, pady=5)
        self.bar.pack(fill="both", expand=True, padx=5, pady=5)

    def updateCanvas(self) -> None:
        self.pie.updateCanvas()
        self.bar.updateCanvas()
        _currentTheme = self._get_appearance_mode()
        if self.currentTheme != _currentTheme:
            self.pie.destroy()
            self.bar.destroy()
            self.currentTheme = _currentTheme
            self.showChart()
