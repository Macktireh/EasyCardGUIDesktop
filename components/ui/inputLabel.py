from typing import Tuple

from customtkinter import CTkBaseClass, CTkEntry, CTkFrame, CTkLabel

from components.ui.separator import Separator


class InputLabel(CTkFrame):
    def __init__(
        self,
        master: CTkBaseClass,
        label: str | None = "Input",
        width: int = 300,
        height: int = 50,
        labelWidth: int = 100,
        entryWidth: int = 400,
        defaultValue: str = "",
        isPassword: bool = False,
        state: str = "normal",
        sep: int = 0,
        bgColor: str | Tuple[str, str] = "transparent",
        entryBgColor: str | Tuple[str, str] = "transparent",
        vertical: bool = True,
    ) -> None:
        self.master = master
        self.label = label
        self.width = width
        self.height = height
        self.labelWidth = labelWidth
        self.entryWidth = entryWidth
        self.defaultValue = defaultValue
        self.isPassword = isPassword
        self.state = state

        super().__init__(self.master, width=self.width, height=self.height, fg_color=bgColor)

        if self.label:
            self.label = CTkLabel(self, text=self.label, width=labelWidth, fg_color="transparent")
            self.label.pack(expand=True, anchor="w", side="top" if vertical else "left")
            Separator(self, width=sep).pack(expand=True, side="top" if vertical else "left")

        self.entry = CTkEntry(self, width=entryWidth, fg_color=entryBgColor)
        self.entry.pack(expand=True, side="top" if vertical else "left")
        self.entry.insert(0, self.defaultValue)
        if self.state != "normal":
            self.entry.configure(state=self.state)

        self.setPassword(self.isPassword)

    def getValue(self) -> str:
        return self.entry.get()

    def setValue(self, value: str) -> None:
        self.entry.delete(0, "end")
        self.entry.insert(0, value)
        self.entry.update()

    def clear(self) -> None:
        self.entry.delete(0, "end")
        self.entry.update()

    def setState(self, state: str) -> None:
        self.entry.configure(state=state)

    def setPassword(self, value: bool) -> None:
        if value:
            self.entry.configure(show="●")
        else:
            self.entry.configure(show="")
