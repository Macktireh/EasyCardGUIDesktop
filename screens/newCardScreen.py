import contextlib
from threading import Thread
from tkinter import messagebox
from typing import List

from customtkinter import CTkBaseClass, CTkFrame

from components import AddCardForm, Dialog, DragAndDrop, Loader
from components.ui import Button
from config.settings import LIST_CARD_TYPES, AssetsImages, Color, imagesTupple
from models.types import AllCreditCardDictIn, CreditCardDictIn
from services.creditCardService import CreditCardService


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

    def __init__(self, master: CTkBaseClass, creditCardService: CreditCardService) -> None:
        self.master = master
        self.creditCardService = creditCardService

        super().__init__(
            self.master,
            width=self.master._current_width,
            height=self.master._current_height,
            fg_color=Color.TRANSPARENT,
            corner_radius=0,
        )

        self.dnd = DragAndDrop(self, self.extractCode)
        self.dnd.place(relx=0.1, rely=0.025, relwidth=0.8, relheight=0.37)
        # self.dnd.place(relx=0.5, y=160, relwidth=0.8, relheight=0.37, anchor="center")
        # self.dnd.pack(pady=15, ipadx=8, ipady=4)

        self.form = AddCardForm(self, height=305)

        self.frame = CTkFrame(self, fg_color=Color.TRANSPARENT, height=40)
        # self.frame.place(relx=0.1, rely=0.9, relwidth=0.8)

        self.cancelButton = Button(
            self.frame,
            text="Cancel",
            fontSize=15,
            textColor=Color.WHITE,
            fg_color=Color.BG_ACTIVE_BUTTON_NAVIGATION,
            hover_color=Color.BG_HOVER_BUTTON_NAVIGATION,
            width=60,
            height=40,
            command=self.handleCancel,
        )
        self.cancelButton.place(relx=0.0, rely=0.005, relwidth=0.495)

        self.saveButton = Button(
            self.frame,
            text="Save",
            fontSize=15,
            textColor=Color.WHITE,
            fg_color=Color.BG_ACTIVE_BUTTON_NAVIGATION,
            hover_color=Color.BG_HOVER_BUTTON_NAVIGATION,
            width=60,
            height=40,
            command=self.saveAllCards,
        )
        self.saveButton.place(relx=0.505, rely=0.005, relwidth=0.495)

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
        self.addButton.place(relx=0.93, rely=0.91)

    def extractCode(self, path) -> None:
        loader = Loader(self)
        loader.show()

        def _func(self: NewCardScreen, loader: Loader) -> None:
            try:
                response, _ = self.creditCardService.extractCreditCard(path, callback=self.master.checkAuthentication)

                if response.is_error:
                    self.master.notify.show(
                        text=response.json().get("message") or "Failed to extract cards", fg_color=Color.RED
                    )
                    return

                data = response.json()

                if len(self.cardNumbers) == 0:
                    self.form.place(relx=0.1, rely=0.42, relwidth=0.8, relheight=0.46)
                    self.frame.place(relx=0.1, rely=0.91, relwidth=0.8)
                    self.cardNumbers = data["cardNumbers"]
                    self.form.render(self.cardNumbers)
                else:
                    self.cardNumbers = data["cardNumbers"]
                    self.form.updateRender(self.cardNumbers)

                self.master.notify.show(text="extracted cards successfully", fg_color=Color.GREEN)
            except Exception:
                self.master.notify.show(text="Failed to extract cards", fg_color=Color.RED)
            finally:
                with contextlib.suppress(Exception):
                    loader.hide() if loader else None

        Thread(
            target=_func,
            args=(
                self,
                loader,
            ),
        ).start()

    def onDelete(self, code: str) -> None:
        self.cardNumbers = [x for x in self.cardNumbers if x != code]
        if len(self.cardNumbers) < 1:
            self.form.place_forget()
            self.frame.place_forget()

    def handleAddCard(self) -> None:
        dialog = Dialog(text="Code :", title="New card", dropdown_values=LIST_CARD_TYPES)
        data = dialog.get_input()

        loader = Loader(self)
        loader.show()

        def _func(self: NewCardScreen, loader: Loader) -> None:
            try:
                payload = CreditCardDictIn(code=data["code"], cardType=data["type"].replace(" FDJ", ""))
                response, _ = self.creditCardService.addCreditCard(payload)
                if response.is_success:
                    self.master.notify.show(text="Card saved successfully")
                else:
                    msg = response.json().get("message", "Failed to save card")
                    if "errors" in response.json():
                        msg += "\n" + "\n".join(response.json()["errors"].values())
                    messagebox.showerror(title="Error", message=msg)
            except Exception:
                self.master.notify.show(text="Failed to save card", fg_color=Color.RED)
            finally:
                with contextlib.suppress(Exception):
                    loader.hide() if loader else None

        Thread(
            target=_func,
            args=(
                self,
                loader,
            ),
        ).start()

    def saveAllCards(self) -> None:
        loader = Loader(self)
        loader.show()

        def _func(self: NewCardScreen, loader: Loader) -> None:
            try:
                data = AllCreditCardDictIn(cards=self.form.getFormsData())

                response, _ = self.creditCardService.addAllCreditCards(data)
                if response.is_success:
                    self.form.deleteAllForms()
                    self.master.notify.show(text="Cards saved successfully")
                else:
                    msg = response.json().get("message", "Failed to save cards")
                    if "errors" in response.json():
                        msg += "\n" + "\n".join(response.json()["errors"].values())
                    messagebox.showerror(title="Error", message=msg)
            except Exception:
                # messagebox.showerror(title="Error", message="Failed to save cards")
                self.master.notify.show(text="Failed to save cards", fg_color=Color.RED)
            finally:
                with contextlib.suppress(Exception):
                    loader.hide() if loader else None

        Thread(
            target=_func,
            args=(
                self,
                loader,
            ),
        ).start()

    def handleCancel(self) -> None:
        self.form.deleteAllForms()
