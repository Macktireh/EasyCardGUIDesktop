from numbers import Number
from tkinter import Scrollbar
from tkinter.ttk import Style, Treeview
from typing import List

from customtkinter import CTkFrame

from config.settings import Color


class Table(CTkFrame):
    def __init__(self, master, colums: List[str], rows: List[List[str | Number | None]]):
        self.master = master
        self.colums = colums
        self.rows = rows

        super().__init__(self.master)

        self.Table(self.colums, self.rows)
        
    def Table(self, colums: List[str], rows: List[List[str | Number | None]]):
        # Add Some Style
        style = Style()
        # style.theme_use("default")
    
        # style.configure("Treeview",
        #                 background="#2a2d2e",
        #                 foreground="white",
        #                 rowheight=25,
        #                 fieldbackground="#343638",
        #                 bordercolor="#343638",
        #                 borderwidth=0)
        # style.map('Treeview', background=[('selected', '#22559b')])

        # style.configure("Treeview.Heading",
        #                 background="#565b5e",
        #                 foreground="white",
        #                 relief="flat")
        # style.map("Treeview.Heading",
        #             background=[('active', '#3484F0')])

        # Pick A Theme
        style.theme_use("default")

        # Configure the Treeview Colors
        style.configure(
            "Treeview.Heading",
            background=Color.BG_ACTIVE_BUTTON_NAVIGATION[0] if self._get_appearance_mode() == "light" else Color.BG_ACTIVE_BUTTON_NAVIGATION[1],  # noqa: E501
            foreground=Color.WHITE,
            rowheight=25,
            fieldbackground=Color.BG_HOVER_BUTTON_NAVIGATION[0] if self._get_appearance_mode() == "light" else Color.BG_HOVER_BUTTON_NAVIGATION[1],  # noqa: E501
        )

        # Change Selected Color
        style.map("Treeview", background=[("selected", "#347083")])

        def clear_data():
            self.tv_All_Data.delete(*self.tv_All_Data.get_children())
            return None

        # frame1 = tk.LabelFrame(self.show_data, text=f"{path}")
        # frame1.place(height=420, width=768, rely=0.02, relx=0.02)

        self.tv_All_Data = Treeview(self)
        self.tv_All_Data.place(relheight=1, relwidth=1)

        # commande signifie mettre à jour la vue de l'axe y du widget
        treescrolly = Scrollbar(self, orient="vertical", command=self.tv_All_Data.yview)

        # commande signifie mettre à jour la vue axe x du widget
        treescrollx = Scrollbar(self, orient="horizontal", command=self.tv_All_Data.xview)

        # affecter les barres de défilement au widget Treeview
        self.tv_All_Data.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)

        # faire en sorte que la barre de défilement remplisse l'axe x du widget Treeview
        treescrollx.pack(side="bottom", fill="x")

        # faire en sorte que la barre de défilement remplisse l'axe y du widget Treeview
        treescrolly.pack(side="right", fill="y")

        global count
        count = 0

        # self.tv_All_Data.tag_configure("oddrow", background=Color.BG_CONTENT_SECONDARY[0] if self._get_appearance_mode() == "light" else Color.BG_CONTENT_SECONDARY[1])  # noqa: E501
        # self.tv_All_Data.tag_configure("evenrow", background=Color.BG_CARD[0] if self._get_appearance_mode() == "light" else Color.BG_CARD[1])  # noqa: E501

        # vider le treeview
        self.tv_All_Data.delete(*self.tv_All_Data.get_children())

        self.tv_All_Data["column"] = colums
        self.tv_All_Data["show"] = "headings"

        for column in self.tv_All_Data["columns"]:
            self.tv_All_Data.column(column, anchor="w")
            self.tv_All_Data.heading(column, anchor="w", text=column)

        # self.df_rows = df.to_numpy().tolist()

        # print()
        # print(self.df_rows)
        # print()

        for row in rows:
            if count % 2 == 0:
                self.tv_All_Data.insert(
                    "",
                    "end",
                    iid=count,
                    values=row,
                    tags=("evenrow",),
                )
            else:
                self.tv_All_Data.insert(
                    "",
                    "end",
                    iid=count,
                    values=row,
                    tags=("oddrow",),
                )
            count += 1
        self.tv_All_Data.insert("", "end", values="")