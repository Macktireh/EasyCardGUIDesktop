from customtkinter import CTkBaseClass, CTkFrame

from components.ui import Button, Label
from config.settings import ScreenName


class NewCardScreen(CTkFrame):
    def __init__(self, master: CTkBaseClass) -> None:
        self.master = master

        super().__init__(
            self.master,
            width=self.master._current_width,
            height=self.master._current_height,
            fg_color="transparent",
            corner_radius=0,
        )

        self.label = Label(self, text="New Card")
        self.label.pack()

        self.button = Button(self, text="Button")
        self.button = Button(self, text="Button", command=lambda: self.master.navigate(ScreenName.DASHBOARD))
        self.button.pack()
