from tkinter import Label, PhotoImage, Tk
from typing import Any

from config.settings import IMAGES_DIR, Color


class SplashScreen(Tk):
    width: int = 400
    height: int = 200

    def __init__(self, app: Tk) -> None:
        super().__init__()
        self.app = app
        self.overrideredirect(True)
        self.update_idletasks()

        frm_width = self.winfo_rootx() - self.winfo_x()
        win_width = self.width + 2 * frm_width

        titlebar_height = self.winfo_rooty() - self.winfo_y()
        win_height = self.height + titlebar_height + frm_width

        x = self.winfo_screenwidth() // 2 - win_width // 2
        y = self.winfo_screenheight() // 2 - win_height // 2

        self.geometry(f"{self.width}x{self.height}+{x}+{y}")
        self.config(background=Color.BG_SPLASH)
        self.deiconify()

        self.BtnExit = Label(self, text="  X  ", font=("Arial", 13), background=Color.BG_SPLASH, fg="black", bd=1)
        self.BtnExit.place(relx=0.913, rely=0.001)
        self.BtnExit.bind("<Button-1>", self.exit)

        self.splach_logo = PhotoImage(file=f"{IMAGES_DIR}/logo.png")
        self.splach_logo = self.splach_logo.subsample(7, 7)

        self.label_show_splach_logo = Label(
            self, image=self.splach_logo, background=Color.BG_SPLASH, width=150, height=150
        ).place(relx=0.32, rely=0.04)

        self.splach_label = Label(
            self, text="Easy Credit Card", background=Color.BG_SPLASH, font=("Helvetica", 14)
        ).place(relx=0.32, rely=0.7)

        for b in [self.BtnExit]:
            b.bind("<Enter>", self.changeBgColor)
            b.bind("<Leave>", self.changeFgColor)

    def exit(self, e: Any) -> None:
        self.quit()

    def changeBgColor(self, e: Any) -> None:
        self.BtnExit.config(background=Color.RED, fg=Color.WHITE, cursor="hand2")

    def changeFgColor(self, e) -> None:
        self.BtnExit.config(background=Color.BG_SPLASH, fg=Color.BLACK)

    def run(self) -> None:
        self.after(1000, self.startApp)
        self.mainloop()

    def startApp(self) -> None:
        self.destroy()
        self.app().run()
