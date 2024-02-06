import json
import customtkinter as ctk

from professeur import Professeur

ctk.set_appearance_mode("light")


class AjouterProfesseur(ctk.CTk):
    font = "Verdana"
    color = "#1d3557"

    def __init__(self):
        super().__init__()
        self.title("Ajouter Professeur")
        self.geometry("600x700+530+50")
        self.iconbitmap("./images/login_icon.ico")
        self.resizable(False, False)

        title_window = ctk.CTkLabel(
            self,
            text="Ajouter Professeur",
            font=(self.font, 25, "bold"),
            text_color=self.color,
        )
        title_window.pack(pady=20)
        self.create_entries_frame()

    def check_ajouter(self):
        nom = value_nom.get()
        prenom = value_prenom.get()
        filiere = value_filiere.get()
        cin = value_cin.get()
        matricule = value_matricule.get()
        final = []

        # for the nom
        if nom == "":
            error_nom.place(x=330, y=20)
        else:
            error_nom.place_forget()
            final.append(nom)

        # for the prenom

        if prenom == "":
            error_prenom.place(x=330, y=120)
        else:
            error_prenom.place_forget()
            final.append(prenom)

        # for the filiere
        if filiere == "":
            error_filiere.place(x=330, y=320)
        else:
            error_filiere.place_forget()
            final.append(filiere)

        # for the cin

        if cin == "":
            error_cin.place(x=330, y=220)
        elif cin in [i["cin"] for i in self.get_data_from_json()]:
            error_cin.configure(text="always exists")
            error_cin.place(x=350, y=220)
        else:
            error_cin.place_forget()
            final.append(cin)

        # for the matricule

        if matricule == "":
            error_matricule.place(x=330, y=415)
        elif matricule in [i["matricule"] for i in self.get_data_from_json()]:
            error_matricule.configure(text="always exists")
            error_matricule.place(x=345, y=415)
        else:
            error_matricule.place_forget()
            final.append(matricule)

        if len(final) != 0:
            Professeur.ajouterProfesseur(
                final[0], final[1], final[2], final[3], final[4]
            )

    def create_entries_frame(self):
        frame = ctk.CTkFrame(self, width=450, height=450, fg_color="#F1F1F1")
        frame.pack(pady=20, ipadx=30, ipady=20)

        # for the nom

        label_nom = ctk.CTkLabel(
            frame, text="Nom:", font=(self.font, 17), text_color=self.color
        )
        global value_nom
        value_nom = ctk.StringVar()
        entry_nom = ctk.CTkEntry(
            frame,
            textvariable=value_nom,
            height=38,
            width=400,
            border_width=0,
            font=(self.font, 13),
            text_color=self.color,
        )
        global error_nom
        error_nom = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            font=(self.font, 11),
            height=5,
        )
        error_nom.pack_forget()
        label_nom.place(x=30)
        entry_nom.pack(pady=40)

        # for the prenom

        label_prenom = ctk.CTkLabel(
            frame, text="Prenom:", font=(self.font, 17), text_color=self.color
        )
        global value_prenom
        value_prenom = ctk.StringVar()
        entry_prenom = ctk.CTkEntry(
            frame,
            textvariable=value_prenom,
            height=38,
            width=400,
            border_width=0,
            font=(self.font, 13),
            text_color=self.color,
        )
        global error_prenom
        error_prenom = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            font=(self.font, 11),
            height=5,
        )
        error_prenom.place_forget()
        label_prenom.place(x=30, y=100)
        entry_prenom.pack(pady=20)

        # for the cin

        label_cin = ctk.CTkLabel(
            frame, text="Cin:", font=(self.font, 17), text_color=self.color
        )
        global value_cin
        value_cin = ctk.StringVar()
        entry_cin = ctk.CTkEntry(
            frame,
            textvariable=value_cin,
            height=38,
            width=400,
            border_width=0,
            font=(self.font, 13),
            text_color=self.color,
        )
        global error_cin
        error_cin = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            font=(self.font, 11),
            height=5,
        )
        error_cin.place_forget()
        label_cin.place(x=30, y=200)
        entry_cin.pack(pady=40)

        # for the filiere

        label_filiere = ctk.CTkLabel(
            frame, text="Filiere:", font=(self.font, 17), text_color=self.color
        )
        global value_filiere
        value_filiere = ctk.StringVar()
        entry_filiere = ctk.CTkEntry(
            frame,
            textvariable=value_filiere,
            height=38,
            width=400,
            border_width=0,
            font=(self.font, 13),
            text_color=self.color,
        )
        global error_filiere
        error_filiere = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            font=(self.font, 11),
            height=5,
        )
        error_filiere.place_forget()
        label_filiere.place(x=30, y=300)
        entry_filiere.pack(pady=20)

        # for the matricule

        label_matricule = ctk.CTkLabel(
            frame, text="Matricule:", font=(self.font, 17), text_color=self.color
        )
        global value_matricule
        value_matricule = ctk.StringVar()
        entry_matricule = ctk.CTkEntry(
            frame,
            textvariable=value_matricule,
            height=38,
            width=400,
            border_width=0,
            font=(self.font, 13),
            text_color=self.color,
        )
        global error_matricule
        error_matricule = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            font=(self.font, 11),
            height=5,
        )
        # error_matricule.place(x=330, y=415)
        label_matricule.place(x=30, y=400)
        entry_matricule.pack(pady=40)

        # for the button

        ajouter_button = ctk.CTkButton(
            frame,
            text="Ajouter",
            font=(self.font, 13),
            width=160,
            height=40,
            fg_color=self.color,
            hover_color="#233d60",
            command=self.check_ajouter,
        )
        ajouter_button.pack()
        ajouter_button.configure(cursor="hand2")

    def get_data_from_json(self):
        with open("./data.json", "r") as f:
            return json.load(f)["professeurs"]


# AjouterProfesseur().mainloop()
