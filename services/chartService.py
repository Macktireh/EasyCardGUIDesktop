from abc import ABC, abstractmethod
from numbers import Number
from typing import Any, Dict, Tuple

from matplotlib.figure import Figure


class ChartService(ABC):
    @abstractmethod
    def bar(
        self,
        x: Tuple[Any, ...] | Any,
        y: Tuple[Number, ...] | Number,
        barColor: str = "skyblue",
        labelColor: Tuple[str, str] = ("black", "black"),
    ) -> Figure: ...

    @abstractmethod
    def pie(
        self,
        y: Tuple[Number, ...] | Number,
        labels: Tuple[Any, ...] | Any,
        labelColor: str = "black",
        percentColor: str = "black",
        listColors: Tuple[str, ...] | str | None = None,
        wedgeprops: Dict = None,
    ) -> Figure: ...
