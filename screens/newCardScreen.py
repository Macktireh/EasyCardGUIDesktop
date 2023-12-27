from typing import List

from customtkinter import CTkBaseClass, CTkFrame, CTkInputDialog

from components import AddCardForm, Dialog, DragAndDrop
from components.ui import Button
from config.settings import LIST_CARD_TYPES, AssetsImages, Color, imagesTupple
from models.types import CreditCardDictIn
from services.creditCardInterface import CreditCardInterface


class NewCardScreen(CTkFrame):
    cardNumbers: List[str] = []
    ADD_IMAGE = imagesTupple(
        light=AssetsImages.ADD_DARK,
        dark=AssetsImages.ADD_DARK,
    )
    SAVE_IMAGE = imagesTupple(
        light=AssetsImages.SAVE_DARK,
        dark=AssetsImages.SAVE_DARK,
    )

    def __init__(self, master: CTkBaseClass, creditCardService: CreditCardInterface) -> None:
        self.master = master
        self.creditCardService = creditCardService

        super().__init__(
            self.master,
            width=self.master._current_width,
            height=self.master._current_height,
            fg_color="transparent",
            corner_radius=0,
        )

        self.dnd = DragAndDrop(self, self.extractCode)
        self.dnd.pack(pady=15, ipadx=8, ipady=4)

        self.form = AddCardForm(self)

        self.frame = CTkFrame(self, fg_color="transparent")
        self.saveButton = Button(
            self.frame,
            text="Save",
            textColor=Color.WHITE,
            image=self.SAVE_IMAGE,
            fg_color=Color.BG_ACTIVE_BUTTON_NAVIGATION,
            hover_color=Color.BG_HOVER_BUTTON_NAVIGATION,
            width=60,
            height=40,
        )
        self.saveButton.pack()

        self.addButton = Button(
            self,
            text="",
            textColor=Color.WHITE,
            image=self.ADD_IMAGE,
            fg_color=Color.BG_ACTIVE_BUTTON_NAVIGATION,
            hover_color=Color.BG_HOVER_BUTTON_NAVIGATION,
            width=40,
            height=40,
            corner_radius=10,
            command=self.handleAddCard,
        )
        self.addButton.place(relx=0.95, rely=0.94, anchor="center")

    def extractCode(self, path) -> None:
        try:
            res = self.creditCardService.extractCreditCard(path)
            if res["status"] != "success" or len(res["cardNumbers"]) < 1:
                return

            if len(self.cardNumbers) < 1:
                self.form.pack(pady=10)
                self.frame.pack(pady=10)
                self.cardNumbers = res["cardNumbers"]
                self.form.render(res["cardNumbers"])
            else:
                self.cardNumbers = res["cardNumbers"]
                self.form.updateRender(res["cardNumbers"])
        except Exception:
            print(res)
            dialog = CTkInputDialog(text="Type in a number:", title="Test")
            print("Number:", dialog.get_input())

    def onDelete(self, code: str) -> None:
        self.cardNumbers = [x for x in self.cardNumbers if x != code]
        if len(self.cardNumbers) < 1:
            self.form.pack_forget()
            self.frame.pack_forget()

    def handleAddCard(self) -> None:
        dialog = Dialog(text="Code :", title="New card", dropdown_values=LIST_CARD_TYPES)
        data = dialog.get_input()
        if data["code"] and data["type"]:
            self.creditCardService.addCreditCard(CreditCardDictIn(code=data["code"], cardType=data["type"]))
            # self.cardNumbers.append(data["code"])
            # self.form.pack(pady=10)
            # self.frame.pack(pady=10)
            # self.form.add(CreditCardDictIn(code=data["code"], cardType=data["type"]))
