import customtkinter as ctk
from tkinter import ttk
import json

ctk.set_appearance_mode("light")


class TestOne(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Test One")
        self.geometry("500x500")
        label = ctk.CTkLabel(self, text="jeniah adam").pack()


class TestTwo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Test Two")
        self.geometry("500x500")
        label = ctk.CTkLabel(self, text="jeniah adam").pack()


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
        gestion_salle_button = create_button(["Ajouter salle", "Affcher salles"])
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
        table.heading("professeur", text="Professeur")
        table.heading("matiere", text="Matiere")
        table.heading("salle", text="Salle")
        table.heading("dateSeance", text="Date Seance")

        table.pack(fill="both", expand=True)

        for i in self.get_data_from_json():
            table.insert(parent="", index="end", values=list(i.values()))

    def close_current_window(self, choice):
        value = choice
        print(value)
        if choice != "":
            self.destroy()
        # if choice == "Ajouter Utilisateur":
        #     # TestOne().mainloop()
        # elif choice == "Afficher Utilisateurs":
        #     # TestTwo().mainloop()

    def get_data_entry_check(self):
        value = value_entry_del.get()
        aridSeance = [i["idSeance"] for i in self.get_data_from_json()]
        if value in aridSeance:
            table.delete(*table.get_children())
            for i in self.get_data_from_json():
                table.insert(parent="", index="end", values=list(i.values()))
        else:
            error.place(relx=0.5, y=110, anchor="center")

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
            command=self.get_data_entry_check,
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
            font=(Home.font, 14),
            textvariable=value_entry_del,
        )
        entry_del.pack(pady=20)
        global error
        error = ctk.CTkLabel(
            frame, text="idSeance not found", text_color="#FF0033", height=20
        )
        # error.place(relx=0.5, y=110, anchor="center")
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
        )
        modi_button.pack(pady=20)

    def get_data_from_json(self):
        with open("./data.json", "r") as f:
            return json.load(f)["seances"]


a = Home().mainloop()
