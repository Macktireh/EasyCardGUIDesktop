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
    MENU_IMAGE = imagesTupple(
        light=AssetsImages.MENU_LIGHT,
        dark=AssetsImages.MENU_DARK,
    )
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
    HEIGHT_BUTTON = 40
    SIDEBAR_WIDTH = 200
    SIDEBAR_WIDTH_MINI = 50
    SIDEBAR_LARGE = True

    def __init__(self, master: CTkBaseClass, width: int = 200, height: int = 600) -> None:
        self.master = master
        self.width = width or self.SIDEBAR_WIDTH
        self.height = height

        super().__init__(
            self.master,
            width=self.width,
            height=650,
            fg_color=Color.BG_NAVIGATION,
            corner_radius=0,
        )

        self.frame = CTkFrame(self, width=self.width, height=650, fg_color=Color.TRANSPARENT)
        self.frame.pack(expand=True, fill="both", padx=8)

        self.boxTitle = CTkFrame(self.frame, width=self.width * 0.9, fg_color=Color.TRANSPARENT)
        self.menu = Label(
            self.boxTitle,
            text="",
            width=40,
            height=40,
            image=self.MENU_IMAGE,
            imageSize=self.SIZE_BUTTON,
            corner_radius=10,
        )
        self.menu.pack(pady=(10, 0), side="left")
        # self.menu.pack(pady=(10, 20), side="left")
        self.menu.bind("<Button-1>", lambda event: self.sideBarSizeToggle())

        for i in [self.menu]:
            i.bind("<Enter>", lambda event: self.menu.configure(fg_color=Color.BG_CARD, cursor="hand2"))
            i.bind("<Leave>", lambda event: self.menu.configure(fg_color=Color.TRANSPARENT, cursor=""))
        # Label(self.boxTitle, text="", image=AssetsImages.LOGO, imageSize=(40, 40)).pack()
        # Label(
        #     self.boxTitle,
        #     text="Easy Credit Card",
        #     fontSize=18,
        #     fontWeight="bold",
        #     height=30,
        # ).pack(pady=10)

        self.dashboard = Button(
            self.frame,
            text=f"  {ScreenName.DASHBOARD_TITLE}",
            fontSize=12,
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
            fontSize=12,
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
            fontSize=12,
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
            fontSize=12,
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
        self.themeSelector = CTkOptionMenu(
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
            text="  Logout",
            fontSize=12,
            width=self.width * 0.9,
            height=40,
            command=lambda: self.master.logout(),
            fg_color=Color.BG_BUTTON_NAVIGATION,
            hover_color=Color.BG_HOVER_BUTTON_NAVIGATION,
            image=self.EXIT_IMAGE,
            imageSize=self.SIZE_BUTTON,
            anchor="w",
        )
        CTkToolTip(self.exit, delay=0.3, message="Logout")

        self.showWidgets()
        self.updateCoderNavButtonActive()
        self.sideBarSizeToggle()

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
        Separator(self.frame, height=0).grid(row=0, column=0)
        self.boxTitle.grid(row=1, column=0, sticky="ew")

        row = 2
        Separator(self.frame, height=10).grid(row=row, column=0)
        self.dashboard.grid(row=row + 1, column=0, sticky="ew")

        Separator(self.frame).grid(row=row + 2, column=0)
        self.newCard.grid(row=row + 3, column=0, sticky="ew")

        Separator(self.frame).grid(row=row + 4, column=0)
        self.data.grid(row=row + 5, column=0, sticky="ew")

        Separator(self.frame).grid(row=row + 6, column=0)
        self.setting.grid(row=row + 7, column=0, sticky="ew")

        # Separator(self.frame, height=230).grid(row=row + 8, column=0)
        # self.themeSelector.grid(row=row + 9, column=0, sticky="s")

        # Separator(self.frame, height=43).grid(row=row + 10, column=0)
        self.exit.place(x=0, y=0, relx=1, rely=0.975, anchor="se")
        # self.exit.grid(row=row + 11, column=0, sticky="s")

    def sideBarSizeToggle(self) -> None:
        screen_defaults = {
            self.dashboard: ScreenName.DASHBOARD_TITLE,
            self.newCard: ScreenName.NEW_TITLE,
            self.data: ScreenName.DATA_TITLE,
            self.setting: ScreenName.SETTING_TITLE,
            self.exit: "Logout",
        }

        if self.SIDEBAR_LARGE:
            for screen_object, _ in screen_defaults.items():
                screen_object.configure(text="", anchor="center")
        else:
            for screen_object, title in screen_defaults.items():
                screen_object.configure(text=f"  {title}", anchor="w")

        self.contractSideBar()

        # self.SIDEBAR_LARGE = not self.SIDEBAR_LARGE

    def contractSideBar(self) -> None:
        screen_defaults = {
            self.boxTitle: "",
            self.dashboard: ScreenName.DASHBOARD_TITLE,
            self.newCard: ScreenName.NEW_TITLE,
            self.data: ScreenName.DATA_TITLE,
            self.setting: ScreenName.SETTING_TITLE,
            self.themeSelector: "",
            self.exit: "Logout",
        }
        if self.SIDEBAR_LARGE:
            self.configure(width=self.SIDEBAR_WIDTH_MINI)
            self.frame.configure(width=self.SIDEBAR_WIDTH_MINI)
            self.menu.configure(width=self.SIDEBAR_WIDTH_MINI * 0.9)
            for screen_object, _ in screen_defaults.items():
                screen_object.configure(width=self.SIDEBAR_WIDTH_MINI * 0.9)
                # self.after(10, self.expandSideBar)
        else:
            self.configure(width=self.SIDEBAR_WIDTH)
            self.frame.configure(width=self.SIDEBAR_WIDTH)
            self.menu.configure(width=40)
            for screen_object, _ in screen_defaults.items():
                screen_object.configure(width=self.SIDEBAR_WIDTH * 0.9)
                # self.after(10, self.contractSideBar)
        self.SIDEBAR_LARGE = not self.SIDEBAR_LARGE

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

        self.master.currentScreen = screen
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
        self.master.screenManager.syncTheme(theme)
        set_appearance_mode(theme)
        self.master.screenManager.changeScreen(self.master.currentScreen)
        image, navButtonCurrentScreen = self.getObjectNavButtonCurrentScreen(self.master.currentScreen)

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
        image, navButtonCurrentScreen = self.getObjectNavButtonCurrentScreen(self.master.currentScreen)
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
