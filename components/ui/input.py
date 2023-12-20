from customtkinter import CTkBaseClass, CTkEntry, CTkFrame, CTkLabel


class Input(CTkFrame):
    def __init__(
        self,
        master: CTkBaseClass,
        label: str = "Input",
        width: int = 300,
        height: int = 50,
        defaultValue: str = "",
        isPassword: bool = False,
        state: str = "normal",
    ) -> None:
        self.master = master
        self.label = label
        self.width = width
        self.height = height
        self.defaultValue = defaultValue
        self.isPassword = isPassword
        self.state = state

        super().__init__(self.master, width=self.width, height=self.height)

        self.label = CTkLabel(self, text=self.label, width=self.width // 3)
        self.label.pack(side="left", padx=5, pady=5)

        self.entry = CTkEntry(self, width=(self.width * 3) // 3, state=self.state)
        self.entry.pack(side="right", padx=5, pady=5)
        self.entry.insert(0, self.defaultValue)

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

    def disable(self) -> None:
        self.entry.configure(state="disabled")

    def senable(self) -> None:
        self.entry.configure(state="normal")

    def setPassword(self, value: bool) -> None:
        if value:
            self.entry.configure(show="*")
        else:
            self.entry.configure(show="")
