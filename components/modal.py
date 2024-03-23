
from customtkinter import CTkBaseClass, CTkFrame

from components.ui import Button, Label
from config.settings import Color


class Modal(CTkFrame):
    def __init__(
        self,
        master: CTkBaseClass,
        text: str,
        fg_color: str = Color.BG_BUTON_DND,
    ) -> None:
        self.master = master

        super().__init__(self.master, fg_color=fg_color)

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
            command=lambda: self.hideModal(),
        )
        self.cancelButton.place(relx=0.53, rely=0.8)

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
        self.reloadButton.place(relx=0.75, rely=0.8)

    def showModal(self) -> None:
        self.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.3, anchor="center")

    def hideModal(self) -> None:
        self.place_forget()
    
    def reload(self) -> None:
        self.master.reload()
