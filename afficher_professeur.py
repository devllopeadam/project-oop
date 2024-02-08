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
        final = []
        valueCin = value_old_cin.get()
        valueNom = value_nom.get()
        valuePrenom = value_prenom.get()
        newCin = value_new_cin.get()
        valueFiliere = value_filiere.get()
        valueMatricule = value_matricule.get()
        cins = [i["cin"] for i in self.get_data_from_json()]
        arP = []
        arC = []
        for i in self.get_data_from_json():
            if i["cin"] != valueCin:
                arC.append(i["cin"])
        for i in self.get_data_from_json():
            if i["cin"] != valueCin:
                arP.append(i["matricule"])

        if valueCin == "" or valueCin == "entre votre cin":
            error_old_cin.configure(text="cannot be empty")
            error_old_cin.place(x=156, y=175)
        elif valueCin not in cins:
            error_old_cin.configure(text="cin not found")
            error_old_cin.place(x=173, y=175)
        elif valueCin in cins:
            error_old_cin.place_forget()
            # for the new nom

            if valueNom == "" or valueNom == "entre votre nom":
                error_nom.place(x=156, y=250)
            else:
                error_nom.place_forget()
                final.append(valueNom)
            # for the new prenom
            if valuePrenom == "" or valuePrenom == "entre votre prenom":
                error_prenom.place(x=156, y=325)
            else:
                error_prenom.place_forget()
                final.append(valuePrenom)
            # for the new cin

            if newCin == "" or newCin == "entre votre cin":
                error_new_cin.place(x=156, y=405)
            elif newCin in arC:
                error_new_cin.configure(text="always exist")
                error_new_cin.place(x=175, y=400)
            elif newCin not in arC:
                error_new_cin.place_forget()
                final.append(newCin)
            # for the filiere

            if valueFiliere == "" or valueFiliere == "entre votre filiere":
                error_filiere.place(x=156, y=477)
            else:
                error_filiere.place_forget()
                final.append(valueFiliere)

            # for the matricule
            if valueMatricule == "" or valueMatricule == "entre votre matricule":
                error_matricule.place(x=155, y=550)
            elif valueMatricule in arP:
                error_matricule.configure(text="always exist")
                error_matricule.place(x=175, y=550)
            elif valueMatricule not in arP:
                error_matricule.place_forget()
                final.append(valueMatricule)

            try:
                Professeur.mofidierProfesseur(
                    valueCin, final[0], final[1], final[2], final[3], final[4]
                )
                table.delete(*table.get_children())
                for i in self.get_data_from_json():
                    table.insert(parent="", index="end", values=list(i.values()))
            except:
                print("final list error")

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

        # for the new nom
        global value_nom
        value_nom = ctk.StringVar()
        entry_nom = ctk.CTkEntry(
            frame, width=200, height=35, font=(self.font, 13), textvariable=value_nom
        )
        global error_nom
        error_nom = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            height=5,
        )
        error_nom.place_forget()
        entry_nom.insert(index=ctk.END, string="entre votre nom")
        entry_nom.pack()

        # for the prenom

        global value_prenom
        value_prenom = ctk.StringVar()
        entry_prenom = ctk.CTkEntry(
            frame, width=200, height=35, font=(self.font, 13), textvariable=value_prenom
        )
        global error_prenom
        error_prenom = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            height=5,
        )
        error_prenom.place_forget()
        entry_prenom.insert(index=ctk.END, string="entre votre prenom")
        entry_prenom.pack(pady=40)

        # for the cin

        global value_new_cin
        value_new_cin = ctk.StringVar()
        entry_cin = ctk.CTkEntry(
            frame,
            width=200,
            height=35,
            font=(self.font, 13),
            textvariable=value_new_cin,
        )
        global error_new_cin
        error_new_cin = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            height=5,
        )
        error_new_cin.place_forget()
        entry_cin.insert(index=ctk.END, string="entre votre cin")
        entry_cin.pack()
        # for the filiere

        global value_filiere
        value_filiere = ctk.StringVar()
        entry_filiere = ctk.CTkEntry(
            frame,
            width=200,
            height=35,
            font=(self.font, 13),
            textvariable=value_filiere,
        )
        global error_filiere
        error_filiere = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            height=5,
        )
        error_filiere.place_forget()
        entry_filiere.insert(index=ctk.END, string="entre votre filiere")
        entry_filiere.pack(pady=40)

        # for the matricule

        global value_matricule
        value_matricule = ctk.StringVar()
        entry_matricule = ctk.CTkEntry(
            frame,
            width=200,
            height=35,
            font=(self.font, 13),
            textvariable=value_matricule,
        )
        global error_matricule
        error_matricule = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            height=5,
        )
        error_matricule.place_forget()
        entry_matricule.insert(index=ctk.END, string="entre votre matricule")
        entry_matricule.pack()

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
        button_modification.pack(pady=20)

    def get_data_from_json(self):
        with open("./data.json", "r") as f:
            return json.load(f)["professeurs"]


# AfficherProfesseur().mainloop()
