from customtkinter import CTk
from tkinterdnd2.TkinterDnD import DnDWrapper, _require

from components import Navigation
from config.settings import ScreenName
from screens import ScreenManager
from services.authServiceImpl import AuthServiceImpl


class App(CTk, DnDWrapper):
    width: int = 1200
    height: int = 700

    def __init__(self) -> None:
        super().__init__()
        self.TkdndVersion = _require(self)
        self.title("EasyCard")
        # self.resizable(True, False)
        self.minsize(800, 600)
        # self.maxsize(self.width + 200, self.height)
        self.centerWindow()

        self.authService = AuthServiceImpl()

        self.currentScreen = ScreenName.DASHBOARD if self.isAuthenticate() else ScreenName.LOGIN
        self.navigation = Navigation(self, height=self._current_height)

        self.screenManager = ScreenManager(
            self,
            authService=self.authService,
            width=self._current_width - self.navigation.width,
            height=self._current_height,
        )

        self.navigation.pack(side="left", fill="y")
        self.screenManager.pack(side="right", fill="both", expand=True)
        # self.loginScreen = LoginScreen(self, self.authService, )
        self.isAuthenticate()

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
        self.title(f"EasyCard - {title}")

    def navigate(self, screen: str) -> None:
        """
        Navigate to a specific screen.

        Args:
            screen (str): The name of the screen to navigate to.
        """
        # print(screen, "from app.py")
        self.navigation.navigate(screen)

    def isAuthenticate(self):
        response = self.authService.verifyAPIKey()
        print("isAuthenticate", response.is_success)
        return response.is_success
        if not response.is_error:
            self.loginScreen.place(relx=0, rely=0, relwidth=1, relheight=1)
            self.currentScreen = ScreenName.LOGIN
            return
        apiKeey = self.authService.getAPIKey()
        if not apiKeey:
            self.loginScreen.place(relx=0, rely=0, relwidth=1, relheight=1)
            self.currentScreen = ScreenName.LOGIN
            return
        self.screenManager.onLoginSuccess(apiKeey)
        self.navigate(ScreenName.DASHBOARD)

    def logout(self):
        self.authService.logout()
        self.screenManager.apiKey.set("")
        self.navigate(ScreenName.LOGIN)
