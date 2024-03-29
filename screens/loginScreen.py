import webbrowser
from typing import Callable

from customtkinter import CTkBaseClass, CTkFrame

from components.ui import Button, InputLabel, Label
from config.settings import AssetsImages, Color, ScreenName, imagesTupple
from services.authService import AuthService


class LoginScreen(CTkFrame):
    CARD_CREDIT_IMAGE = imagesTupple(
        light=AssetsImages.CARD_CREDIT_LIGHT,
        dark=AssetsImages.CARD_CREDIT_DARK,
    )

    def __init__(
        self, master: CTkBaseClass, authService: AuthService, callback: Callable[[str], None] | None = None
    ) -> None:
        self.master = master
        self.authService = authService
        self.callback = callback

        super().__init__(
            self.master,
            width=self.master._current_width,
            height=self.master._current_height,
            fg_color=Color.BG_CONTENT,
            corner_radius=0,
        )

        Label(self, text="Welcome to Easy Card", fontSize=26, fontWeight="bold").pack(pady=(50, 30))

        container = CTkFrame(self, fg_color=Color.TRANSPARENT)
        container.pack()
        Label(container, text="Login to your account to continue", fontSize=20).pack(pady=(10, 30))

        leftFrame = CTkFrame(container, fg_color=Color.TRANSPARENT, width=500)
        leftFrame.pack(side="left", fill="both", expand=True, padx=10)

        rightFrame = CTkFrame(container, fg_color=Color.TRANSPARENT, width=500)
        rightFrame.pack(side="right", fill="both", expand=True, padx=20)

        Label(leftFrame, text="", image=self.CARD_CREDIT_IMAGE, imageSize=(450, 300)).pack(pady=20)

        self.email = InputLabel(
            rightFrame, label="Email", width=300, labelWidth=45, height=50, defaultValue="admin@example.com"
        )
        self.email.grid(row=0, column=0, pady=(20, 10))
        self.password = InputLabel(
            rightFrame, label="Password", width=300, height=50, labelWidth=70, isPassword=True, defaultValue="admin"
        )
        self.password.grid(row=1, column=0, pady=(10, 20))

        self.loginButton = Button(
            rightFrame,
            text="Login",
            textColor=Color.WHITE,
            width=400,
            height=40,
            command=lambda: self.handleLogin(),
        )
        self.loginButton.grid(row=2, column=0, pady=(15, 5))

        self.errorLabel = Label(rightFrame, text="", textColor=Color.ORANGE, height=30, fontSize=14)

        linkSignup = Label(
            rightFrame,
            text="Sign up if you don't have an account",
            height=30,
            fontSize=14,
            textColor=["blue", "cyan"],
        )
        linkSignup.grid(row=4, column=0, pady=10)
        linkSignup.bind("<Button-1>", lambda event: webbrowser.open_new_tab("https://www.github.com/Macktireh"))
        linkSignup.bind("<Enter>", lambda event: linkSignup.configure(font=("Arial", 14, "underline"), cursor="hand2"))
        linkSignup.bind("<Leave>", lambda event: linkSignup.configure(font=("Arial", 14), cursor="arrow"))

    def handleLogin(self) -> None:
        # return
        payload = {"email": self.email.getValue(), "password": self.password.getValue()}
        print(payload)
        response = self.authService.login(payload)
        print(response.json())
        if response.is_success:
            self.errorLabel.grid_forget()
            # self.master.reRenderScreenManager()
            self.master.currentScreen = ScreenName.DASHBOARD
            self.callback(response.json()["apiKey"])
            self.place_forget()
        else:
            self.errorLabel.grid(row=3, column=0)
            self.errorLabel.configure(text=response.json()["message"])
