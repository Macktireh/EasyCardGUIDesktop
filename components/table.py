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
        style.theme_use("clam")

        # Configure the Treeview Colors
        style.configure(
            "Treeview.Heading",
            background=Color.BG_BUTTON_NAVIGATION[0],
            foreground="black",
            rowheight=35,
            fieldbackground="white",
            font=("Helvetica", 13, "bold"),
        )
        style.configure(
            "Treeview",
            background=Color.BG_CONTENT[0],
            foreground="black",
            rowheight=30,
            fieldbackground=Color.BG_CONTENT[0],
            font=("Helvetica", 11),
        )

        # Change Selected Color
        style.map("Treeview", background=[("selected", Color.BG_ACTIVE_BUTTON_NAVIGATION[1])])

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

        self.tv_All_Data.tag_configure("oddrow", background=Color.BG_ALT_TREEVIEW[0])
        self.tv_All_Data.tag_configure("evenrow", background=Color.BG_ALT_TREEVIEW[1])

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