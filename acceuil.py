import customtkinter as ctk
from tkinter import ttk
import json
from seance import Seance
from afficher_utilisateur import AfficherUtilisateur
from afficher_professeur import AfficherProfesseur
from afficher_salle import AfficherSalle
from afficher_matiere import AfficherMatiere
from ajouter_utilisateur import AjouterUtilisateur
from ajouter_professeur import AjouterProfesseur
from ajouter_salle import AjouterSalle
from ajouter_matiere import AjouterMatiere
from ajouter_seance import AjouterSeance


ctk.set_appearance_mode("light")


class Home(ctk.CTk):
    font = "Verdana"
    color = "#1d3557"

    def __init__(self):
        super().__init__()
        self.title("Acceuil")
        self.geometry("1470x750+40+15")
        self.resizable(False, False)
        self.iconbitmap("./images/home_icon.ico")
        self.create_control_panel_frame()
        self.create_treeview()
        self.get_data_from_json()
        self.create_action_panel()
        self.create_filter_bar()

    def create_control_panel_frame(self):
        frame = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
        frame.place(x=0, y=0, relheight=1, relwidth=0.2)

        def create_button(values):
            return ctk.CTkComboBox(
                frame,
                values=values,
                fg_color=Home.color,
                font=(Home.font, 15),
                text_color="white",
                button_color=Home.color,
                border_color=Home.color,
                button_hover_color="#274063",
                width=210,
                height=40,
                dropdown_font=(Home.font, 15),
                dropdown_text_color="white",
                dropdown_fg_color=Home.color,
                dropdown_hover_color="#274063",
                command=self.close_current_window,
            )

        # Gestion Utilisateur
        gestion_utilisateur_button = create_button(
            ["Ajouter Utilisateur", "Afficher Utilisateurs"]
        )
        gestion_utilisateur_button.set("Gestion Utilisateur")
        gestion_utilisateur_button.pack(padx=20, pady=20)

        # Gestion Personne
        gestion_personne_button = create_button(
            [
                "Ajouter Apprenant",
                "Afficher Apprenant",
                "Ajouter Professeur",
                "Afficher Professeur",
                "Ajouter Responsable",
                "Afficher Responsable",
            ]
        )
        gestion_personne_button.set("Gestion Personne")
        gestion_personne_button.pack(padx=20, pady=20)

        # Gestion des Matieres
        gestion_matieres_button = create_button(["Ajouter matière", "Afficher matière"])
        gestion_matieres_button.set("Gestion matières")
        gestion_matieres_button.pack(pady=20, padx=20)

        # Gestion des salles
        gestion_salle_button = create_button(["Ajouter salle", "Afficher salles"])
        gestion_salle_button.pack(pady=20, padx=20)
        gestion_salle_button.set("Gestion salles")

        # Gestion des seances
        gestion_seances_button = create_button(["Ajouter séance", "Afficher séance"])
        gestion_seances_button.pack(pady=20, padx=20)
        gestion_seances_button.set("Gestion séances")

        # The quit

        quit_button = ctk.CTkButton(
            frame,
            text="Quit",
            text_color="white",
            fg_color="#FF3333",
            hover_color="#ff4848",
            font=(Home.font, 15),
            width=210,
            height=40,
            command=lambda: self.destroy(),
        )
        quit_button.place(x=33, rely=0.911)
        quit_button.configure(cursor="hand2")

    def create_treeview(self):
        frame = ctk.CTkFrame(self, corner_radius=0)
        frame.place(relx=0.2, y=91, relheight=0.88, relwidth=0.64)
        style = ttk.Style()
        style.configure(
            "Treeview.Heading",
            font=(Home.font, 14, "normal"),
            fg_color="red",
            padding=(10, 10),
        )
        style.configure(
            "Custom.Treeview",
            font=(Home.font, 14, "normal"),
            foreground=Home.color,
            background="#f8f8f8",
            rowheight=37,
            anchor="center",
            borderwidth=0,
            relief="flat",
        )
        global table
        table = ttk.Treeview(
            frame,
            columns=(
                "idSeance",
                "professeur",
                "matiere",
                "salle",
                "dateSeance",
            ),
            style="Custom.Treeview",
            show="headings",
        )

        table.column("idSeance", width=120, anchor="center")
        table.column("dateSeance", width=120, anchor="center")
        table.column("professeur", anchor="center", width=140)
        table.column("matiere", anchor="center", width=110)
        table.column("dateSeance", anchor="center")
        table.column("salle", anchor="center", width=100)

        table.heading("idSeance", text="Id Seance")
        table.heading("professeur", text="Professeur matricule")
        table.heading("matiere", text="Matiere id")
        table.heading("salle", text="Salle id")
        table.heading("dateSeance", text="Date Seance")

        table.pack(fill="both", expand=True)

        for i in self.get_data_from_json():
            table.insert(parent="", index="end", values=list(i.values()))

    def close_current_window(self, choice):
        if choice != "":
            self.destroy()
        if choice == "Ajouter Utilisateur":
            AjouterUtilisateur().mainloop()
        elif choice == "Ajouter Professeur":
            AjouterProfesseur().mainloop()
        elif choice == "Ajouter salle":
            AjouterSalle().mainloop()
        elif choice == "Ajouter matière":
            AjouterMatiere().mainloop()
        elif choice == "Ajouter séance":
            AjouterSeance().mainloop()
        elif choice == "Afficher Utilisateurs":
            AfficherUtilisateur().mainloop()
        elif choice == "Afficher Professeur":
            AfficherProfesseur().mainloop()
        elif choice == "Afficher salles":
            AfficherSalle().mainloop()
        elif choice == "Afficher séance":
            AfficherMatiere().mainloop()

    def get_data_entry_check(self):
        value = value_entry_del.get()
        aridSeance = [i["idSeance"] for i in self.get_data_from_json()]
        if value in aridSeance:
            Seance.supprimerSeance(value)
            error.place_forget()
            table.delete(*table.get_children())
            for i in self.get_data_from_json():
                table.insert(parent="", index="end", values=list(i.values()))
        else:
            error.place(relx=0.5, y=110, anchor="center")

    def modification(self):
        final = []
        aridSeance = [i["idSeance"] for i in self.get_data_from_json()]
        arI = []
        for i in self.get_data_from_json():
            if i["idSeance"] != value_entry_mod.get():
                arI.append(i["idSeance"])
        newId = value_entry_idSeance.get()
        newPro = value_entry_professeur.get()
        newMatiere = value_entry_matiere.get()
        newSalle = value_entry_salle.get()
        newDate = value_entry_date.get()
        sals = [i["idSalle"] for i in self.get_data("salles")]
        mats = [i["idMatiere"] for i in self.get_data("matieres")]
        pro = [i["matricule"] for i in self.get_data("professeurs")]

        if value_entry_mod.get() in aridSeance:
            error_mod.place_forget()
            # For the new id checking
            if newId == "nouveau id" or newId == "" or newId in arI:
                error_id.place(relx=0.5, anchor="center", y=325)
            else:
                error_id.place_forget()
                final.append(newId)
            # For the new pro checking
            if newPro == "nouveau matricule pro" or newPro == "" or newPro not in pro:
                error_professeur.place(relx=0.5, anchor="center", y=380)
            elif newPro in pro:
                error_professeur.place_forget()
                final.append(
                    {
                        "nom": "biba",
                        "prenom": "khawa",
                        "cin": "adlfk",
                        "filiere": "adfas",
                        "matricule": newPro,
                    }
                )

            # For the new matiere checking

            if (
                newMatiere == "nouvelle matiere"
                or newMatiere == ""
                or newMatiere not in mats
            ):
                error_matiere.place(relx=0.5, anchor="center", y=439)
            elif newMatiere in mats:
                error_matiere.place_forget()
                final.append(
                    {
                        "idMatiere": newMatiere,
                        "libelle": "pour la langue francaise",
                        "langue": "Francais",
                    }
                )

            # For the new Salle

            if newSalle == "nouvelle salle" or newSalle == "" or newSalle not in sals:
                error_salle.place(relx=0.5, anchor="center", y=495)
            elif newSalle in sals:
                error_salle.place_forget()
                final.append(
                    {"idSalle": newSalle, "libelle": "libelle", "numero": "numero"}
                )

            # For the data and the afficher salle dispo function
            state = Seance.afficherSalleDispo(newSalle, newDate)
            if newDate == "nouvelle date" or newSalle == "" or state == True:
                error_date.place(relx=0.5, anchor="center", y=550)
            elif state == False:
                error_date.place_forget()
                final.append(newDate)

            try:
                Seance.modifierSeance(
                    value_entry_mod.get(),
                    final[0],
                    final[1],
                    final[2],
                    final[3],
                    final[4],
                )
                table.delete(*table.get_children())
                for i in self.get_data_from_json():
                    table.insert(parent="", index="end", values=list(i.values()))
            except:
                print("final list error")
        else:
            error_mod.place(relx=0.5, y=260, anchor="center")

    def create_action_panel(self):
        # for the frame
        frame = ctk.CTkFrame(self, corner_radius=0, fg_color="white")
        frame.place(relx=0.84, y=91, relheight=0.88, relwidth=0.16)
        frame_title = ctk.CTkLabel(
            frame, text="Action", font=(Home.font, 15), text_color=Home.color
        )
        frame_title.pack()
        # Delete and entry button
        del_button = ctk.CTkButton(
            frame,
            text="Supprimer",
            font=(Home.font, 15),
            fg_color="red",
            text_color="white",
            height=35,
            hover_color="#f53737",
            command=lambda: self.get_data_entry_check(),
        )
        del_button.configure(cursor="hand2")
        del_button.pack(pady=20)
        global value_entry_del
        value_entry_del = ctk.StringVar()
        entry_del = ctk.CTkEntry(
            frame,
            placeholder_text="Entrer id seance",
            width=170,
            height=35,
            font=(Home.font, 13),
            textvariable=value_entry_del,
        )
        entry_del.pack(pady=20)
        entry_del.insert(ctk.END, "Entrer id seance")
        global error
        error = ctk.CTkLabel(
            frame,
            text="idSeance not found",
            text_color="#FF0033",
            height=20,
            font=(Home.font, 11),
        )
        error.place_forget()
        # modification button
        modi_button = ctk.CTkButton(
            frame,
            text="Modifier",
            font=(Home.font, 15),
            fg_color="#26D782",
            text_color="white",
            height=35,
            hover_color="#2ee28b",
            command=self.modification,
        )
        global value_entry_mod
        value_entry_mod = ctk.StringVar()

        entry_mod = ctk.CTkEntry(
            frame,
            placeholder_text="Entrer id seance",
            width=170,
            height=35,
            font=(Home.font, 13),
            textvariable=value_entry_mod,
        )
        global error_mod
        error_mod = ctk.CTkLabel(
            frame,
            text="id not found",
            text_color="#FF0033",
            height=20,
            font=(Home.font, 11),
        )

        modi_button.pack(pady=20)
        error_mod.place_forget()
        entry_mod.insert(ctk.END, "Entrer id seance")
        entry_mod.pack(pady=20)

        # start other entries for modifying the seance
        # entry for new id
        global value_entry_idSeance
        value_entry_idSeance = ctk.StringVar()
        global entry_idSeance
        entry_idSeance = ctk.CTkEntry(
            frame,
            width=170,
            height=35,
            font=(Home.font, 13),
            textvariable=value_entry_idSeance,
        )
        global error_id
        error_id = ctk.CTkLabel(
            frame,
            text="id always exist",
            text_color="#FF0033",
            height=20,
            font=(Home.font, 11),
        )
        error_id.place_forget()
        entry_idSeance.insert(index=ctk.END, string="nouveau id")
        entry_idSeance.pack(pady=10)
        # entry for new professeur
        global value_entry_professeur
        value_entry_professeur = ctk.StringVar()
        global entry_professeur
        entry_professeur = ctk.CTkEntry(
            frame,
            width=170,
            height=35,
            font=(Home.font, 13),
            textvariable=value_entry_professeur,
        )
        entry_professeur.insert(index=ctk.END, string="nouveau matricule pro")
        global error_professeur
        error_professeur = ctk.CTkLabel(
            frame,
            text="Professeur not found",
            text_color="#FF0033",
            height=15,
            font=(Home.font, 11),
        )
        error_professeur.place_forget()
        entry_professeur.pack(pady=10)

        # entry for new matiere
        global value_entry_matiere
        value_entry_matiere = ctk.StringVar()
        global entry_matiere
        entry_matiere = ctk.CTkEntry(
            frame,
            width=170,
            height=35,
            font=(Home.font, 13),
            textvariable=value_entry_matiere,
        )
        entry_matiere.insert(index=ctk.END, string="nouvelle matiere")
        global error_matiere
        error_matiere = ctk.CTkLabel(
            frame,
            text="Matiere not found",
            text_color="#FF0033",
            height=20,
            font=(Home.font, 11),
        )
        error_matiere.place_forget()
        entry_matiere.pack(pady=10)

        # Entry for salle
        global value_entry_salle
        value_entry_salle = ctk.StringVar()
        global entry_salle
        entry_salle = ctk.CTkEntry(
            frame,
            width=170,
            height=35,
            font=(Home.font, 13),
            textvariable=value_entry_salle,
        )
        entry_salle.insert(index=ctk.END, string="nouvelle salle")
        global error_salle
        error_salle = ctk.CTkLabel(
            frame,
            text="salle not found",
            text_color="#FF0033",
            height=20,
            font=(Home.font, 11),
        )
        error_salle.place_forget()
        entry_salle.pack(pady=10)

        # entry for date
        global value_entry_date
        value_entry_date = ctk.StringVar()
        global entry_date
        entry_date = ctk.CTkEntry(
            frame,
            width=170,
            height=35,
            font=(Home.font, 13),
            textvariable=value_entry_date,
        )
        entry_date.insert(index=ctk.END, string="nouvelle date")
        global error_date
        error_date = ctk.CTkLabel(
            frame,
            text="date not dispo",
            text_color="#FF0033",
            height=20,
            font=(Home.font, 11),
        )
        error_date.place_forget()
        entry_date.pack(pady=10)

    def get_data_filter(self):
        value = value_entry_filter.get()
        pro = [i["professeur"] for i in self.get_data_from_json()]
        if value == "Entrer votre matricule" or value == "" or value not in pro:
            error_filter.place(x=425, anchor="center", y=20)
            table.delete(*table.get_children())
            for i in self.get_data_from_json():
                table.insert(parent="", index="end", values=list(i.values()))
        elif value in pro:
            table.delete(*table.get_children())
            for i in Seance.afficherSeanceProfesseur(value):
                table.insert(parent="", index="end", values=list(i.values()))
            error_filter.place_forget()

    def create_filter_bar(self):
        frame_bar = ctk.CTkFrame(
            self,
            width=400,
            height=91,
            fg_color="#f8f8f8",
            bg_color="#f8f8f8",
            corner_radius=0,
        )
        frame_bar.place(relx=0.2, y=1, relwidth=0.8)
        global value_entry_filter
        value_entry_filter = ctk.StringVar()
        entry_filter = ctk.CTkEntry(
            frame_bar,
            text_color=Home.color,
            font=(Home.font, 14),
            fg_color="#f8f8f8",
            height=35,
            width=300,
            textvariable=value_entry_filter,
        )
        entry_filter.place(y=30, x=280)
        entry_filter.insert(index=ctk.END, string="Entrer votre matricule")
        button_filter = ctk.CTkButton(
            frame_bar,
            text="Chercher par matricule professeur",
            fg_color=Home.color,
            font=(Home.font, 15),
            bg_color="#f8f8f8",
            height=35,
            hover_color="#253f64",
            command=self.get_data_filter,
        )
        global error_filter
        error_filter = ctk.CTkLabel(
            frame_bar,
            text="Professeur matricule not found",
            text_color="#FF0033",
            height=15,
            font=(Home.font, 11),
        )
        error_filter.place_forget()
        button_filter.place(y=30, x=600)
        button_filter.configure(cursor="hand2")

    def get_data_from_json(self):
        with open("./data.json", "r") as f:
            return json.load(f)["seances"]

    def get_data(self, value):
        with open("./data.json", "r") as f:
            return json.load(f)[value]


# Home().mainloop()
