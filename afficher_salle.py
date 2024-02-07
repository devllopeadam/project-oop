import json
import customtkinter as ctk
from tkinter import ttk

ctk.set_appearance_mode("light")

from salle import Salle


class AfficherSalle(ctk.CTk):
    font = "Verdana"
    color = "#1d3557"

    def __init__(self):
        super().__init__()
        self.title("Afficher Salle")
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
            columns=("idSalle", "libelle", "numero"),
            style="Custom.Treeview",
            show="headings",
        )
        table.heading("idSalle", text="id Salle")
        table.heading("libelle", text="Libelle")
        table.heading("numero", text="Numero")

        table.column("idSalle", anchor="center")
        table.column("libelle", anchor="center")
        table.column("numero", anchor="center")
        table.pack(fill="both", expand=True)

        for i in self.get_data_from_json():
            table.insert(parent="", index="end", values=list(i.values()))

    def check_delete(self):
        final = []
        ids = [i["idSalle"] for i in self.get_data_from_json()]

        if value_idSalle.get() == "" or value_idSalle.get() == "entre votre idSalle":
            error_idSalle.configure(text="cannot be empty")
            error_idSalle.place(x=150, y=25)
        elif value_idSalle.get() not in ids:
            error_idSalle.configure(text="idSalle not found")
            error_idSalle.place(x=150, y=25)
        elif value_idSalle.get() in ids:
            error_idSalle.place_forget()
            Salle.supprimerSalle(value_idSalle.get())
            table.delete(*table.get_children())
            for i in self.get_data_from_json():
                table.insert(parent="", index="end", values=list(i.values()))

    def modification(self):
        final = []
        ids = [i["idSalle"] for i in self.get_data_from_json()]
        newId = value_newId.get()
        libelle = value_libelle.get()
        numero = value_numero.get()
        arI = []
        for i in self.get_data_from_json():
            if i["idSalle"] != value_idSalle_modi.get():
                arI.append(i["idSalle"])

        if (
            value_idSalle_modi.get() == ""
            or value_idSalle_modi.get() == "entre votre idSalle"
        ):
            error_idSalle_modi.place(x=150, y=174)
        elif value_idSalle_modi.get() not in ids:
            error_idSalle_modi.configure("is not found")
            error_idSalle_modi.place(x=148, y=174)
        elif value_idSalle_modi.get() in ids:

            # for the newidSalle
            if newId == "" or newId == "entre votre idSalle":
                error_newId.configure(text="cannot be empty")
                error_newId.place(x=150, y=250)
            elif newId in arI:
                error_newId.configure(text="always exist")
                error_newId.place(x=175, y=250)
            elif newId not in arI:
                error_newId.place_forget()
                final.append(newId)

            # for the libelle
            if libelle == "" or libelle == "entre votre libelle":
                error_libelle.place(x=150, y=325)
            else:
                error_libelle.place_forget()
                final.append(libelle)
            # for the numero

            if numero == "" or numero == "entre votre numero":
                error_numero.place(x=150, y=402)
            else:
                error_numero.place_forget()
                final.append(numero)

            try:
                Salle.mofidierSalle(
                    value_idSalle_modi.get(), final[0], final[1], final[2]
                )
                table.delete(*table.get_children())
                for i in self.get_data_from_json():
                    table.insert(parent="", index="end", values=list(i.values()))
            except:
                print("error on the final list")

            error_idSalle_modi.place_forget()

    def filter_delete_bar(self):
        frame = ctk.CTkFrame(
            self,
            fg_color="#f8f8f8",
            bg_color="#f8f8f8",
            corner_radius=0,
        )
        frame.place(relwidth=0.27, relheight=1, relx=0.73)

        # for the delete salle
        global value_idSalle
        value_idSalle = ctk.StringVar()
        entry_idSalle = ctk.CTkEntry(
            frame,
            width=200,
            height=35,
            font=(self.font, 13),
            textvariable=value_idSalle,
        )
        global error_idSalle
        error_idSalle = ctk.CTkLabel(
            frame,
            text="idSalle not found",
            text_color="#FF0033",
            height=5,
        )
        # for the delete button
        button_idSalle = ctk.CTkButton(
            frame,
            text="Supprimer",
            font=(self.font, 15),
            fg_color="red",
            text_color="white",
            height=38,
            hover_color="#f53737",
            command=self.check_delete,
        )
        button_idSalle.configure(cursor="hand2")
        error_idSalle.place_forget()
        entry_idSalle.insert(index=ctk.END, string="entre votre idSalle")
        entry_idSalle.pack(pady=40)
        button_idSalle.pack()
        # for the modification entries etc...

        # for the idSalle

        global value_idSalle_modi
        value_idSalle_modi = ctk.StringVar()
        entry_idSalle_modi = ctk.CTkEntry(
            frame,
            width=200,
            height=35,
            font=(self.font, 13),
            textvariable=value_idSalle_modi,
        )
        global error_idSalle_modi
        error_idSalle_modi = ctk.CTkLabel(
            frame,
            text="idSalle not found",
            text_color="#FF0033",
            height=5,
        )

        error_idSalle_modi.place_forget()
        entry_idSalle_modi.insert(index=ctk.END, string="entre votre idSalle")
        entry_idSalle_modi.pack(pady=40)

        # for the new idSalle

        global value_newId
        value_newId = ctk.StringVar()
        entry_newId = ctk.CTkEntry(
            frame,
            width=200,
            height=35,
            font=(self.font, 13),
            textvariable=value_newId,
        )
        global error_newId
        error_newId = ctk.CTkLabel(
            frame,
            text="idSalle not found",
            text_color="#FF0033",
            height=5,
        )

        error_newId.place_forget()
        entry_newId.insert(index=ctk.END, string="entre votre idSalle")
        entry_newId.pack()

        # for the libelle

        global value_libelle
        value_libelle = ctk.StringVar()
        entry_libelle = ctk.CTkEntry(
            frame,
            width=200,
            height=35,
            font=(self.font, 13),
            textvariable=value_libelle,
        )
        global error_libelle
        error_libelle = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            height=5,
        )

        error_libelle.place_forget()
        entry_libelle.insert(index=ctk.END, string="entre votre libelle")
        entry_libelle.pack(pady=40)

        # for the new numero

        global value_numero
        value_numero = ctk.StringVar()
        entry_numero = ctk.CTkEntry(
            frame,
            width=200,
            height=35,
            font=(self.font, 13),
            textvariable=value_numero,
        )
        global error_numero
        error_numero = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            height=5,
        )

        error_numero.place_forget()
        entry_numero.insert(index=ctk.END, string="entre votre numero")
        entry_numero.pack()

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
        button_modification.pack(pady=20)

    def get_data_from_json(self):
        with open("./data.json", "r") as f:
            return json.load(f)["salles"]
