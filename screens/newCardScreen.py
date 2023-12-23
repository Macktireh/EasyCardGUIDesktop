from typing import List

from customtkinter import CTkBaseClass, CTkFrame

from components.addCardForm import AddCardForm
from components.dragAndDrop import DragAndDrop
from services.creditCardInterface import CreditCardInterface


class NewCardScreen(CTkFrame):
    cardNumbers: List[str]

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
        self.form.pack(pady=15)
    
    def extractCode(self, path) -> None:
        res = self.creditCardService.extractCreditCard(path)
        self.form.inputCode.setValue(res["cardNumbers"][0])
        self.cardNumbers = res["cardNumbers"]

        