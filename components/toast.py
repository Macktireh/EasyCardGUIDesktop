import contextlib
from tkinter import TclError

from customtkinter import CTkBaseClass

from components.ui import Label
from config.settings import Color


class Toast(Label):
    def __init__(
        self,
        master: CTkBaseClass,
        text: str,
        fg_color: str = Color.ORANGE,
    ) -> None:
        self.master = master

        super().__init__(
            self.master,
            text=text,
            fontSize=13,
            fontWeight="bold",
            fg_color=fg_color,
            height=24,
            corner_radius=4,
        )

    def show(
        self,
        text: str | None = None,
        fg_color: str | None = None,
        before: CTkBaseClass | None = None,
        after: CTkBaseClass | None = None,
    ) -> None:
        if text:
            self.configure(text=text)
        if fg_color:
            self.configure(fg_color=fg_color)
        if before:
            self.pack(fill="x", pady=(1, 0), padx=1, before=before)
        elif after:
            self.pack(fill="x", pady=(1, 0), padx=1, after=after)
        else:
            self.pack(fill="x", pady=(1, 0), padx=1)

    def hide(self) -> None:
        with contextlib.suppress(Exception, TclError):
            self.pack_forget()
