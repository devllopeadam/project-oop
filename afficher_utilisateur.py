import json
import customtkinter as ctk
from tkinter import ttk

ctk.set_appearance_mode("light")

from utilisateur import Utilisateur


class AfficherUtilisateur(ctk.CTk):
    font = "Verdana"
    color = "#1d3557"

    def __init__(self):
        super().__init__()
        self.title("Afficher Utilisateur")
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
            columns=("login", "password", "email"),
            style="Custom.Treeview",
            show="headings",
        )
        table.heading("login", text="Login")
        table.heading("password", text="Password")
        table.heading("email", text="Email")
        table.column("login", anchor="center")
        table.column("password", anchor="center")
        table.column("email", anchor="center")
        table.pack(fill="both", expand=True)

        for i in self.get_data_from_json():
            table.insert(parent="", index="end", values=list(i.values()))

    def check_delete(self):
        logins = [i["login"] for i in self.get_data_from_json()]
        value = value_login.get()
        if value == "" or value == "entre votre login":
            error_login.configure(text="cannot be empty")
            error_login.place(x=153, y=21)
        elif value not in logins:
            error_login.configure(text="login not defind")
            error_login.place(x=153, y=21)
        elif value in logins:
            Utilisateur.supprimerUtilisateur(value)
            table.delete(*table.get_children())
            for i in self.get_data_from_json():
                table.insert(parent="", index="end", values=list(i.values()))
            error_login.place_forget()

    def modification(self):
        logins = [i["login"] for i in self.get_data_from_json()]
        newLogin = value_entry_new_login.get()
        newPassword = value_entry_new_password.get()
        newEmail = value_entry_new_email.get()
        valueLogin = value_old_login.get()
        final = []
        arL = []
        arP = []
        arE = []

        for i in self.get_data_from_json():
            if i["login"] != valueLogin:
                arL.append(i["login"])
        for i in self.get_data_from_json():
            if i["login"] != valueLogin:
                arP.append(i["password"])

        for i in self.get_data_from_json():
            if i["login"] != valueLogin:
                arE.append(i["email"])

        if valueLogin == "" or valueLogin == "Entre votre login":
            error_old_login.configure(text="cannot be empty")
            error_old_login.place(x=153, y=175)
        elif valueLogin not in logins:
            error_old_login.configure(text="login not found")
            error_old_login.place(x=153, y=175)
        elif valueLogin in logins:
            # for the new login

            if newLogin == "" or newLogin == "new login":
                error_new_login.configure(text="cannot be empty")
                error_new_login.place(x=153, y=272)
            elif newLogin in arL:
                error_new_login.configure(text="always exist")
                error_new_login.place(x=170, y=272)
            elif newLogin not in arL:
                error_new_login.place_forget()
                final.append(newLogin)

            # for the new password

            if newPassword == "" or newPassword == "new password":
                error_new_password.configure(text="cannot be empty")
                error_new_password.place(x=153, y=345)
            elif newPassword in arP:
                error_new_password.configure(text="always exist")
                error_new_password.place(x=170, y=345)
            elif newPassword not in arP:
                error_new_password.place_forget()
                final.append(newPassword)

            # for the new email
            if newEmail == "" or newEmail == "new email":
                error_new_email.configure(text="cannot be empty")
                error_new_email.place(x=153, y=420)
            elif newEmail in arE:
                error_new_email.configure(text="always exist")
                error_new_email.place(x=170, y=420)
            elif newEmail not in arE:
                error_new_email.place_forget()
                final.append(newEmail)

            try:
                Utilisateur.mofidierUtilisateur(
                    value_old_login.get(), final[0], final[1], final[2]
                )
                table.delete(*table.get_children())
                for i in self.get_data_from_json():
                    table.insert(parent="", index="end", values=list(i.values()))
            except:
                print("final is empty")

            error_old_login.place_forget()

    def filter_delete_bar(self):
        frame = ctk.CTkFrame(
            self,
            fg_color="#f8f8f8",
            bg_color="#f8f8f8",
            corner_radius=0,
        )
        frame.place(relwidth=0.27, relheight=1, relx=0.73)

        # for the delete utilisateur
        global value_login
        value_login = ctk.StringVar()
        entry_login = ctk.CTkEntry(
            frame, width=200, height=35, font=(self.font, 13), textvariable=value_login
        )
        global error_login
        error_login = ctk.CTkLabel(
            frame,
            text="Login not found",
            text_color="#FF0033",
            height=5,
        )
        # for the delete button
        button_login = ctk.CTkButton(
            frame,
            text="Supprimer",
            font=(self.font, 15),
            fg_color="red",
            text_color="white",
            height=38,
            hover_color="#f53737",
            command=self.check_delete,
        )
        button_login.configure(cursor="hand2")
        error_login.place_forget()
        entry_login.insert(index=ctk.END, string="entre votre login")
        entry_login.pack(pady=40)
        button_login.pack()
        # for the modification entries etc...
        global value_old_login
        value_old_login = ctk.StringVar()
        entry_old_login = ctk.CTkEntry(
            frame,
            width=200,
            height=35,
            font=(self.font, 13),
            textvariable=value_old_login,
        )
        global error_old_login
        error_old_login = ctk.CTkLabel(
            frame,
            text="Login not found",
            text_color="#FF0033",
            height=5,
        )
        error_old_login.place_forget()
        entry_old_login.pack(pady=40)
        entry_old_login.insert(index=ctk.END, string="Entre votre login")

        # for the new login
        global value_entry_new_login
        value_entry_new_login = ctk.StringVar()
        entry_new_login = ctk.CTkEntry(
            frame,
            width=200,
            height=35,
            font=(self.font, 13),
            textvariable=value_entry_new_login,
        )
        global error_new_login
        error_new_login = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            height=5,
        )
        error_new_login.place_forget()
        entry_new_login.insert(index=ctk.END, string="new login")
        entry_new_login.pack(pady=20)

        # for the new password

        global value_entry_new_password
        value_entry_new_password = ctk.StringVar()
        entry_new_password = ctk.CTkEntry(
            frame,
            width=200,
            height=35,
            font=(self.font, 13),
            textvariable=value_entry_new_password,
        )
        global error_new_password
        error_new_password = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            height=5,
        )
        error_new_password.place_forget()
        entry_new_password.insert(index=ctk.END, string="new password")
        entry_new_password.pack(pady=20)

        # for the new email

        global value_entry_new_email
        value_entry_new_email = ctk.StringVar()
        entry_new_email = ctk.CTkEntry(
            frame,
            width=200,
            height=35,
            font=(self.font, 13),
            textvariable=value_entry_new_email,
        )
        global error_new_email
        error_new_email = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            height=5,
        )
        error_new_email.place_forget()
        entry_new_email.insert(index=ctk.END, string="new email")
        entry_new_email.pack(pady=20)

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
        with open("./data.json", "r") as f:
            return json.load(f)["utilisateurs"]
