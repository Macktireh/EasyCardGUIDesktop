from numbers import Number
from typing import Any, Dict, Tuple

from matplotlib.figure import Figure

from services.chartService import ChartService


class MatplotlibService(ChartService):
    def __init__(
        self,
        plt,
        axesFaceColor: str = "#2b2b31",
        figureFaceColor: str = "#2b2b31",
        savefigFaceColor: str = "#2b2b31",
        axesEdgecolor: str = "red",
        xTickColor: str = "green",
        yTickColor: str = "yellow",
    ) -> None:
        self.plt = plt
        # self.plt.style.use("grayscale")
        self.plt.rcParams["axes.facecolor"] = axesFaceColor
        self.plt.rcParams["figure.facecolor"] = figureFaceColor
        self.plt.rcParams["savefig.facecolor"] = savefigFaceColor
        self.plt.rcParams["axes.edgecolor"] = axesEdgecolor
        self.plt.rcParams["xtick.color"] = xTickColor
        self.plt.rcParams["ytick.color"] = yTickColor
        self.plt.rcParams["axes.prop_cycle"] = self.plt.cycler(
            color=["#545473", "#464667", "#3b3b54", "#2a2a3c", "#262631"]
        )

    def bar(
        self,
        x: Tuple[Any, ...] | Any,
        y: Tuple[Number, ...] | Number,
        barColor: str = "skyblue",
        labelColor: Tuple[str, str] = ("black", "black"),
    ) -> Figure:
        """
        Plots a bar chart with the given data.

        Args:
            x: (Tuple[Any, ...] | Any): The x-values for the bar chart.
            y: (Tuple[Number, ...] | Number): The y-values for the bar chart.
            barColor: (str, optional): The color of the bars. Defaults to "skyblue".
            labelColor: (Tuple[str, str], optional): The color of the axis labels. Defaults to ("black", "black").

        Returns:
            Figure: The generated bar chart figure.
        """
        fig, ax = self.plt.subplots()
        bars = ax.bar(x, y, color=barColor)
        ax.set_xlabel("X-axis", color=labelColor[0])
        ax.set_ylabel("Y-axis", color=labelColor[1])

        for bar in bars:
            yval = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                yval / 2,
                round(yval, 2),
                ha="center",
                va="center",
                color="white",
            )

        return fig

    def pie(
        self,
        y: Tuple[Number, ...] | Number,
        labels: Tuple[Any, ...] | Any,
        labelColor: str = "black",
        percentColor: str = "black",
        listColors: Tuple[str, ...] | str | None = None,
        wedgeprops: Dict = None,
    ) -> Figure:
        """
        Generates a pie chart using the given data.

        Args:
            y: (Tuple[Number, ...] | Number): The data values for the pie chart.
            labels: (Tuple[Any, ...] | Any): The labels for each data value.
            labelColor: (str, optional): The color of the labels. Defaults to "black".
            percentColor: (str, optional): The color of the percentage values. Defaults to "black".
            listColors: (Tuple[str, ...] | str | None, optional): The colors for each wedge. 
                        If None, a default color palette will be used. Defaults to None.
            wedgeprops: (Dict, optional): Additional properties for the wedges. Defaults to None.

        Returns:
            Figure: The generated pie chart figure.
        """
        if wedgeprops is None:
            wedgeprops = dict(width=0.6, edgecolor="w")
        fig, ax = self.plt.subplots()

        colors = listColors or self.plt.cm.Set3.colors
        _, _labels, autopct = ax.pie(
            y,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90,
            wedgeprops=wedgeprops,
            colors=colors,
            textprops={"color": percentColor},
        )

        for label in _labels:
            label.set_color(labelColor)

        return fig
