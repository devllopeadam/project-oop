import customtkinter as ctk
from tkinter import ttk
from pymongo import *

ctk.set_appearance_mode("light")

from classes.utilisateur import Utilisateur
client = MongoClient("mongodb://localhost:27017/")
db = client["center-formation"]
collection = db["utilisateurs"]


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
            columns=("username", "password", "email"),
            style="Custom.Treeview",
            show="headings",
        )
        table.heading("username", text="username")
        table.heading("password", text="Password")
        table.heading("email", text="Email")
        table.column("username", anchor="center")
        table.column("password", anchor="center")
        table.column("email", anchor="center")
        table.pack(fill="both", expand=True)

        for i in self.get_data_from_json():
            table.insert(parent="", index="end", values=list(i.values())[1:])

    def check_delete(self):
        usernames = [i["username"] for i in self.get_data_from_json()]
        value = value_username.get()
        if value == "" or value == "entre votre username":
            error_username.configure(text="cannot be empty")
            error_username.place(x=153, y=21)
        elif value not in usernames:
            error_username.configure(text="username not defind")
            error_username.place(x=153, y=21)
        elif value in usernames:
            Utilisateur.supprimerUtilisateur(value)
            table.delete(*table.get_children())
            for i in self.get_data_from_json():
                table.insert(parent="", index="end", values=list(i.values()[1:]))
            error_username.place_forget()

    def modification(self):
        usernames = [i["username"] for i in self.get_data_from_json()]
        newusername = value_entry_new_username.get()
        newPassword = value_entry_new_password.get()
        newEmail = value_entry_new_email.get()
        valueusername = value_old_username.get()
        final = []
        arL = []
        arP = []
        arE = []

        for i in self.get_data_from_json():
            if i["username"] != valueusername:
                arL.append(i["username"])
        for i in self.get_data_from_json():
            if i["username"] != valueusername:
                arP.append(i["password"])

        for i in self.get_data_from_json():
            if i["username"] != valueusername:
                arE.append(i["email"])

        if valueusername == "" or valueusername == "Entre votre username":
            error_old_username.configure(text="cannot be empty")
            error_old_username.place(x=153, y=175)
        elif valueusername not in usernames:
            error_old_username.configure(text="username not found")
            error_old_username.place(x=153, y=175)
        elif valueusername in usernames:
            # for the new username

            if newusername == "" or newusername == "new username":
                error_new_username.configure(text="cannot be empty")
                error_new_username.place(x=153, y=272)
            elif newusername in arL:
                error_new_username.configure(text="always exist")
                error_new_username.place(x=170, y=272)
            elif newusername not in arL:
                error_new_username.place_forget()
                final.append(newusername)

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
                    value_old_username.get(), final[0], final[1], final[2]
                )
                table.delete(*table.get_children())
                for i in self.get_data_from_json():
                    table.insert(parent="", index="end", values=list(i.values()[1:]))
            except:
                print("final is empty")

            error_old_username.place_forget()

    def filter_delete_bar(self):
        frame = ctk.CTkFrame(
            self,
            fg_color="#f8f8f8",
            bg_color="#f8f8f8",
            corner_radius=0,
        )
        frame.place(relwidth=0.27, relheight=1, relx=0.73)

        # for the delete utilisateur
        global value_username
        value_username = ctk.StringVar()
        # for the delete button
        button_username = ctk.CTkButton(
            frame,
            text="Supprimer",
            font=(self.font, 15),
            fg_color="red",
            text_color="white",
            height=38,
            hover_color="#f53737",
            command=self.check_delete,
        )
        entry_username = ctk.CTkEntry(
            frame,
            width=200,
            height=35,
            font=(self.font, 13),
            textvariable=value_username,
        )
        global error_username
        error_username = ctk.CTkLabel(
            frame,
            text="username not found",
            text_color="#FF0033",
            height=5,
        )
        button_username.configure(cursor="hand2")
        error_username.place_forget()
        entry_username.insert(index=ctk.END, string="entre votre username")
        entry_username.pack(pady=40)
        button_username.pack()
        # for the modification entries etc...
        global value_old_username
        value_old_username = ctk.StringVar()
        entry_old_username = ctk.CTkEntry(
            frame,
            width=200,
            height=35,
            font=(self.font, 13),
            textvariable=value_old_username,
        )
        global error_old_username
        error_old_username = ctk.CTkLabel(
            frame,
            text="username not found",
            text_color="#FF0033",
            height=5,
        )
        error_old_username.place_forget()
        entry_old_username.pack(pady=40)
        entry_old_username.insert(index=ctk.END, string="Entre votre username")

        # for the new username
        global value_entry_new_username
        value_entry_new_username = ctk.StringVar()
        entry_new_username = ctk.CTkEntry(
            frame,
            width=200,
            height=35,
            font=(self.font, 13),
            textvariable=value_entry_new_username,
        )
        global error_new_username
        error_new_username = ctk.CTkLabel(
            frame,
            text="cannot be empty",
            text_color="#FF0033",
            height=5,
        )
        error_new_username.place_forget()
        entry_new_username.insert(index=ctk.END, string="new username")
        entry_new_username.pack(pady=20)

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
        return list(collection.find())
