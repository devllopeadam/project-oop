import json
import customtkinter as ctk
from pymongo import *

ctk.set_appearance_mode("light")

from classes.seance import Seance
client = MongoClient("mongodb://localhost:27017/")
db = client["center-formation"]
collection = db["utilisateurs"]

class AjouterSeance(ctk.CTk):
    font = "Verdana"
    color = "#1d3557"

    def __init__(self):
        super().__init__()
        self.title("Ajouter Seance")
        self.geometry("600x700+530+50")
        self.iconbitmap("./images/login_icon.ico")
        self.resizable(False, False)

        title_window = ctk.CTkLabel(
            self,
            text="Ajouter Seance",
            font=(self.font, 25, "bold"),
            text_color=self.color,
        )
        title_window.pack(pady=20)
        self.create_entries_frame()

    def check_ajouter(self):
        ids = [i["idSeance"] for i in self.get_data_from_json()]
        with open("./data.json", "r") as f:
            dataP = json.load(f)["professeurs"]
        proM = [i["matricule"] for i in dataP]
        with open("./data.json", "r") as f:
            dataM = json.load(f)["matieres"]
        matM = [i["idMatiere"] for i in dataM]
        with open("./data.json", "r") as f:
            dataS = json.load(f)["salles"]
        salM = [i["idSalle"] for i in dataS]
        final = []
        # for the id seance
        if value_id.get() == "":
            error_id.place(x=330, y=23)
        elif value_id.get() in ids:
            error_id.configure(text="always exist")
            error_id.place(x=350, y=23)
        else:
            error_id.place_forget()
            final.append(value_id.get())

        # for the professeur
        if value_professeur.get() == "":
            error_professeur.place(x=330, y=123)
        elif value_professeur.get() not in proM:
            error_professeur.configure(text="is not exist")
            error_professeur.place(x=350, y=23)
        else:
            error_professeur.place_forget()
            for i in dataP:
                if i["matricule"] == value_professeur.get():
                    final.append(i)

        # for the matiere id

        if value_matiere.get() == "":
            error_matiere.place(x=330, y=223)
        elif value_matiere.get() not in matM:
            error_matiere.configure(text="is not exist")
            error_matiere.place(x=355, y=223)
        else:
            error_matiere.place_forget()
            for i in dataM:
                if i["idMatiere"] == value_matiere.get():
                    final.append(i)

        if value_salle.get() == "":
            error_salle.place(x=330, y=323)
        elif value_salle.get() not in salM:
            error_salle.configure(text="is not exist")
            error_salle.place(x=355, y=323)
        else:
            error_salle.place_forget()
            for i in dataS:
                if i["idSalle"] == value_salle.get():
                    final.append(i)

        # for the date
        state = Seance.afficherSalleDispo(value_salle.get(), value_date.get())

        if value_date.get() == "":
            error_date.place(x=330, y=420)
        elif state == True:
            # for update please
            error_date.configure("date not dispo")
            error_date.place(x=330, y=420)
        else:
            error_date.place_forget()
            final.append(value_date.get())

        Seance.ajouterSeance(final[0], final[1], final[2], final[3], final[4])

    def create_entries_frame(self):
        frame = ctk.CTkFrame(self, width=450, height=450, fg_color="#F1F1F1")
        frame.pack(pady=20, ipadx=30, ipady=20)

        # for the id
        label_id = ctk.CTkLabel(
            frame, text="Id seance:", font=(self.font, 17), text_color=self.color
        )
        global value_id
        value_id = ctk.StringVar()
        entry_id = ctk.CTkEntry(
            frame,
            textvariable=value_id,
            height=38,
            width=400,
            border_width=0,
            font=(self.font, 13),
            text_color=self.color,
        )
        global error_id
        error_id = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            font=(self.font, 11),
            height=5,
        )
        error_id.place_forget()
        label_id.place(x=30)
        entry_id.pack(pady=40)

        # for the professeur

        label_professeur = ctk.CTkLabel(
            frame,
            text="professeur matricule:",
            font=(self.font, 17),
            text_color=self.color,
        )
        global value_professeur
        value_professeur = ctk.StringVar()
        entry_professeur = ctk.CTkEntry(
            frame,
            textvariable=value_professeur,
            height=38,
            width=400,
            border_width=0,
            font=(self.font, 13),
            text_color=self.color,
        )
        global error_professeur
        error_professeur = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            font=(self.font, 11),
            height=5,
        )
        error_professeur.place_forget()
        label_professeur.place(x=30, y=100)
        entry_professeur.pack(pady=20)

        # for the matiere

        label_matiere = ctk.CTkLabel(
            frame,
            text="id matiere:",
            font=(self.font, 17),
            text_color=self.color,
        )
        global value_matiere
        value_matiere = ctk.StringVar()
        entry_matiere = ctk.CTkEntry(
            frame,
            textvariable=value_matiere,
            height=38,
            width=400,
            border_width=0,
            font=(self.font, 13),
            text_color=self.color,
        )
        global error_matiere
        error_matiere = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            font=(self.font, 11),
            height=5,
        )
        error_matiere.place_forget()
        label_matiere.place(x=30, y=200)
        entry_matiere.pack(pady=40)

        # for the salle

        label_salle = ctk.CTkLabel(
            frame,
            text="salle id:",
            font=(self.font, 17),
            text_color=self.color,
        )
        global value_salle
        value_salle = ctk.StringVar()
        entry_salle = ctk.CTkEntry(
            frame,
            textvariable=value_salle,
            height=38,
            width=400,
            border_width=0,
            font=(self.font, 13),
            text_color=self.color,
        )
        global error_salle
        error_salle = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            font=(self.font, 11),
            height=5,
        )
        error_salle.place_forget()
        label_salle.place(x=30, y=300)
        entry_salle.pack(pady=20)

        # for the date

        label_date = ctk.CTkLabel(
            frame, text="Date Seance:", font=(self.font, 17), text_color=self.color
        )
        global value_date
        value_date = ctk.StringVar()
        entry_date = ctk.CTkEntry(
            frame,
            textvariable=value_date,
            height=38,
            width=400,
            border_width=0,
            font=(self.font, 13),
            text_color=self.color,
        )
        global error_date
        error_date = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            font=(self.font, 11),
            height=5,
        )
        error_date.place_forget()
        label_date.place(x=30, y=400)
        entry_date.pack(pady=40)

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
        return list(collection.find())


# AjouterSeance().mainloop()
