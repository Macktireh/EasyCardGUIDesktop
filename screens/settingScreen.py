import contextlib
from tkinter import StringVar
from typing import Literal

from customtkinter import CTkBaseClass, CTkFrame, CTkOptionMenu, CTkScrollableFrame

from components.ui import Button, Input, Label
from config.settings import AssetsImages, Color, imagesTupple


class SettingScreen(CTkFrame):
    THEME_IMAGE = imagesTupple(
        light=AssetsImages.THEME_LIGHT,
        dark=AssetsImages.THEME_DARK,
    )
    GENERAL_IMAGE = imagesTupple(
        light=AssetsImages.GENERAL_LIGHT,
        dark=AssetsImages.GENERAL_DARK,
    )
    API_IMAGE = imagesTupple(
        light=AssetsImages.API_LIGHT,
        dark=AssetsImages.API_DARK,
    )
    EYE_IMAGE = imagesTupple(
        light=AssetsImages.EYE_LIGHT,
        dark=AssetsImages.EYE_DARK,
    )
    EYE_CLOSED_IMAGE = imagesTupple(
        light=AssetsImages.EYE_CLOSED_LIGHT,
        dark=AssetsImages.EYE_CLOSED_DARK,
    )
    KEY_IMAGE = imagesTupple(
        light=AssetsImages.KEY_LIGHT,
        dark=AssetsImages.KEY_DARK,
    )
    PRIVACY_IMAGE = imagesTupple(
        light=AssetsImages.PRIVACY_LIGHT,
        dark=AssetsImages.PRIVACY_DARK,
    )
    NOTIFICATION_IMAGE = imagesTupple(
        light=AssetsImages.NOTIFICATION_LIGHT,
        dark=AssetsImages.NOTIFICATION_DARK,
    )
    HELP_IMAGE = imagesTupple(
        light=AssetsImages.HELP_LIGHT,
        dark=AssetsImages.HELP_DARK,
    )
    RELOAD_IMAGE = imagesTupple(
        light=AssetsImages.RELOAD_LIGHT,
        dark=AssetsImages.RELOAD_DARK,
    )
    INFO_IMAGE = imagesTupple(
        light=AssetsImages.INFO_LIGHT,
        dark=AssetsImages.INFO_DARK,
    )
    displayApiKey = True

    def __init__(self, master: CTkBaseClass) -> None:
        self.master = master

        super().__init__(
            self.master,
            width=self.master._current_width,
            height=self.master._current_height,
            fg_color="transparent",
            corner_radius=0,
        )

        self.body = CTkScrollableFrame(
            self,
            fg_color=Color.BG_CONTENT,
            width=self.master._current_width,
            height=self.master._current_height,
        )
        self.body.pack(fill="both", expand=True)

        self.container = CTkFrame(self.body, fg_color=Color.BG_CARD, width=1150)
        self.container.pack(padx=10, pady=(40, 0))

        c = CTkFrame(self.container, fg_color=Color.BG_CONTENT, height=65, width=1100)
        c.pack(pady=(10, 0.5), padx=10)
        Label(c, text="   Appearance theme", fontSize=14, image=self.THEME_IMAGE, compound="left").place(
            relx=0.03, rely=0.13
        )
        self.optionTheme = StringVar(value=self._get_appearance_mode())
        self.themeSelector = CTkOptionMenu(
            c,
            values=["Light", "Dark"],
            text_color=Color.TEXT,
            fg_color=Color.BG_CARD,
            button_color=Color.BG_ACTIVE_BUTTON_NAVIGATION,
            button_hover_color=Color.BG_ACTIVE_BUTTON_NAVIGATION,
            dropdown_fg_color=Color.BG_CONTENT,
            command=self.toggleTheme,
            variable=self.optionTheme,
        )
        self.themeSelector.place(relx=0.67, rely=0.3, relwidth=0.3, relheight=0.4)

        c1 = CTkFrame(self.container, fg_color=Color.BG_CONTENT, height=65, width=1100)
        c1.pack(padx=10, pady=0.5)
        l1 = Label(c1, text="   General", fontSize=14, image=self.GENERAL_IMAGE, compound="left")
        l1.place(relx=0.03, rely=0.13)
        self.onHover(c1, l1)

        c2 = CTkFrame(self.container, fg_color=Color.BG_CONTENT, height=65, width=1100)
        c2.pack(padx=10, pady=(0.5, 10))
        l2 = Label(c2, text="   API key", fontSize=14, image=self.API_IMAGE, compound="left")
        l2.place(relx=0.03, rely=0.13)
        _ = CTkFrame(c2, fg_color=Color.BG_CONTENT)
        _.place(relx=0.3, rely=0.3, relwidth=0.62, relheight=0.4)
        self.apiKeyEntry = Input(
            _,
            width=470,
            text_color=Color.TEXT,
            fg_color=Color.BG_CARD,
            # defaultValue=self.master.apiKey.get(),
            show="●",
            on_change_callback=self.onChange,
        )
        self.saveBtn = Button(
            _,
            text="Save",
            textColor=Color.WHITE,
            width=60,
            state="disabled",
            text_color_disabled=Color.TEXT_GRAY,
            command=self.saveApiKey,
        )
        self.apiKeyEntry.pack(side="left", fill="both", expand=True)
        # self.apiKeyEntry.place(relx=0.3, rely=0.3, relwidth=0.5, relheight=0.4)
        self.saveBtn.pack(side="right", padx=(5, 0))
        # self.saveBtn.place(relx=0.8, rely=0.3, relwidth=0.1, relheight=0.4)
        self.iconDisplay = Label(c2, text="", fontSize=12, image=self.EYE_IMAGE, imageSize=(18, 18))
        self.iconHide = Label(c2, text="", fontSize=12, image=self.EYE_CLOSED_IMAGE, imageSize=(18, 18))
        self.iconDisplay.bind("<Button-1>", lambda event: self.handleDisplayAPIKey())
        self.iconHide.bind("<Button-1>", lambda event: self.handleDisplayAPIKey())
        self.handleDisplayAPIKey()
        for i in [self.iconDisplay]:
            i.bind("<Enter>", lambda event: self.iconDisplay.configure(cursor="hand2"))
            i.bind("<Leave>", lambda event: self.iconDisplay.configure(cursor=""))
        for i in [self.iconHide]:
            i.bind("<Enter>", lambda event: self.iconHide.configure(cursor="hand2"))
            i.bind("<Leave>", lambda event: self.iconHide.configure(cursor=""))

        self.container = CTkFrame(self.body, fg_color=Color.BG_CARD, width=1150)
        self.container.pack(padx=10, pady=20)

        c3 = CTkFrame(self.container, fg_color=Color.BG_CONTENT, height=65, width=1100)
        c3.pack(pady=(10, 0.5), padx=10)
        l3 = Label(c3, text="   Account", fontSize=14, image=self.KEY_IMAGE, compound="left")
        l3.place(relx=0.03, rely=0.13)
        self.onHover(c3, l3)

        c4 = CTkFrame(self.container, fg_color=Color.BG_CONTENT, height=65, width=1100)
        c4.pack(padx=10, pady=0.5)
        l4 = Label(c4, text="   Privacy", fontSize=14, image=self.PRIVACY_IMAGE, compound="left")
        l4.place(relx=0.03, rely=0.13)
        self.onHover(c4, l4)

        c5 = CTkFrame(self.container, fg_color=Color.BG_CONTENT, height=65, width=1100)
        c5.pack(padx=10, pady=(0.5, 10))
        l5 = Label(c5, text="   Notification", fontSize=14, image=self.NOTIFICATION_IMAGE, compound="left")
        l5.place(relx=0.03, rely=0.13)
        self.onHover(c5, l5)

        self.container = CTkFrame(self.body, fg_color=Color.BG_CARD, width=1150)
        self.container.pack(padx=10)

        c6 = CTkFrame(self.container, fg_color=Color.BG_CONTENT, height=65, width=1100)
        c6.pack(padx=10, pady=(10, 0.5))
        l6 = Label(c6, text="   Reload App", fontSize=14, image=self.RELOAD_IMAGE, compound="left")
        l6.place(relx=0.03, rely=0.13)
        self.onHover(c6, l6)
        c6.bind("<Button-1>", lambda event: self.reload())

        c7 = CTkFrame(self.container, fg_color=Color.BG_CONTENT, height=65, width=1100)
        c7.pack(pady=0.5, padx=10)
        l7 = Label(c7, text="   Help", fontSize=14, image=self.HELP_IMAGE, compound="left")
        l7.place(relx=0.03, rely=0.13)
        self.onHover(c7, l7)

        c8 = CTkFrame(self.container, fg_color=Color.BG_CONTENT, height=65, width=1100)
        c8.pack(pady=(0.5, 10), padx=10)
        l8 = Label(c8, text="   About", fontSize=14, image=self.INFO_IMAGE, compound="left")
        l8.place(relx=0.03, rely=0.13)
        self.onHover(c8, l8)

    def onHover(self, frame, label, color=Color.BG_CONTENT_SECONDARY) -> None:
        for i in [frame]:
            i.bind("<Enter>", lambda event: self.onMouseEnterFrame(frame, color))
            i.bind("<Leave>", lambda event: self.onMouseLeaveFrame(frame))
        for i in [label]:
            i.bind("<Enter>", lambda event: self.onMouseEnterLabel(label, frame, color))
            i.bind("<Leave>", lambda event: self.onMouseLeaveLabel(label, frame))

    def toggleTheme(self, theme: Literal["light", "dark"]) -> None:
        self.optionTheme.set(theme)
        self.master.toggleTheme(theme)

    def onMouseEnterFrame(self, element, color=Color.BG_CONTENT_SECONDARY) -> None:
        element.configure(fg_color=color, cursor="hand2")

    def onMouseLeaveFrame(self, element):
        element.configure(fg_color=Color.BG_CONTENT, cursor="")

    def onMouseEnterLabel(self, element1, element2, color=Color.BG_CONTENT_SECONDARY) -> None:
        element1.configure(cursor="hand2")
        self.onMouseEnterFrame(element2, color)

    def onMouseLeaveLabel(self, element1, element2) -> None:
        element1.configure(cursor="")
        self.onMouseLeaveFrame(element2)

    def onChange(self, var: StringVar) -> None:
        if var.get() != self.master.apiKey.get():
            self.saveBtn.configure(state="normal")
        else:
            with contextlib.suppress(Exception):
                self.saveBtn.configure(state="disabled")

    def saveApiKey(self) -> None:
        _apiKey = self.apiKeyEntry.getValue()
        self.master.apiKey.set(_apiKey)
        self.master.authService.saveAPIKey(_apiKey)
        self.saveBtn.configure(state="disabled")

    def handleDisplayAPIKey(self) -> None:
        if self.displayApiKey:
            self.displayApiKey = False
            self.iconDisplay.place_forget()
            self.iconHide.place(relx=0.93, rely=0.13)
            self.apiKeyEntry.setPassword(True)
        else:
            self.displayApiKey = True
            self.iconHide.place_forget()
            self.iconDisplay.place(relx=0.93, rely=0.13)
            self.apiKeyEntry.setPassword(False)

    def reload(self) -> None:
        self.master.reload()
