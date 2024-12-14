from datetime import datetime
import customtkinter as ctk
from pymongo import *

ctk.set_appearance_mode("light")

from classes.seance import Seance
client = MongoClient("mongodb://localhost:27017/")
db = client["center-formation"]
collection = db["seances"]

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

    from datetime import datetime

    def check_ajouter(self):
        try:
            # Fetch data for validation
            ids = [i["_id"] for i in self.get_data_from_json()]
            proM = [i["_id"] for i in self.get_data("professeurs")]
            matM = [i["_id"] for i in self.get_data("matieres")]
            salM = [i["_id"] for i in self.get_data("salles")]
            final = []

            # Validate Seance ID
            if value_id.get().strip() == "":
                error_id.configure(text="ID cannot be empty")
                error_id.place(x=330, y=23)
                return
            elif value_id.get().strip() in ids:
                error_id.configure(text="ID already exists")
                error_id.place(x=350, y=23)
                return
            else:
                error_id.place_forget()
                final.append(value_id.get().strip())

            # Validate Professeur
            if value_professeur.get().strip() == "":
                error_professeur.configure(text="Professeur cannot be empty")
                error_professeur.place(x=330, y=123)
                return
            elif value_professeur.get().strip() not in proM:
                error_professeur.configure(text="Professeur does not exist")
                error_professeur.place(x=350, y=123)
                return
            else:
                error_professeur.place_forget()
                final.append(value_professeur.get().strip())

            # Validate Matiere
            if value_matiere.get().strip() == "":
                error_matiere.configure(text="Matiere cannot be empty")
                error_matiere.place(x=330, y=223)
                return
            elif value_matiere.get().strip() not in matM:
                error_matiere.configure(text="Matiere does not exist")
                error_matiere.place(x=355, y=223)
                return
            else:
                error_matiere.place_forget()
                final.append(value_matiere.get().strip())

            # Validate Salle
            if value_salle.get().strip() == "":
                error_salle.configure(text="Salle cannot be empty")
                error_salle.place(x=330, y=323)
                return
            elif value_salle.get().strip() not in salM:
                error_salle.configure(text="Salle does not exist")
                error_salle.place(x=355, y=323)
                return
            else:
                error_salle.place_forget()
                final.append(value_salle.get().strip())

            # Validate Date
            if value_date.get().strip() == "":
                error_date.configure(text="Date cannot be empty")
                error_date.place(x=330, y=420)
                return

            try:
                # Format the date
                formatted_date = datetime.strptime(
                    value_date.get().strip(), "%d/%m/%Y"
                ).strftime("%Y-%m-%d")
            except ValueError:
                error_date.configure(text="Invalid date format. Use DD/MM/YYYY.")
                error_date.place(x=320, y=420)
                return

            # Check Salle availability on the given Date
            print(
                f"Checking salle availability: Salle = {value_salle.get()}, Date = {formatted_date}"
            )
            state = Seance.afficherSalleDispo(value_salle.get(), formatted_date)
            if not state:  # Room is not available
                error_date.configure(text="Salle not available on this date")
                error_date.place(x=330, y=420)
                return
            else:
                error_date.place_forget()
                final.append(formatted_date)

            # Debug: Log final data
            print("Final Data to Add:", final)

            # Add the Seance
            Seance.ajouterSeance(final[0], final[1], final[2], final[3], final[4])
            from acceuil import Home

            print("Seance added successfully!")
            self.destroy()
            Home().mainloop()
        except Exception as e:
            print("Error in check_ajouter:", e)

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

    def get_data(self, value):
        colt = db[value]
        return list(colt.find())

    def get_data_from_json(self):
        return list(collection.find())
