from customtkinter import CTkBaseClass

from components.ui import Label
from config.settings import Color


class Toast:
    def __init__(
        self,
        master: CTkBaseClass,
        text: str,
        fg_color: str = Color.ORANGE,
    ) -> None:
        self.master = master

        self.label = Label(
            self.master,
            text=text,
            fontSize=13,
            fontWeight="bold",
            fg_color=fg_color,
            height=24,
            corner_radius=4,
        )

    def show(self, before: CTkBaseClass | None = None, after: CTkBaseClass | None = None) -> None:
        if before:
            self.label.pack(fill="x", pady=(1, 0), padx=1, before=before)
        elif after:
            self.label.pack(fill="x", pady=(1, 0), padx=1, after=after)
        else:
            self.label.pack(fill="x", pady=(1, 0), padx=1)

    def hide(self) -> None:
        self.label.pack_forget()
