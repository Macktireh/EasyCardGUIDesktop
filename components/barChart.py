from numbers import Number
from typing import Any, Tuple

from customtkinter import CTkBaseClass, CTkFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from components.ui import Label
from config.settings import Color
from services.chartService import ChartService


class BarChart(CTkFrame):
    def __init__(
        self,
        master: CTkBaseClass,
        chartService: ChartService,
        x: Tuple[Any, ...] | Any,
        y: Tuple[Number, ...] | Number,
        title: str = "Bar Chart",
        titleColor: str = "black",
        barColor: str = "skyblue",
        labelColor: Tuple[str, str] = ("black", "black"),
        **kwargs,
    ) -> None:
        self.master = master
        self.chartService = chartService
        self.x = x
        self.y = y
        self.title = title
        self.titleColor = titleColor
        self.barColor = barColor
        self.labelColor = labelColor
        self.currentTheme = self.master._get_appearance_mode()

        super().__init__(
            self.master,
            fg_color=Color.BG_CARD,
            corner_radius=10,
            **kwargs,
        )

        Label(self, text=self.title, fontSize=16, fontWeight="bold").pack()

        self.showChart()

    def showChart(self) -> None:
        fig = self.chartService.bar(x=self.x, y=self.y, barColor=self.barColor, labelColor=self.labelColor)
        self.canvas = FigureCanvasTkAgg(fig, master=self).get_tk_widget()
        self.canvas.pack(fill="both", expand=True)

    def updateCanvas(self) -> None:
        _currentTheme = self._get_appearance_mode()
        if self.currentTheme != _currentTheme:
            self.canvas.destroy()
            self.showChart()
            self.currentTheme = _currentTheme
