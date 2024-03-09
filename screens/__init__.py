from tkinter import StringVar
from typing import Literal

import matplotlib.pyplot as plt
from customtkinter import CTkBaseClass, CTkFrame

from components.ui import Label
from config.settings import Color, ScreenName
from screens.dashboardScreen import DashboardScreen
from screens.dataScreen import DataScreen
from screens.loginScreen import LoginScreen
from screens.newCardScreen import NewCardScreen
from screens.settingScreen import SettingScreen
from screens.splashScreen import SplashScreen
from services.authService import AuthService
from services.creditCardServiceImpl import CreditCardServiceImpl
from services.matplotlibService import MatplotlibService
from utils import rcParams


class ScreenManager(CTkFrame):
    def __init__(self, master: CTkBaseClass, authService: AuthService, width: int, height: int) -> None:
        self.master = master
        self.width = width
        self.height = height
        self.authService = authService

        super().__init__(
            self.master,
            width=self.width,
            height=self.height,
            fg_color=Color.BG_CONTENT,
            corner_radius=0,
        )

        self.apiKey = StringVar(self, value="", name="apiKey")
        self.alter = Label(
            self,
            text="The API key is either not valid or could not be found. Please check your API key or reconnect again.",
            fontSize=13,
            fontWeight="bold",
            fg_color=Color.ORANGE,
            height=24,
            corner_radius=4,
        )
        self.alter.pack(fill="x", pady=(2, 0), padx=2)
        # self.after(10000, self.alter.pack_forget)

        self.dashboardScreen = DashboardScreen(
            self, chartService=MatplotlibService(plt, **rcParams(self._get_appearance_mode()))
        )
        self.newCardScreen = NewCardScreen(self, creditCardService=CreditCardServiceImpl())
        self.dataScreen = DataScreen(self)
        self.settingScreen = SettingScreen(self)
        self.loginScreen = LoginScreen(self.master, self.authService, self.onLoginSuccess)

        self.rentder(self.master.currentScreen)
        self.updateApiKey()

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
            ScreenName.LOGIN: (self.loginScreen, ScreenName.LOGIN_TITLE),
        }

        # for name, (screen_obj, title) in screens.items():
        #     if screen == name:
        #         screen_obj.pack(expand=True, fill="both")
        #         self.master.setTitle(title)
        #     else:
        #         screen_obj.pack_forget()
        for name, (screen_obj, title) in screens.items():
            if screen == name:
                if screen == ScreenName.LOGIN:
                    screen_obj.place(relx=0, rely=0, relwidth=1, relheight=1)
                else:
                    screen_obj.pack(expand=True, fill="both")
                self.master.setTitle(title)
            else:
                if screen == ScreenName.LOGIN:
                    continue
                    # screen_obj.place_forget()
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

    def toggleTheme(self, theme: Literal["light", "dark"]) -> None:
        self.master.navigation.toggleTheme(theme)

    def syncTheme(self, theme: Literal["light", "dark"]) -> None:
        self.settingScreen.optionTheme.set(theme)

    def onLoginSuccess(self, apiKey: str) -> None:
        self.navigate(ScreenName.DASHBOARD)
        self.apiKey.set(apiKey)
        self.settingScreen.apiKeyEntry.setValue(apiKey)

    def updateApiKey(self) -> None:
        if self.master.currentScreen != ScreenName.LOGIN:
            self.apiKey.set(self.authService.getAPIKey() or "")
            self.settingScreen.apiKeyEntry.setValue(self.apiKey.get())


__all__ = [
    "ScreenManager",
    "LoginScreen",
    "DashboardScreen",
    "NewCardScreen",
    "DataScreen",
    "SettingScreen",
    "SplashScreen",
]
