import customtkinter as ctk

ctk.set_appearance_mode("light")

from utilisateur import Utilisateur
from acceuil import Home


class Login(ctk.CTk):
    font = "Verdana"
    color = "#1d3557"

    def __init__(self):
        super().__init__()
        self.title("Authentification")
        self.geometry("600x550+530+50")
        self.iconbitmap("./images/login_icon.ico")
        self.resizable(False, False)
        # The title of the login window
        login_title = ctk.CTkLabel(
            self,
            text="Login",
            font=("Verdana", 30, "bold"),
            text_color=("#1d3557", "white"),
        )
        login_title.pack(pady=30)

        # the inputs
        input_frame = ctk.CTkFrame(self, width=400, height=450, fg_color="#f0efef")
        input_frame.pack(pady=20, ipady=30)
        self.make_input(input_frame)

        # Create the submit button
        btn = ctk.CTkButton(
            input_frame,
            text="Submit",
            command=self.submit,
            fg_color=Login.color,
            font=(Login.color, 17),
            hover_color="#234067",
            height=40,
        )
        btn.pack(pady=20)

    def make_input(self, parent):
        global make_error

        def make_error(parent, text_error, xValue, color):
            global error_label
            error_label = ctk.CTkLabel(
                parent,
                text=text_error,
                text_color=color,
                font=(Login.font, 13, "normal"),
                justify="right",
            )
            error_label.place(y=20, x=xValue)

        # first input
        global frameOne
        frameOne = ctk.CTkFrame(parent, width=500, height=100, fg_color="transparent")

        label_input = ctk.CTkLabel(
            frameOne,
            text="Login:",
            font=(Login.font, 15),
            text_color=Login.color,
        )
        label_input.place(x=30, y=20)
        global login_value
        login_value = ctk.StringVar()
        login_input = ctk.CTkEntry(
            parent,
            placeholder_text="login",
            width=430,
            height=40,
            font=(Login.font, 13),
            corner_radius=10,
            border_width=0,
            border_color=Login.color,
            textvariable=login_value,
        )

        login_input.place(x=30, y=65)
        frameOne.pack(pady=5)
        # second input
        global frameTwo
        frameTwo = ctk.CTkFrame(parent, width=500, height=100, fg_color="transparent")
        label_pass = ctk.CTkLabel(
            frameTwo,
            text="Password:",
            font=(Login.font, 15),
            text_color=Login.color,
        )
        label_pass.place(x=30, y=20)
        global password_value
        password_value = ctk.StringVar()
        password_input = ctk.CTkEntry(
            frameTwo,
            placeholder_text="password",
            width=430,
            height=40,
            font=(Login.font, 13),
            corner_radius=10,
            border_width=0,
            border_color=Login.color,
            textvariable=password_value,
            show="⁕",
        )
        password_input.place(x=30, y=60)
        frameTwo.pack(pady=10)

    def submit(self):
        get_login = login_value.get()
        get_password = password_value.get()
        colorInvalid = "#FF3333"
        try:
            if Utilisateur.authentifier(get_login, get_password) == True:
                self.destroy()
                Home().mainloop()
            elif Utilisateur.authentifier(get_login, get_password) == False:
                make_error(frameTwo, "Incorrect Password", 333, colorInvalid)
            else:
                print(Utilisateur.authentifier(get_login, get_password))
                make_error(frameOne, "Incorrect Login", 360, colorInvalid)
        except:
            print("Error for the hide function")


Login().mainloop()
