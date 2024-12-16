from abc import ABC, abstractmethod
from numbers import Number
from typing import Any

from matplotlib.figure import Figure


class ChartService(ABC):
    @abstractmethod
    def bar(
        self,
        x: tuple[Any, ...] | Any,
        y: tuple[Number, ...] | Number,
        barColor: str = "skyblue",
        labelColor: tuple[str, str] = ("black", "black"),
        x_label: str = "X-axis",
        y_label: str = "Y-axis",
    ) -> Figure: ...

    @abstractmethod
    def pie(
        self,
        y: tuple[Number, ...] | Number,
        labels: tuple[Any, ...] | Any,
        labelColor: str = "black",
        percentColor: str = "black",
        listColors: tuple[str, ...] | str | None = None,
        wedgeprops: dict = None,
    ) -> Figure: ...
