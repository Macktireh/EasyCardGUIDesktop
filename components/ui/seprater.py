from customtkinter import CTkBaseClass, CTkFrame


class Seprater(CTkFrame):
    def __init__(self, master: CTkBaseClass, width: int = 10, height: int = 10) -> None:
        super().__init__(master, width=width, height=height, fg_color="transparent")
