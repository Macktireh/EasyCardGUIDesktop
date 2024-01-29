import matplotlib.pyplot as plt
from customtkinter import CTkBaseClass, CTkFrame
from httpx import Client

from config.settings import Color, ScreenName
from screens.dashboardScreen import DashboardScreen
from screens.dataScreen import DataScreen
from screens.newCardScreen import NewCardScreen
from screens.settingScreen import SettingScreen
from screens.splashScreen import SplashScreen
from services.creditCardService import CreditCardService
from services.matplotlibService import MatplotlibService
from utils import rcParams


class ScreenManager(CTkFrame):
    def __init__(self, master: CTkBaseClass, width: int, height: int) -> None:
        self.master = master
        self.width = width
        self.height = height

        super().__init__(
            self.master,
            width=self.width,
            height=self.height,
            fg_color=Color.BG_CONTENT,
            corner_radius=0,
        )

        self.dashboardScreen = DashboardScreen(
            self, chartService=MatplotlibService(plt, **rcParams(self._get_appearance_mode()))
        )
        self.newCardScreen = NewCardScreen(self, creditCardService=CreditCardService(Client()))
        self.dataScreen = DataScreen(self)
        self.settingScreen = SettingScreen(self)

        self.rentder(self.master.currentScreen.get())

    def rentder(self, screen: str) -> None:
        """
        Renders the specified screen by hiding all other screens and packing the selected one.

        Args:
            screen (str): The name of the screen to be rendered.
        """
        screens = {
            ScreenName.DASHBOARD: (self.dashboardScreen, ScreenName.DASHBOARD_TITLE),
            ScreenName.NEW: (self.newCardScreen, ScreenName.NEW_TITLE),
            ScreenName.DATA: (self.dataScreen, ScreenName.DATA_TITLE),
            ScreenName.SETTING: (self.settingScreen, ScreenName.SETTING_TITLE),
        }

        for name, (screen_obj, title) in screens.items():
            if screen == name:
                screen_obj.pack(expand=True, fill="both")
                self.master.setTitle(title)
            else:
                screen_obj.pack_forget()

    def changeScreen(self, screen: str) -> None:
        """
        Changes the current screen to the specified screen.

        Args:
            screen (str): The name of the screen to switch to.
        """
        self.dashboardScreen.chartService = MatplotlibService(plt, **rcParams(self._get_appearance_mode()))
        self.dashboardScreen.updateCanvas()
        self.rentder(screen)

    def navigate(self, screen: str) -> None:
        self.master.navigate(screen)


__all__ = [
    "ScreenManager",
    "DashboardScreen",
    "NewCardScreen",
    "DataScreen",
    "SettingScreen",
    "SplashScreen",
]
