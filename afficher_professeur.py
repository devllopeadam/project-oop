import json
import customtkinter as ctk
from tkinter import ttk

ctk.set_appearance_mode("light")

from professeur import Professeur


class AfficherProfesseur(ctk.CTk):
    font = "Verdana"
    color = "#1d3557"

    def __init__(self):
        super().__init__()
        self.title("Afficher Professeur")
        self.geometry("1120x750+250+15")
        self.iconbitmap("./images/user_icon.ico")
        self.create_treeview()
        self.filter_delete_bar()

    def create_treeview(self):
        frame = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
        frame.place(x=0, y=0, relheight=1, relwidth=0.73)
        style = ttk.Style()
        style.configure(
            "Treeview.Heading",
            font=(self.font, 14, "normal"),
            fg_color="red",
            padding=(10, 10),
        )
        style.configure(
            "Custom.Treeview",
            font=(self.font, 14, "normal"),
            foreground=self.color,
            background="#f8f8f8",
            rowheight=37,
            anchor="center",
            borderwidth=0,
            relief="flat",
        )
        global table
        table = ttk.Treeview(
            frame,
            columns=("nom", "prenom", "cin", "filiere", "matricule"),
            style="Custom.Treeview",
            show="headings",
        )
        table.heading("nom", text="Nom")
        table.heading("prenom", text="Prenom")
        table.heading("cin", text="Cin")
        table.heading("filiere", text="Filiere")
        table.heading("matricule", text="Matricule")

        table.column("nom", anchor="center")
        table.column("prenom", anchor="center")
        table.column("cin", anchor="center")
        table.column("filiere", anchor="center")
        table.column("matricule", anchor="center")
        table.pack(fill="both", expand=True)

        for i in self.get_data_from_json():
            table.insert(parent="", index="end", values=list(i.values()))

    def check_delete(self):
        cins = [i["cin"] for i in self.get_data_from_json()]
        value = value_cin.get()
        if value == "" or value == "entre votre cin":
            error_cin.configure(text="cannot be empty")
            error_cin.place(x=153, y=21)
        elif value not in cins:
            error_cin.configure(text="cin not defind")
            error_cin.place(x=154, y=21)
        elif value in cins:
            Professeur.supprimerProfesseur(value)
            table.delete(*table.get_children())
            for i in self.get_data_from_json():
                table.insert(parent="", index="end", values=list(i.values()))
            error_cin.place_forget()

    def modification(self):
        # place(x=173, y=175)
        valueCin = value_old_cin.get()
        cins = [i["cin"] for i in self.get_data_from_json()]
        arC = []
        for i in self.get_data_from_json():
            if i["cin"] != valueCin:
                arC.append(i["cin"])

        if valueCin == "" or valueCin == "entre votre cin":
            error_old_cin.configure(text="cannot be empty")
            error_old_cin.place(x=156, y=175)
        elif valueCin not in cins:
            error_old_cin.configure(text="cin not found")
            error_old_cin.place(x=173, y=175)
        elif valueCin in cins:
            error_old_cin.place_forget()
            True

    def filter_delete_bar(self):
        frame = ctk.CTkFrame(
            self,
            fg_color="#f8f8f8",
            bg_color="#f8f8f8",
            corner_radius=0,
        )
        frame.place(relwidth=0.27, relheight=1, relx=0.73)

        # for the delete utilisateur
        global value_cin
        value_cin = ctk.StringVar()
        entry_cin = ctk.CTkEntry(
            frame, width=200, height=35, font=(self.font, 13), textvariable=value_cin
        )
        global error_cin
        error_cin = ctk.CTkLabel(
            frame,
            text="cin not found",
            text_color="#FF0033",
            height=5,
        )
        # for the delete button
        button_cin = ctk.CTkButton(
            frame,
            text="Supprimer",
            font=(self.font, 15),
            fg_color="red",
            text_color="white",
            height=38,
            hover_color="#f53737",
            command=self.check_delete,
        )
        button_cin.configure(cursor="hand2")
        error_cin.place_forget()
        entry_cin.insert(index=ctk.END, string="entre votre cin")
        entry_cin.pack(pady=40)
        button_cin.pack()

        # for the old cin
        global value_old_cin
        value_old_cin = ctk.StringVar()
        entry_old_cin = ctk.CTkEntry(
            frame,
            width=200,
            height=35,
            font=(self.font, 13),
            textvariable=value_old_cin,
        )
        global error_old_cin
        error_old_cin = ctk.CTkLabel(
            frame,
            text="cin not found",
            text_color="#FF0033",
            height=5,
        )
        error_old_cin.place_forget()
        entry_old_cin.pack(pady=40)
        entry_old_cin.insert(index=ctk.END, string="entre votre cin")
        # for the button modification

        button_modification = ctk.CTkButton(
            frame,
            text="Modifier",
            font=(self.font, 15),
            fg_color="#26D782",
            text_color="white",
            height=35,
            hover_color="#2ee28b",
            command=self.modification,
        )
        button_modification.pack()

    def get_data_from_json(self):
        with open("./data.json", "r") as f:
            return json.load(f)["professeurs"]


AfficherProfesseur().mainloop()
