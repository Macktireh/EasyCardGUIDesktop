from customtkinter import CTkBaseClass, CTkFrame

from components.ui import Label
from config.settings import AssetsImages, Color, imagesTupple


class Notify(CTkFrame):
    CROSS_IMAGE = imagesTupple(
        light=AssetsImages.CROSS_DARK,
        dark=AssetsImages.CROSS_DARK,
    )

    def __init__(
        self,
        master: CTkBaseClass,
        text: str = "Notification successfully",
        fg_color: str = Color.GREEN,
    ) -> None:
        self.master = master

        super().__init__(self.master, width=210, height=40, fg_color=fg_color)

        self.label = Label(
            self,
            text=text,
            textColor=Color.WHITE,
            fontSize=13,
            fontWeight="bold",
            height=24,
            compound="left",
        )
        self.label.place(relx=0.01, rely=0.05, relwidth=0.85, relheight=0.9)

        self.XBtn = Label(
            self,
            text="",
            image=self.CROSS_IMAGE,
            imageSize=(15, 15),
            fontWeight="bold",
            width=20,
        )
        self.XBtn.place(relx=0.88, rely=0.05, relheight=0.9)

        self.XBtn.bind("<Button-1>", lambda event: self.hide())

        for i in [self.XBtn]:
            i.bind("<Enter>", lambda event: self.XBtn.configure(cursor="hand2"))
            i.bind("<Leave>", lambda event: self.XBtn.configure(cursor=""))

    def show(self, text: str | None = None, fg_color: str | None = None) -> None:
        if text:
            self.label.configure(text=text)
        if fg_color:
            self.configure(fg_color=fg_color)

        self.relx = 1.2
        self._min_relx = self.get_min_relx()
        self.animateShow(self._min_relx)

    def get_min_relx(self) -> float:
        _space = self.master._current_width - 225
        _min_relx = _space / self.master._current_width
        return _min_relx

    def hide(self) -> None:
        # self.relx = 0.8
        self.animateHide()

    def animateShow(self, min_relx: float) -> None:
        if self.relx > min_relx:
            self.relx -= 0.01
            self.place(relx=self.relx, rely=0.03)
            self.after(5, lambda: self.animateShow(min_relx))
        else:
            self.after(5000, self.hide)

    def animateHide(self) -> None:
        if self.relx < 1.2:
            self.relx += 0.01
            self.place(relx=self.relx, rely=0.03)
            self.after(5, self.animateHide)
