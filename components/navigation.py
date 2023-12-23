from typing import Literal, Tuple

from CTkToolTip import CTkToolTip
from customtkinter import (
    CTkBaseClass,
    CTkFrame,
    CTkOptionMenu,
    StringVar,
    set_appearance_mode,
)

from components.ui import Button, Image, Label
from components.ui.separator import Separator
from config.settings import LIST_SCREEN, AssetsImages, Color, ScreenName, imagesTupple


class Navigation(CTkFrame):
    DASHBOARD_IMAGE = imagesTupple(
        light=AssetsImages.DASHBOARD_LIGHT,
        dark=AssetsImages.DASHBOARD_DARK,
    )
    NEW_IMAGE = imagesTupple(
        light=AssetsImages.NEW_LIGHT,
        dark=AssetsImages.NEW_DARK,
    )
    DATA_IMAGE = imagesTupple(
        light=AssetsImages.DATA_LIGHT,
        dark=AssetsImages.DATA_DARK,
    )
    SETTING_IMAGE = imagesTupple(
        light=AssetsImages.SETTING_LIGHT,
        dark=AssetsImages.SETTING_DARK,
    )
    EXIT_IMAGE = imagesTupple(
        light=AssetsImages.EXIT_LIGHT,
        dark=AssetsImages.EXIT_DARK,
    )
    SIZE_BUTTON = (23, 23)
    HEIGHT_BUTTON = 55

    def __init__(self, master: CTkBaseClass, width: int, height: int) -> None:
        self.master = master
        self.width = width
        self.height = height

        super().__init__(
            self.master,
            width=self.width,
            height=650,
            fg_color=Color.BG_NAVIGATION,
            corner_radius=0,
        )

        self.frame = CTkFrame(self, width=self.width, height=650, fg_color="transparent")
        self.frame.pack(expand=True, fill="both", padx=8)

        self.boxTitle = CTkFrame(self.frame, width=self.width * 0.9, fg_color="transparent")
        Label(self.boxTitle, text="", image=AssetsImages.LOGO, imageSize=(40, 40)).pack()
        Label(
            self.boxTitle,
            text="Easy Credit Card",
            fontSize=18,
            fontWeight="bold",
            height=30,
        ).pack(pady=10)

        self.dashboard = Button(
            self.frame,
            text=f"  {ScreenName.DASHBOARD_TITLE}",
            width=self.width * 0.9,
            height=self.HEIGHT_BUTTON,
            command=lambda: self.navigate(ScreenName.DASHBOARD),
            fg_color=Color.BG_ACTIVE_BUTTON_NAVIGATION,
            hover_color=Color.BG_HOVER_BUTTON_NAVIGATION,
            image=self.DASHBOARD_IMAGE,
            imageSize=self.SIZE_BUTTON,
            anchor="w",
        )
        CTkToolTip(self.dashboard, delay=0.3, message=ScreenName.DASHBOARD_TITLE)
        self.newCard = Button(
            self.frame,
            text=f"  {ScreenName.NEW_TITLE}",
            width=self.width * 0.9,
            height=self.HEIGHT_BUTTON,
            command=lambda: self.navigate(ScreenName.NEW),
            fg_color=Color.BG_BUTTON_NAVIGATION,
            hover_color=Color.BG_HOVER_BUTTON_NAVIGATION,
            image=self.NEW_IMAGE,
            imageSize=self.SIZE_BUTTON,
            anchor="w",
        )
        CTkToolTip(self.newCard, delay=0.3, message=ScreenName.NEW_TITLE)
        self.data = Button(
            self.frame,
            text=f"  {ScreenName.DATA_TITLE}",
            width=self.width * 0.9,
            height=self.HEIGHT_BUTTON,
            command=lambda: self.navigate(ScreenName.DATA),
            fg_color=Color.BG_BUTTON_NAVIGATION,
            hover_color=Color.BG_HOVER_BUTTON_NAVIGATION,
            image=self.DATA_IMAGE,
            imageSize=self.SIZE_BUTTON,
            anchor="w",
        )
        CTkToolTip(self.data, delay=0.3, message=ScreenName.DATA_TITLE)
        self.setting = Button(
            self.frame,
            text=f"  {ScreenName.SETTING_TITLE}",
            width=self.width * 0.9,
            height=self.HEIGHT_BUTTON,
            command=lambda: self.navigate(ScreenName.SETTING),
            fg_color=Color.BG_BUTTON_NAVIGATION,
            hover_color=Color.BG_HOVER_BUTTON_NAVIGATION,
            image=self.SETTING_IMAGE,
            imageSize=self.SIZE_BUTTON,
            anchor="w",
        )
        CTkToolTip(self.setting, delay=0.3, message=ScreenName.SETTING_TITLE)
        self.optionTheme = StringVar(value=self._get_appearance_mode())
        self.selectorTheme = CTkOptionMenu(
            self.frame,
            width=self.width * 0.9,
            values=["Light", "Dark"],
            text_color=Color.TEXT,
            fg_color=Color.BG_CARD,
            button_color=Color.BG_ACTIVE_BUTTON_NAVIGATION,
            button_hover_color=Color.BG_ACTIVE_BUTTON_NAVIGATION,
            dropdown_fg_color=Color.BG_CONTENT,
            command=self.toggleTheme,
            variable=self.optionTheme,
        )
        self.exit = Button(
            self.frame,
            text="  Exit",
            width=self.width * 0.9,
            height=40,
            command=lambda: self.master.quit(),
            fg_color=Color.BG_BUTTON_NAVIGATION,
            hover_color=Color.RED,
            image=self.EXIT_IMAGE,
            imageSize=self.SIZE_BUTTON,
            anchor="w",
        )
        CTkToolTip(self.exit, delay=0.3, message="Exit")

        self.showWidgets()
        self.updateCoderNavButtonActive()

    def showWidgets(self) -> None:
        """
        Show the widgets on the frame.

        This function is responsible for displaying the widgets on the frame in the desired layout.
        It places several widgets, including the box title, dashboard, new card, data, setting, selector theme
        and exit button, on the frame using the grid layout manager.
        The widgets are placed at specific rows and columns on the frame.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None: This function does not return anything.
        """
        Separator(self.frame, height=20).grid(row=0, column=0)
        self.boxTitle.grid(row=1, column=0, sticky="ew")

        row = 2
        Separator(self.frame, height=50).grid(row=row, column=0)
        self.dashboard.grid(row=row + 1, column=0, sticky="ew")

        Separator(self.frame).grid(row=row + 2, column=0)
        self.newCard.grid(row=row + 3, column=0, sticky="ew")

        Separator(self.frame).grid(row=row + 4, column=0)
        self.data.grid(row=row + 5, column=0, sticky="ew")

        Separator(self.frame).grid(row=row + 6, column=0)
        self.setting.grid(row=row + 7, column=0, sticky="ew")

        Separator(self.frame, height=180).grid(row=row + 8, column=0)
        self.selectorTheme.grid(row=row + 9, column=0, sticky="s")

        Separator(self.frame, height=16).grid(row=row + 10, column=0)
        self.exit.grid(row=row + 11, column=0, sticky="s")

    def navigate(self, screen: str) -> None:
        """
        Navigates to the specified screen in the application and configure the navigation component.

        Args:
            screen (str): The name of the screen to navigate to.

        Returns:
            None: This function does not return anything.
        """
        if screen not in LIST_SCREEN:
            raise AttributeError(f"{screen} screen not found in {LIST_SCREEN}")
        self.resetDefault()

        _image, navButtonCurrentScreen = self.getObjectNavButtonCurrentScreen(screen)

        if navButtonCurrentScreen:
            appearance_mode = self._get_appearance_mode()

            # Configure the screen object
            navButtonCurrentScreen.configure(
                fg_color=Color.BG_ACTIVE_BUTTON_NAVIGATION,
                image=Image(
                    imagesTupple(
                        light=_image,
                        dark=_image,
                    )
                )
                if appearance_mode == "light"
                else Image(getattr(self, f"{screen.upper()}_IMAGE")),
                text_color=Color.WHITE if appearance_mode == "light" else Color.TEXT,
            )

        self.master.currentScreen.set(screen)
        self.master.screenManager.changeScreen(screen)

    def resetDefault(self) -> None:
        """
        his function resets the default configuration navigation component in the application.
        It takes no parameters and does not return any value.
        """
        screen_defaults = {
            self.dashboard: self.DASHBOARD_IMAGE,
            self.newCard: self.NEW_IMAGE,
            self.data: self.DATA_IMAGE,
            self.setting: self.SETTING_IMAGE,
        }

        for screen_object, image_attr in screen_defaults.items():
            screen_object.configure(
                fg_color=Color.BG_BUTTON_NAVIGATION,
                text_color=Color.TEXT,
                image=Image(image_attr, size=self.SIZE_BUTTON),
            )

    def toggleTheme(self, theme: Literal["light", "dark"]) -> None:
        """
        Toggles the theme of the application.

        Args:
            theme (str): The name of the theme to be toggled. Can be either 'light' or 'dark'.
        """
        self.optionTheme.set(theme)
        set_appearance_mode(theme)
        self.master.screenManager.changeScreen(self.master.currentScreen.get())
        image, navButtonCurrentScreen = self.getObjectNavButtonCurrentScreen(self.master.currentScreen.get())

        if navButtonCurrentScreen:
            navButtonCurrentScreen.configure(
                text_color=Color.WHITE,
                image=Image(
                    imagesTupple(
                        light=image,
                        dark=image,
                    )
                ),
            )

    def getObjectNavButtonCurrentScreen(self, screen: str) -> Tuple[Image, Button]:
        """
        Returns an image constant and the navigation button object associated with the current screen.

        Args:
            screen (str): The name of the screen.

        :return: A tuple containing the image constant and screen object.
        :rtype: tuple
        """
        screen_map = {
            f"{ScreenName.DASHBOARD}": (AssetsImages.DASHBOARD_DARK, self.dashboard),
            f"{ScreenName.NEW}": (AssetsImages.NEW_DARK, self.newCard),
            f"{ScreenName.DATA}": (AssetsImages.DATA_DARK, self.data),
            f"{ScreenName.SETTING}": (AssetsImages.SETTING_DARK, self.setting),
        }
        return screen_map.get(screen, (None, None))
    
    def updateCoderNavButtonActive(self) -> None:
        image, navButtonCurrentScreen = self.getObjectNavButtonCurrentScreen(self.master.currentScreen.get())
        navButtonCurrentScreen.configure(
            text_color=Color.WHITE,
            image=Image(
                imagesTupple(
                    light=image,
                    dark=image,
                )
            )
        )
