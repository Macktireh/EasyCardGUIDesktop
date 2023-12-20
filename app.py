from customtkinter import CTk, StringVar

from components import Navigation
from config.settings import ScreenName
from screens import ScreenManager


class App(CTk):
    width: int = 1200
    height: int = 700

    def __init__(self) -> None:
        super().__init__()
        self.title("EasyCreditCard")
        self.resizable(False, False)
        self.centerWindow()

        self.currentScreen = StringVar(self, value=ScreenName.DASHBOARD)

        self.navigation = Navigation(self, width=200, height=self._current_height)
        self.navigation.pack(side="left", fill="y")

        self.screenManager = ScreenManager(
            self,
            width=self._current_width - self.navigation.width,
            height=self._current_height,
        )
        self.screenManager.pack(side="right", fill="both", expand=True)

    def run(self) -> None:
        """Run the application."""
        self.mainloop()

    def centerWindow(self) -> None:
        """Center the application window on the screen."""
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (self.width // 2)
        y = (self.winfo_screenheight() // 2) - (self.height // 2)
        self.geometry(f"{self.width}x{self.height}+{x}+{y}")

    def setTitle(self, title: str) -> None:
        """
        Set the title of the application window.

        Args:
            title (str): The title to be set.
        """
        self.title(f"EasyCreditCard - {title}")
