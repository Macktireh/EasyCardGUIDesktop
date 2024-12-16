from collections.abc import Callable
from tkinter import NORMAL, StringVar
from typing import Any

from customtkinter import CTkBaseClass, CTkEntry, CTkFont

from config.settings import Color


class Input(CTkEntry):
    def __init__(
        self,
        master: CTkBaseClass,
        width: int = 140,
        height: int = 28,
        corner_radius: int | None = None,
        border_width: int | None = None,
        bg_color: str | tuple[str, str] = Color.TRANSPARENT,
        fg_color: str | tuple[str, str] | None = None,
        border_color: str | tuple[str, str] | None = None,
        text_color: str | tuple[str, str] | None = None,
        placeholder_text_color: str | tuple[str, str] | None = None,
        # textvariable: Union[Variable, None] = None,
        placeholder_text: str | None = None,
        font: tuple | CTkFont | None = None,
        state: str = NORMAL,
        defaultValue: str | None = "",
        on_change_callback: Callable[[StringVar], Any] | None = None,
        **kwargs,
    ) -> None:
        self.on_change_callback = on_change_callback

        self.var = StringVar()
        self.var.trace_add("write", self.onChange)

        super().__init__(
            master=master,
            # width=width,
            height=height,
            corner_radius=corner_radius,
            border_width=border_width,
            bg_color=bg_color,
            fg_color=fg_color,
            border_color=border_color,
            text_color=text_color,
            placeholder_text_color=placeholder_text_color,
            textvariable=self.var,
            placeholder_text=placeholder_text,
            font=font,
            state=state,
            **kwargs,
        )
        self.var.set(defaultValue)

    def getValue(self) -> str:
        return self.var.get()

    def setValue(self, value: str) -> None:
        self.var.set(value)

    def clear(self) -> None:
        self.var.set("")
        self.update()

    def setState(self, state: str) -> None:
        self.configure(state=state)

    def setPassword(self, value: bool) -> None:
        if value:
            self.configure(show="●")
        else:
            self.configure(show="")

    def onChange(self, *args: tuple[Any, ...]) -> None:
        if self.on_change_callback is not None:
            self.on_change_callback(self.var)
            return
