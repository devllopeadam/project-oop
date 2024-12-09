import customtkinter as ctk
from tkinter import ttk
from pymongo import *

ctk.set_appearance_mode("light")

from classes.matiere import Matiere
client = MongoClient("mongodb://localhost:27017/")
db = client["center-formation"]
collection = db["matieres"]

class AfficherMatiere(ctk.CTk):
    font = "Verdana"
    color = "#1d3557"

    def __init__(self):
        super().__init__()
        self.title("Afficher Matiere")
        self.geometry("1080x750+250+15")
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
            columns=("idMatiere", "libelle", "langue"),
            style="Custom.Treeview",
            show="headings",
        )
        table.heading("idMatiere", text="id Matiere")
        table.heading("libelle", text="Libelle")
        table.heading("langue", text="Langue")
        table.column("idMatiere", anchor="center")
        table.column("libelle", anchor="center")
        table.column("langue", anchor="center")
        table.pack(fill="both", expand=True)

        for i in self.get_data_from_json():
            table.insert(parent="", index="end", values=list(i.values()))

    def check_delete(self):
        ids = [i["_id"] for i in self.get_data_from_json()]
        value = value_id.get()
        if value == "" or value == "entre votre id":
            error_id.configure(text="cannot be empty")
            error_id.place(x=153, y=21)
        elif value not in ids:
            error_id.configure(text="id not defind")
            error_id.place(x=170, y=21)
        elif value in ids:
            Matiere.supprimerMatiere(value)
            table.delete(*table.get_children())
            for i in self.get_data_from_json():
                table.insert(parent="", index="end", values=list(i.values()))
            error_id.place_forget()

    def modification(self):
        ids = [i["_id"] for i in self.get_data_from_json()]
        newId = value_entry_new_id.get()
        newLibelle = value_entry_new_libelle.get()
        newLangue = value_entry_new_langue.get()
        valueId = value_old_id.get()
        final = []
        arL = []

        for i in self.get_data_from_json():
            if i["_id"] != valueId:
                arL.append(i["_id"])

        if valueId == "" or valueId == "Entre votre id":
            error_old_id.configure(text="cannot be empty")
            error_old_id.place(x=153, y=175)
        elif valueId not in ids:
            error_old_id.configure(text="id not found")
            error_old_id.place(x=170, y=175)
        elif valueId in ids:
            # for the new login

            if newId == "" or newId == "new id":
                error_new_id.configure(text="cannot be empty")
                error_new_id.place(x=153, y=272)
            elif newId in arL:
                error_new_id.configure(text="always exist")
                error_new_id.place(x=170, y=272)
            elif newId not in arL:
                error_new_id.place_forget()
                final.append(newId)

            # for the new libelle

            if newLibelle == "" or newLibelle == "new libelle":
                error_new_libelle.configure(text="cannot be empty")
                error_new_libelle.place(x=153, y=345)
            else:
                error_new_libelle.place_forget()
                final.append(newLibelle)

            # for the new langue
            if newLangue == "" or newLangue == "new langue":
                error_new_langue.configure(text="cannot be empty")
                error_new_langue.place(x=153, y=420)
            else:
                error_new_langue.place_forget()
                final.append(newLangue)

            try:
                Matiere.mofidierMatiere(valueId, final[0], final[1], final[2])
                table.delete(*table.get_children())
                for i in self.get_data_from_json():
                    table.insert(parent="", index="end", values=list(i.values()))
            except:
                print("final is empty")

            error_old_id.place_forget()

    def filter_delete_bar(self):
        frame = ctk.CTkFrame(
            self,
            fg_color="#f8f8f8",
            bg_color="#f8f8f8",
            corner_radius=0,
        )
        frame.place(relwidth=0.27, relheight=1, relx=0.73)

        # for the delete utilisateur
        global value_id
        value_id = ctk.StringVar()
        entry_id = ctk.CTkEntry(
            frame, width=200, height=35, font=(self.font, 13), textvariable=value_id
        )
        global error_id
        error_id = ctk.CTkLabel(
            frame,
            text="id not found",
            text_color="#FF0033",
            height=5,
        )
        # for the delete button
        button_id = ctk.CTkButton(
            frame,
            text="Supprimer",
            font=(self.font, 15),
            fg_color="red",
            text_color="white",
            height=38,
            hover_color="#f53737",
            command=self.check_delete,
        )
        button_id.configure(cursor="hand2")
        error_id.place_forget()
        entry_id.insert(index=ctk.END, string="entre votre id")
        entry_id.pack(pady=40)
        button_id.pack()
        # for the modification entries etc...
        global value_old_id
        value_old_id = ctk.StringVar()
        entry_old_id = ctk.CTkEntry(
            frame,
            width=200,
            height=35,
            font=(self.font, 13),
            textvariable=value_old_id,
        )
        global error_old_id
        error_old_id = ctk.CTkLabel(
            frame,
            text="id not found",
            text_color="#FF0033",
            height=5,
        )
        error_old_id.place_forget()
        entry_old_id.pack(pady=40)
        entry_old_id.insert(index=ctk.END, string="Entre votre login")

        # for the new id
        global value_entry_new_id
        value_entry_new_id = ctk.StringVar()
        entry_new_id = ctk.CTkEntry(
            frame,
            width=200,
            height=35,
            font=(self.font, 13),
            textvariable=value_entry_new_id,
        )
        global error_new_id
        error_new_id = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            height=5,
        )
        error_new_id.place_forget()
        entry_new_id.insert(index=ctk.END, string="new id")
        entry_new_id.pack(pady=20)

        # for the new libelle

        global value_entry_new_libelle
        value_entry_new_libelle = ctk.StringVar()
        entry_new_libelle = ctk.CTkEntry(
            frame,
            width=200,
            height=35,
            font=(self.font, 13),
            textvariable=value_entry_new_libelle,
        )
        global error_new_libelle
        error_new_libelle = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            height=5,
        )
        error_new_libelle.place_forget()
        entry_new_libelle.insert(index=ctk.END, string="new libelle")
        entry_new_libelle.pack(pady=20)

        # for the new langue

        global value_entry_new_langue
        value_entry_new_langue = ctk.StringVar()
        entry_new_langue = ctk.CTkEntry(
            frame,
            width=200,
            height=35,
            font=(self.font, 13),
            textvariable=value_entry_new_langue,
        )
        global error_new_langue
        error_new_langue = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            height=5,
        )
        error_new_langue.place_forget()
        entry_new_langue.insert(index=ctk.END, string="new langue")
        entry_new_langue.pack(pady=20)

        # for the button modifiacation

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
        return list(collection.find())
