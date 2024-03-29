from customtkinter import CTkBaseClass, CTkFrame

from components import AnimatedGif
from components.ui.label import Label
from config.settings import AssetsImages, Color


class Loader(CTkFrame):
    def __init__(self, master: CTkBaseClass, text: str = "Loading...", fg_color: str = Color.TRANSPARENT) -> None:
        self.master = master

        super().__init__(self.master, fg_color=fg_color)

        self.loader = AnimatedGif(
            self,
            gif_file=AssetsImages.LOADING_GIF,
            delay=0.02,
            bg=Color.BG_CONTENT[0] if self._get_appearance_mode() == "Dark" else Color.BG_CONTENT[1],
        )
        self.loader.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")
        # self.loader.pack(expand=True, padx=10, pady=10)

        if text:
            self.loader.place(relx=0.5, rely=0.45, anchor="center")
            self.label = Label(self, text=text, fontSize=16, textColor=Color.TEXT_GRAY, height=20)
            self.label.place(relx=0.5, rely=0.6, anchor="center")
        else:
            self.loader.pack(expand=True, padx=10, pady=10)

    def show(self) -> None:
        self.loader.start_thread()
        self.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")

    def hide(self) -> None:
        # self.loader.stop_thread()
        self.place_forget()
        self.destroy()
