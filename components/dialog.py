from typing import Dict, List, Tuple

from customtkinter import CTkButton, CTkEntry, CTkFont, CTkLabel, CTkOptionMenu, CTkToplevel, ThemeManager

from config.settings import Color


class Dialog(CTkToplevel):
    """
    Dialog with extra window, message, entry widget, cancel and ok button.
    For detailed information check out the documentation.
    """

    width = 350
    height = 250

    def __init__(
        self,
        fg_color: str | Tuple[str, str] | None = Color.BG_CONTENT,
        text_color: str | Tuple[str, str] | None = None,
        button_fg_color: str | Tuple[str, str] | None = Color.BG_ACTIVE_BUTTON_NAVIGATION,
        button_hover_color: str | Tuple[str, str] | None = Color.BG_HOVER_BUTTON_NAVIGATION,
        button_text_color: str | Tuple[str, str] | None = Color.WHITE,
        entry_fg_color: str | Tuple[str, str] | None = None,
        entry_border_color: str | Tuple[str, str] | None = None,
        entry_text_color: str | Tuple[str, str] | None = None,
        dropdown_fg_color: str | Tuple[str, str] | None = Color.BG_CONTENT_SECONDARY,
        dropdown_button_color: str | Tuple[str, str] | None = Color.BG_ACTIVE_BUTTON_NAVIGATION,
        dropdown_text_color: str | Tuple[str, str] | None = Color.TEXT,
        dropdown_button_hover_color: str | Tuple[str, str] | None = Color.BG_HOVER_BUTTON_NAVIGATION,
        dropdown_values: List[str] | None = None,
        title: str = "CTkDialog",
        font: tuple | CTkFont | None = None,
        text: str = "CTkDialog",
    ) -> None:
        super().__init__(fg_color=fg_color)
        self.centerWindow()

        self._fg_color = (
            ThemeManager.theme["CTkToplevel"]["fg_color"] if fg_color is None else self._check_color_type(fg_color)
        )  # noqa: E501
        self._text_color = (
            ThemeManager.theme["CTkLabel"]["text_color"]
            if text_color is None
            else self._check_color_type(button_hover_color)
        )  # noqa: E501
        self._button_fg_color = (
            ThemeManager.theme["CTkButton"]["fg_color"]
            if button_fg_color is None
            else self._check_color_type(button_fg_color)
        )  # noqa: E501
        self._button_hover_color = (
            ThemeManager.theme["CTkButton"]["hover_color"]
            if button_hover_color is None
            else self._check_color_type(button_hover_color)
        )  # noqa: E501
        self._button_text_color = (
            ThemeManager.theme["CTkButton"]["text_color"]
            if button_text_color is None
            else self._check_color_type(button_text_color)
        )  # noqa: E501
        self._entry_fg_color = (
            ThemeManager.theme["CTkEntry"]["fg_color"]
            if entry_fg_color is None
            else self._check_color_type(entry_fg_color)
        )  # noqa: E501
        self._entry_border_color = (
            ThemeManager.theme["CTkEntry"]["border_color"]
            if entry_border_color is None
            else self._check_color_type(entry_border_color)
        )  # noqa: E501
        self._entry_text_color = (
            ThemeManager.theme["CTkEntry"]["text_color"]
            if entry_text_color is None
            else self._check_color_type(entry_text_color)
        )  # noqa: E501
        self._dropdown_text_color = (
            ThemeManager.theme["CTkOptionMenu"]["text_color"]
            if dropdown_text_color is None
            else self._check_color_type(dropdown_text_color)
        )  # noqa: E501
        self._dropdown_fg_color = (
            ThemeManager.theme["CTkOptionMenu"]["fg_color"]
            if dropdown_fg_color is None
            else self._check_color_type(dropdown_fg_color)
        )  # noqa: E501
        self._dropdown_button_color = (
            ThemeManager.theme["CTkOptionMenu"]["button_color"]
            if dropdown_button_color is None
            else self._check_color_type(dropdown_button_color)
        )  # noqa: E501
        self._dropdown_button_hover_color = (
            ThemeManager.theme["CTkOptionMenu"]["button_hover_color"]
            if dropdown_button_hover_color is None
            else self._check_color_type(dropdown_button_hover_color)
        )  # noqa: E501
        self._dropdown_values: List[str] = dropdown_values or ["Option 1", "Option 2", "Option 3"]

        self._user_input: str | None = None
        self._dropdown_value: str | None = None
        self._running: bool = False
        self._title = title
        self._text = text
        self._font = font

        self.title(self._title)
        self.lift()  # lift window on top
        self.attributes("-topmost", True)  # stay on top
        self.protocol("WM_DELETE_WINDOW", self._on_closing)
        self.after(
            10, self._create_widgets
        )  # create widgets with slight delay, to avoid white flickering of background  # noqa: E501
        self.resizable(False, False)
        self.grab_set()  # make other windows not clickable

    def _create_widgets(self) -> None:
        self.grid_columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)

        self._label = CTkLabel(
            master=self,
            width=300,
            wraplength=300,
            fg_color=Color.TRANSPARENT,
            text_color=self._text_color,
            text=self._text,
            font=self._font,
        )
        self._label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self._label_error = CTkLabel(
            master=self,
            width=300,
            wraplength=300,
            fg_color=Color.TRANSPARENT,
            text_color=self._text_color,
            text=self._text,
            font=self._font,
        )

        self._entry = CTkEntry(
            master=self,
            width=230,
            fg_color=self._entry_fg_color,
            border_color=self._entry_border_color,
            text_color=self._entry_text_color,
            font=self._font,
        )
        self._entry.grid(row=2, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="ew")

        self._dropdown = CTkOptionMenu(
            master=self,
            values=self._dropdown_values,
            fg_color=self._dropdown_fg_color,
            text_color=self._dropdown_text_color,
            button_color=self._dropdown_button_color,
            button_hover_color=self._dropdown_button_hover_color,
            font=self._font,
        )
        self._dropdown.grid(row=3, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="ew")

        self._cancel_button = CTkButton(
            master=self,
            width=100,
            border_width=0,
            fg_color=Color.BG_CARD,
            hover_color=self._button_hover_color,
            text_color=Color.TEXT,
            text="Cancel",
            font=self._font,
            command=self._cancel_event,
        )
        self._cancel_button.grid(row=4, column=0, columnspan=1, padx=(20, 5), pady=(10, 20), sticky="ew")

        self._ok_button = CTkButton(
            master=self,
            width=100,
            border_width=0,
            fg_color=self._button_fg_color,
            hover_color=self._button_hover_color,
            text_color=self._button_text_color,
            text="Ok",
            font=self._font,
            command=self._ok_event,
        )
        self._ok_button.grid(row=4, column=1, columnspan=1, padx=(5, 20), pady=(10, 20), sticky="ew")

        self.after(150, lambda: self._entry.focus())  # set focus to entry with slight delay, otherwise it won't work
        self._entry.bind("<Return>", self._ok_event)

        for b in [self._cancel_button]:
            if self._get_appearance_mode() == "light":
                b.bind(
                    "<Enter>",
                    lambda e: self._cancel_button.configure(text_color=Color.WHITE, fg_color=self._button_hover_color),
                )
                b.bind(
                    "<Leave>", lambda e: self._cancel_button.configure(text_color=Color.BLACK, fg_color=Color.BG_CARD)
                )

    def _ok_event(self, event=None) -> None:
        code = self._entry.get()
        if not code:
            self._label_error.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
            self._label_error.configure(text="Please enter a value", text_color=Color.RED)
            self._label_error.after(10000, lambda: self._label_error.grid_forget())
            self._entry.configure(border_color=Color.RED)
            self._entry.focus()
            return
        elif len(code) != 12 or not code.isdigit():
            self._label_error.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
            self._label_error.configure(text="Code is invalid, must be 12 digits", text_color=Color.RED)
            self._label_error.after(10000, lambda: self._label_error.grid_forget())
            self._entry.configure(border_color=Color.RED)
            self._entry.focus()
            return
        elif self._dropdown.get() == "":
            self._label_error.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
            self._label_error.configure(text="Please select a value", text_color=Color.RED)
            self._label_error.after(10000, lambda: self._label_error.grid_forget())
            self._dropdown.configure(border_color=Color.RED)
            self._dropdown.focus()
            return
        self._user_input = self._entry.get()
        self._dropdown_value = self._dropdown.get()
        self.grab_release()
        self.destroy()

    def _on_closing(self) -> None:
        self.grab_release()
        self.destroy()

    def _cancel_event(self) -> None:
        self.grab_release()
        self.destroy()

    def centerWindow(self) -> None:
        """Center the application window on the screen."""
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (self.width // 2)
        y = (self.winfo_screenheight() // 2) - (self.height // 2)
        self.geometry(f"{self.width}x{self.height}+{x}+{y}")

    def get_input(self) -> Dict[str, str | None]:
        self.master.wait_window(self)
        return {"code": self._user_input, "type": self._dropdown_value}
