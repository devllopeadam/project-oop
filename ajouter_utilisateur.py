import json
import re
import customtkinter as ctk

from utilisateur import Utilisateur


ctk.set_appearance_mode("light")


class AjouterUtilisateur(ctk.CTk):
    font = "Verdana"
    color = "#1d3557"

    def __init__(self):
        super().__init__()
        self.title("Ajouter Utilisateur")
        self.geometry("600x550+530+50")
        self.iconbitmap("./images/login_icon.ico")
        self.resizable(False, False)
        # Title window

        title_window = ctk.CTkLabel(
            self,
            text="Ajouter Utilisateur",
            font=(self.font, 25, "bold"),
            text_color=self.color,
        )
        title_window.pack(pady=20)
        self.create_entries_frame()

    def check_ajouter(self):
        logins = [i["login"] for i in self.get_data_from_json()]
        passwords = [i["password"] for i in self.get_data_from_json()]
        emails = [i["email"] for i in self.get_data_from_json()]
        login = value_login.get()
        password = value_password.get()
        email = value_email.get()
        final = []

        # for the login validation
        if login == "":
            error_login.configure(text="cannot be empty")
            error_login.place(x=325, y=10)
        elif login in logins:
            error_login.configure(text="login always exist")
            error_login.place(x=320, y=10)
        else:
            error_login.place_forget()
            final.append(login)

        # for the password validation
        if password == "":
            error_password.configure(text="cannot be empty")
            error_password.place(y=112, x=325)
        elif password in passwords:
            error_password.configure(text="password always exist")
            error_password.place(y=112, x=296)
        else:
            error_password.place_forget()
            final.append(password)

        # for the email validation

        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if email == "" or bool(re.match(pattern, email)) == False:
            error_email.configure(text="Invalid Email")
            error_email.place(y=212, x=350)
        elif email in emails:
            error_email.configure(text="Email always exist")
            error_email.place(y=212, x=310)
        else:
            error_email.place_forget()
            final.append(email)

        Utilisateur.ajouterUtilisateur(final[0], final[1], final[2])

    def create_entries_frame(self):
        frame = ctk.CTkFrame(self, width=450, height=500, fg_color="#F1F1F1")
        frame.pack(pady=20, ipadx=30, ipady=20)

        # for the login entry
        label_login = ctk.CTkLabel(
            frame, text="Login:", font=(self.font, 17), text_color=self.color
        )
        global value_login
        value_login = ctk.StringVar()
        entry_login = ctk.CTkEntry(
            frame,
            textvariable=value_login,
            height=38,
            width=400,
            border_width=0,
            font=(self.font, 13),
            text_color=self.color,
        )
        global error_login
        error_login = ctk.CTkLabel(
            frame,
            text="login always exist",
            text_color="#FF0033",
            font=(self.font, 11),
            height=5,
        )
        label_login.place(x=25, y=-5)
        # error_login.place(x=320, y=10)
        error_login.place_forget()
        entry_login.pack(pady=30)

        # for the password

        label_password = ctk.CTkLabel(
            frame, text="Password:", font=(self.font, 17), text_color=self.color
        )
        global value_password
        value_password = ctk.StringVar()
        entry_password = ctk.CTkEntry(
            frame,
            textvariable=value_password,
            height=38,
            width=400,
            border_width=0,
            font=(self.font, 13),
            text_color=self.color,
            show="⁕",
        )
        label_password.place(y=95, x=25)
        entry_password.pack(pady=30)
        global error_password
        error_password = ctk.CTkLabel(
            frame,
            text="password always exist",
            text_color="#FF0033",
            font=(self.font, 11),
            height=5,
        )
        # error_password.place(y=112, x=320)
        error_password.place_forget()

        # for the email

        label_email = ctk.CTkLabel(
            frame, text="Email:", font=(self.font, 17), text_color=self.color
        )
        global value_email
        value_email = ctk.StringVar()
        entry_email = ctk.CTkEntry(
            frame,
            textvariable=value_email,
            height=38,
            width=400,
            border_width=0,
        )
        label_email.place(y=190, x=25)
        entry_email.pack(pady=30)
        global error_email
        error_email = ctk.CTkLabel(
            frame,
            text="invalid email",
            text_color="#FF0033",
            font=(self.font, 11),
            height=5,
        )
        # error_email.place(y=212, x=350)
        error_email.place_forget()

        # Button ajouter

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
            return json.load(f)["utilisateurs"]


# AjouterUtilisateur().mainloop()
