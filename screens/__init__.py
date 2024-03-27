from threading import Thread
from tkinter import StringVar
from typing import List, Literal

import matplotlib.pyplot as plt
from customtkinter import CTkBaseClass, CTkFrame

from components import Modal, Toast
from config.settings import Color, ScreenName
from models.types import CreditCardDictOut
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
        self.creditCardService = CreditCardServiceImpl()

        super().__init__(
            self.master,
            width=self.width,
            height=self.height,
            fg_color=Color.BG_CONTENT,
            corner_radius=0,
        )

        self.apiKey = StringVar(self, value="", name="apiKey")
        self.toast = Toast(
            self,
            text="The API key is either not valid or could not be found. Please check your API key or reconnect again.",
        )
        

        # self.modal = CTkFrame(self, width=300, height=300, fg_color=Color.GRAY)
        # self.modal.place(relx=0.5, rely=0.5, anchor="center")

        response, isAuthorized = self.creditCardService.getAllCreditCards()

        # if not isAuthorized:
        self.toast.show()
        self.after(5000, lambda: self.toast.hide())
        self.after(10000, lambda: self.toast.show(before=self.getCurrentScreenObj()))

        self.data = response.json() if response.is_success else []

        self.initializeScreens()
        self.loginScreen = LoginScreen(self.master, self.authService, self.onLoginSuccess)
        self.rentder(self.master.currentScreen)
        self.updateApiKey()

        self.modal = Modal(
            self, text="Oops, we have an authentication problem.\n Please reload the application and try again."
        )
        self.modal.showModal()

    def getCurrentScreenObj(self):
        match self.master.currentScreen:
            case ScreenName.DASHBOARD:
                return self.dashboardScreen
            case ScreenName.NEW:
                return self.newCardScreen
            case ScreenName.DATA:
                return self.dataScreen
            case ScreenName.SETTING:
                return self.settingScreen

    def initializeScreens(self) -> None:
        self.dashboardScreen = DashboardScreen(
            self, chartService=MatplotlibService(plt, **rcParams(self._get_appearance_mode()))
        )
        self.newCardScreen = NewCardScreen(self, self.creditCardService)
        self.dataScreen = DataScreen(self, self.creditCardService)
        self.settingScreen = SettingScreen(self)

    def destroyScreens(self) -> None:
        self.dashboardScreen.destroy()
        self.newCardScreen.destroy()
        self.dataScreen.destroy()
        self.settingScreen.destroy()

    def reInitializeScreens(self) -> None:
        self.data = self.getData()
        self.destroyScreens()
        self.initializeScreens()

    def getData(self) -> List[CreditCardDictOut] | None:
        response, isAuthorized = self.creditCardService.getAllCreditCards()

        if not isAuthorized:
            self.toast.show()
        else:
            self.toast.hide()

        return response.json() if response.is_success else []

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
        self.checkAuthentication()

    def navigate(self, screen: str) -> None:
        self.master.navigate(screen)

    def toggleTheme(self, theme: Literal["light", "dark"]) -> None:
        self.master.navigation.toggleTheme(theme)

    def syncTheme(self, theme: Literal["light", "dark"]) -> None:
        self.settingScreen.optionTheme.set(theme)

    def onLoginSuccess(self, apiKey: str) -> None:
        self.reInitializeScreens()
        self.navigate(ScreenName.DASHBOARD)
        self.apiKey.set(apiKey)
        self.settingScreen.apiKeyEntry.setValue(apiKey)

    def updateApiKey(self) -> None:
        if self.master.currentScreen != ScreenName.LOGIN:
            self.apiKey.set(self.authService.getAPIKey() or "")
            self.settingScreen.apiKeyEntry.setValue(self.apiKey.get())
    
    def checkAuthentication(self) -> bool:
        """
        Check if the user is authenticated and return a boolean value.
        """
        def _checkAuthentication(self):
            response = self.authService.verifyAPIKey()
            print("isAuthenticate", response.is_success)
            if response.is_success:
                self.modal.showModal()
        
        Thread(target=_checkAuthentication, args=(self,)).start()
    
    def reload(self) -> None:
        from app import App

        self.master.destroy()
        App().mainloop()



__all__ = [
    "ScreenManager",
    "LoginScreen",
    "DashboardScreen",
    "NewCardScreen",
    "DataScreen",
    "SettingScreen",
    "SplashScreen",
]
