from customtkinter import CTkBaseClass, CTkFrame, CTkLabel, CTkProgressBar

from config.settings import Color


class ProgressBar(CTkFrame):
    def __init__(
        self,
        master: CTkBaseClass,
        width: int = 300,
        height: int = 50,
        defaultValue: float = 0.0,
    ) -> None:
        self.master = master
        self.width = width
        self.height = height
        self.defaultValue = defaultValue

        super().__init__(self.master, width=self.width, height=self.height, fg_color=Color.TRANSPARENT)

        self.label = CTkLabel(self, text=f"{int(self.defaultValue * 100)}%", width=self.width // 5)
        self.label.pack(side="left", padx=5, pady=10)

        self.progress = CTkProgressBar(self, width=(self.width * 4) // 5)
        self.progress.pack(side="right", padx=5, pady=10)

        self.progress.set(self.defaultValue)

    def setValue(self, value: float) -> None:
        self.progress.set(value)
        self.progress.update()
        self.label.configure(text=f"{int(value * 100)}%")
        self.label.update()

    def getValue(self) -> float:
        return self.progress.get()
