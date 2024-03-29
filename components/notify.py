from customtkinter import CTkBaseClass, CTkFrame

from components.ui import Label
from config.settings import Color


class Notify(CTkFrame):
    def __init__(
        self,
        master: CTkBaseClass,
        text: str,
        fg_color: str = Color.GREEN,
    ) -> None:
        self.master = master

        super().__init__(self.master, width=200, height=40, fg_color=fg_color)

        self.label = Label(
            self,
            text=text,
            fontSize=13,
            fontWeight="bold",
            height=24,
        )
        self.label.place(relx=0.5, rely=0.5, anchor="center")

        self.XBtn = Label(
            self,
            text=" X ",
            fontWeight="bold",
            height=24,
        )
        self.XBtn.place(relx=0.9, rely=0.5, anchor="center")

        self.XBtn.bind("<Button-1>", lambda event: self.hide())

        for i in [self.XBtn]:
            i.bind("<Enter>", lambda event: self.XBtn.configure(cursor="hand2"))
            i.bind("<Leave>", lambda event: self.XBtn.configure(cursor=""))

    def show(self, text: str | None = None) -> None:
        if text:
            self.label.configure(text=text)
        self.place(relx=0.9, rely=0.93, anchor="center")
        # self.after(5000, self.hide)

    def hide(self) -> None:
        self.place_forget()
