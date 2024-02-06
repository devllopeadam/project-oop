import json
import customtkinter as ctk

ctk.set_appearance_mode("light")

from salle import Salle


class AjouterSalle(ctk.CTk):
    font = "Verdana"
    color = "#1d3557"

    def __init__(self):
        super().__init__()
        self.title("Ajouter Salle")
        self.geometry("600x550+530+50")
        self.iconbitmap("./images/login_icon.ico")
        self.resizable(False, False)

        title_window = ctk.CTkLabel(
            self,
            text="Ajouter Salle",
            font=(self.font, 25, "bold"),
            text_color=self.color,
        )
        title_window.pack(pady=20)
        self.create_entries_frame()

    def check_ajouter(self):
        final = []

        ids = [i["idSalle"] for i in self.get_data_from_json()]
        # for the id
        if value_id.get() == "":
            error_id.place(x=330, y=23)
        elif value_id.get() in ids:
            error_id.configure(text="always exist")
            error_id.place(x=350, y=23)
        else:
            error_id.place_forget()
            final.append(value_id.get())
        # for the libelle
        if value_libelle.get() == "":
            error_libelle.place(x=330, y=123)
        else:
            error_libelle.place_forget()
            final.append(value_libelle.get())
        # for the langue
        if value_numero.get() == "":
            error_numero.place(x=330, y=223)
        else:
            error_numero.place_forget()
            final.append(value_numero.get())

        if len(final) != 0:
            Salle.ajouterSalle(final[0], final[1], final[2])

    def create_entries_frame(self):
        frame = ctk.CTkFrame(self, width=450, height=450, fg_color="#F1F1F1")
        frame.pack(pady=20, ipadx=30, ipady=20)

        # for the id
        label_id = ctk.CTkLabel(
            frame, text="Id salle:", font=(self.font, 17), text_color=self.color
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
        # for the libelle

        label_libelle = ctk.CTkLabel(
            frame, text="Libelle:", font=(self.font, 17), text_color=self.color
        )
        global value_libelle
        value_libelle = ctk.StringVar()
        entry_libelle = ctk.CTkEntry(
            frame,
            textvariable=value_libelle,
            height=38,
            width=400,
            border_width=0,
            font=(self.font, 13),
            text_color=self.color,
        )
        global error_libelle
        error_libelle = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            font=(self.font, 11),
            height=5,
        )
        error_libelle.place_forget()
        label_libelle.place(x=30, y=100)
        entry_libelle.pack(pady=20)

        # for the numero
        label_numero = ctk.CTkLabel(
            frame, text="Numero:", font=(self.font, 17), text_color=self.color
        )
        global value_numero
        value_numero = ctk.StringVar()
        entry_numero = ctk.CTkEntry(
            frame,
            textvariable=value_numero,
            height=38,
            width=400,
            border_width=0,
            font=(self.font, 13),
            text_color=self.color,
        )
        global error_numero
        error_numero = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            font=(self.font, 11),
            height=5,
        )
        error_numero.place_forget()
        label_numero.place(x=30, y=200)
        entry_numero.pack(pady=40)

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
            return json.load(f)["salles"]


AjouterSalle().mainloop()
