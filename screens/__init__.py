import matplotlib.pyplot as plt
from customtkinter import CTkBaseClass, CTkFrame

from config.settings import Color, ScreenName
from models.types import RCParams
from screens.dashboardScreen import DashboardScreen
from screens.dataScreen import DataScreen
from screens.newCardScreen import NewCardScreen
from screens.settingScreen import SettingScreen
from services.matplotlibService import MatplotlibService


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

        self.dashboardScreen = DashboardScreen(self, chartService=MatplotlibService(plt, **self.rcParamsHelper()))
        self.newCardScreen = NewCardScreen(self)
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

    def rcParamsHelper(self) -> RCParams:
        """
        Generates the RCParams object for customizing the appearance of plots based on the current appearance mode.
        
        Returns:
            RCParams: The RCParams object with the customized appearance settings.
        """
        appearance_mode = self._get_appearance_mode()
        axesFaceColor = Color.BG_CARD[1] if appearance_mode == "dark" else Color.BG_CARD[0]
        xTickColor = Color.WHITE if appearance_mode == "dark" else Color.BLACK
        yTickColor = Color.WHITE if appearance_mode == "dark" else Color.BLACK

        return RCParams(
            axesFaceColor=axesFaceColor,
            figureFaceColor=axesFaceColor,
            savefigFaceColor=axesFaceColor,
            axesEdgecolor=axesFaceColor,
            xTickColor=xTickColor,
            yTickColor=yTickColor,
        )

    def changeScreen(self, screen: str) -> None:
        """
        Changes the current screen to the specified screen.

        Args:
            screen (str): The name of the screen to switch to.
        """
        self.dashboardScreen.chartService = MatplotlibService(plt, **self.rcParamsHelper())
        self.dashboardScreen.updateCanvas()
        self.rentder(screen)
    
    def navigate(self, screen: str) -> None:
        self.master.navigate(screen)
