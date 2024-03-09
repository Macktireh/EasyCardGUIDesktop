from tkinter import filedialog
from typing import Any, Callable, Tuple

from CTkToolTip import CTkToolTip
from customtkinter import CTkBaseClass, CTkFrame
from tkinterdnd2 import DND_FILES

from components.ui import Button, Image, InputLabel, Separator
from config.settings import AssetsImages, Color, imagesTupple
from utils.validator import Validator


class DragAndDrop(CTkFrame):
    DELETE_IMAGE = imagesTupple(
        light=AssetsImages.DELETE_LIGHT,
        dark=AssetsImages.DELETE_DARK,
    )
    EXTRACT_IMAGE = imagesTupple(
        light=AssetsImages.EXTRACT_LIGHT,
        dark=AssetsImages.EXTRACT_DARK,
    )
    DRAG_AND_DROP_IMAGE = imagesTupple(
        light=AssetsImages.DRAG_AND_DROP_LIGHT,
        dark=AssetsImages.DRAG_AND_DROP_DARK,
    )
    BUTTON_DND_TEXT = "Drag and drop image here or select an image"

    def __init__(
        self,
        master: CTkBaseClass,
        extractCode: Callable,
        fg_color: str | Tuple[str, str] | None = Color.BG_CARD,
        **kwargs,
    ) -> None:
        super().__init__(master, fg_color=fg_color, **kwargs)
        self.extractCode = extractCode

        self.buttonDnD = Button(
            master=self,
            text=self.BUTTON_DND_TEXT,
            image=self.DRAG_AND_DROP_IMAGE,
            width=700,
            height=200,
            textColor=Color.TEXT_GRAY,
            fg_color=Color.BG_BUTON_DND,
            hover_color=Color.BG_BUTON_DND,
            command=self.selectImage,
        )
        CTkToolTip(self.buttonDnD, delay=0.3, message=self.BUTTON_DND_TEXT)

        self.pathFrame = CTkFrame(master=self, fg_color="transparent")
        self.pathEntry = InputLabel(master=self.pathFrame, label="", state="readonly", width=450, bgColor=Color.BG_CARD)
        self.extractButton = Button(
            master=self.pathFrame,
            text="Extract Code",
            width=90,
            height=20,
            image=self.EXTRACT_IMAGE,
            textColor=Color.WHITE,
            fg_color=Color.BG_ACTIVE_BUTTON_NAVIGATION,
            hover_color=Color.BG_HOVER_BUTTON_NAVIGATION,
            command=lambda: self.extractCode(self.pathEntry.getValue()),
        )
        CTkToolTip(self.extractButton, delay=0.3, message="Extract Code")

        self.resetPathButton = Button(
            master=self.pathFrame,
            text="",
            width=20,
            height=15,
            image=self.DELETE_IMAGE,
            fg_color=Color.BG_CARD,
            hover_color=Color.BG_BUTON_DND,
            command=self.resetPath,
        )
        CTkToolTip(self.resetPathButton, delay=0.3, message="Reset Image")

        self.render()
        self.buttonDnD.drop_target_register(DND_FILES)
        self.buttonDnD.dnd_bind("<<Drop>>", self.getPath)

    def render(self) -> None:
        # self.pack(pady=15, ipadx=8, ipady=4)
        Separator(self, height=8).pack()
        self.buttonDnD.pack()
        Separator(self, height=8).pack()
        self.pathEntry.pack(padx=8, side="left", expand=True)
        self.extractButton.pack(side="left", expand=True)
        self.resetPathButton.pack(padx=8, side="left", expand=True)

    def displayPathFrame(self) -> None:
        self.pathFrame.pack()

    def hidePathFrame(self) -> None:
        self.pathFrame.pack_forget()

    def getPath(self, event: Any) -> None:
        if not event.data or not Validator.validateImagePath(event.data):
            return
        self.pathEntry.setState("normal")
        self.pathEntry.clear()
        self.pathEntry.setValue(event.data)
        self.pathEntry.setState("readonly")
        self.displayPathFrame()
        self.buttonDnD.configure(text="", image=Image(event.data, size=(600, 200), external=True))

    def selectImage(self) -> None:
        path = filedialog.askopenfilename(
            initialdir="C:/Users/ABDISOUBANEH/Downloads",
            title="Select file",
            filetypes=(("all files", "*.*"), ("text files", "*.txt")),
        )
        if not path or not Validator.validateImagePath(path):
            return
        self.pathEntry.setState("normal")
        self.pathEntry.setValue(path)
        self.pathEntry.setState("readonly")
        self.displayPathFrame()
        self.buttonDnD.configure(text="", image=Image(path, size=(600, 200), external=True))

    def resetPath(self) -> None:
        self.buttonDnD.configure(text=self.BUTTON_DND_TEXT, image=Image(self.DRAG_AND_DROP_IMAGE))
        self.pathFrame.pack_forget()
        self.pathEntry.setState("normal")
        self.pathEntry.clear()
        self.pathEntry.setState("readonly")
