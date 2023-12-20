from numbers import Number
from typing import Any, Dict, Tuple

from customtkinter import CTkBaseClass, CTkFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from components.ui import Label
from config.settings import Color
from services.chartService import ChartService


class PieChart(CTkFrame):
    def __init__(
        self,
        master: CTkBaseClass,
        chartService: ChartService,
        y: Tuple[Number, ...] | Number,
        labels: Tuple[Any, ...] | Any,
        title: str = "Pie Chart",
        titleColor: str = "black",
        labelColor: str = "black",
        percentColor: str = "black",
        listColors: Tuple[str, ...] | str | None = None,
        wedgeprops: Dict | None = None,
        **kwargs,
    ) -> None:
        self.master = master
        self.chartService = chartService
        self.y = y
        self.labels = labels
        self.title = title
        self.titleColor = titleColor
        self.labelColor = labelColor
        self.percentColor = percentColor
        self.listColors = listColors
        self.wedgeprops = wedgeprops
        self.currentTheme = self.master._get_appearance_mode()

        super().__init__(
            self.master,
            fg_color=Color.BG_CARD,
            corner_radius=10,
            **kwargs,
        )

        # Seprater(self, width=15, height=15).pack()
        Label(self, text=self.title, fontSize=16, fontWeight="bold").pack(pady=5)

        self.showChart()

    def showChart(self) -> None:
        fig = self.chartService.pie(
            y=self.y,
            labels=self.labels,
            labelColor=self.labelColor,
            percentColor=self.percentColor,
            listColors=self.listColors,
            wedgeprops=self.wedgeprops,
        )
        self.canvas = FigureCanvasTkAgg(fig, master=self).get_tk_widget()
        self.canvas.pack(fill="both", expand=True)

    def updateCanvas(self) -> None:
        _currentTheme = self._get_appearance_mode()
        if self.currentTheme != _currentTheme:
            self.canvas.destroy()
            self.showChart()
            self.currentTheme = _currentTheme
