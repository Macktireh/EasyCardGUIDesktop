import contextlib
from tkinter import TclError

from customtkinter import CTkBaseClass, CTkFrame

from components.ui import Button, Label
from config.settings import Color


class Modal(CTkFrame):
    def __init__(
        self,
        master: CTkBaseClass,
        text: str = "Modal",
        fg_color: str = Color.BG_BUTON_DND,
    ) -> None:
        self.master = master

        super().__init__(self.master, width=380, height=160, fg_color=fg_color)

        self.label = Label(
            self,
            text=text,
            fontSize=13,
            fontWeight="bold",
            # fg_color=fg_color,
            height=24,
            corner_radius=4,
        )
        self.label.place(relx=0.5, rely=0.4, anchor="center")

        self.cancelButton = Button(
            self,
            text="Cancel",
            width=80,
            height=30,
            fg_color=Color.BG_BUTTON_NAVIGATION,
            hover_color=Color.BG_HOVER_BUTTON_NAVIGATION,
            command=lambda: self.hide(),
        )
        self.cancelButton.place(relx=0.53, rely=0.75)

        self.reloadButton = Button(
            self,
            text="Reload",
            width=80,
            height=30,
            textColor=Color.WHITE,
            fg_color=Color.BG_ACTIVE_BUTTON_NAVIGATION,
            hover_color=Color.BG_HOVER_BUTTON_NAVIGATION,
            command=lambda: self.reload(),
        )
        self.reloadButton.place(relx=0.75, rely=0.75)

    def show(self, text: str | None = None) -> None:
        if text:
            self.label.configure(text=text)

        self.place(relx=0.5, rely=0.5, anchor="center")

    def hide(self) -> None:
        with contextlib.suppress(Exception, TclError):
            self.place_forget()

    def reload(self) -> None:
        self.master.reload()
