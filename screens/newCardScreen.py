from customtkinter import CTkBaseClass, CTkFrame, CTkLabel


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

        self.label = CTkLabel(self, text="New Card")
        self.label.pack()
