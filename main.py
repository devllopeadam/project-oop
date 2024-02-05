import json


# Declaring all the classes
# class Matiere
class Matiere:
    matieres = []

    def __init__(self, idMatiere, libelle, langue):
        self.__idMatiere = idMatiere
        self.__libelle = libelle
        self.__langue = langue

        # Pour Lister Tout les matieres

        Matiere.matieres.append(
            {
                "idMatiere": self.idMatiere,
                "libelle": self.libelle,
                "langue": self.langue,
            }
        )
        with open("./data.json", "r") as file:
            data = json.load(file)

            data["matieres"] = Matiere.matieres

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    # to delete a specific matiere using the idMatiere
    def supprimerMatiere(idMatiere):
        for i in Matiere.matieres:
            if i["idMatiere"] == idMatiere:
                Matiere.matieres.remove(i)
        with open("./data.json", "r") as file:
            data = json.load(file)
        data["matieres"] = Matiere.matieres

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    # to add a matiere to the matieres list
    @classmethod
    def ajouterMatiere(cls, idMatiere, libelle, langue):
        return cls(idMatiere, libelle, langue)

    # to modify the matiere
    @classmethod
    def mofidierMatiere(cls, idMatiere, newIdMatiere, newLibelle, newLangue):
        for i in Matiere.matieres:
            if i["idMatiere"] == idMatiere:
                i["idMatiere"] = newIdMatiere
                i["libelle"] = newLibelle
                i["langue"] = newLangue
            with open("./data.json", "r") as file:
                data = json.load(file)
            data["matieres"] = Matiere.matieres
            with open("./data.json", "w") as file:
                json.dump(data, file, indent=2)

    # the getters and the setters

    @property
    def idMatiere(self):
        return self.__idMatiere

    @idMatiere.setter
    def idMatiere(self, value):
        self.__idMatiere = value

    @property
    def libelle(self):
        return self.__libelle

    @libelle.setter
    def libelle(self, value):
        self.__libelle = value

    @property
    def langue(self):
        return self.__langue

    @langue.setter
    def langue(self, value):
        self.__libelle = value

    # the method to return a string about the object
    def __str__(self):
        return f"La matiere de l'id {self.idMatiere} de libelle {self.libelle}, et de langue {self.langue}"


matiereOne = Matiere("fr1230", "pour la langue francaise", "Francais")
matiereTwo = Matiere("en500", "english course", "English")
# matiereThree = Matiere("ar400", "arabic course", "Arabic")

# Matiere.ajouterMatiere("ger123", "pour la langue germnay", "Germany")
# Matiere.mofidierMatiere("ger123", "ger5500", "Pour la langue germany", "germany")

# print(Matiere.matieres)


class Salle:
    salles = []

    def __init__(self, idSalle, libelle, numero):
        self.__idSalle = idSalle
        self.__libelle = libelle
        self.__numero = numero

        Salle.salles.append({"idSalle": idSalle, "libelle": libelle, "numero": numero})

    # to delete a salle from the salles list
    def supprimerSalle(idSalle):
        for i in Salle.salles:
            if i["idSalle"] == idSalle:
                Salle.salles.remove(i)

    # to add a salle to the salle list
    @classmethod
    def ajouterSalle(cls, idSalle, libelle, numero):
        return cls(idSalle, libelle, numero)

    # to modify the salle
    @classmethod
    def mofidierSalle(cls, idSalle, newIdSalle, newLibelle, newNumero):
        for i in Salle.salles:
            if i["idSalle"] == idSalle:
                i["idSalle"] = newIdSalle
                i["libelle"] = newLibelle
                i["numero"] = newNumero

    # the getters and the setters
    @property
    def idSalle(self):
        return self.__idSalle

    @idSalle.setter
    def idSalle(self, value):
        self.__idSalle = value

    @property
    def libelle(self):
        return self.__libelle

    @libelle.setter
    def libelle(self, value):
        self.__libelle = value

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, value):
        self.__numero = value

    def __str__(self) -> str:
        return f"la salle de l'id {self.idSalle} de libelle {self.libelle}, et de numero {self.numero}"


saleOne = Salle.ajouterSalle("salleE", "pour la salle E", 80)
saleTwo = Salle.ajouterSalle("salleJ", "pour la salle j", "math")
saleThree = Salle.ajouterSalle("salleH", "pour la salle h", "pc")
# Salle.ajouterSalle("salleA", "pour la salle B", 60)
# Salle.mofidierSalle("salleA", "salleA+", "Pour la salle A+", 62)

# print(Salle.salles)


class Person:
    personnes = []

    def __init__(self, nom, prenom, cin):
        self._nom = nom
        self._prenom = prenom
        self._cin = cin
        Person.personnes.append({"nom": nom, "prenom": prenom, "cin": cin})

    # to delete a salle from the personnes list

    def supprimerPerson(cin):
        for i in Person.personnes:
            if i["cin"] == cin:
                Person.personnes.remove(i)

    @classmethod
    def ajouterPerson(cls, nom, prenom, cin):
        return cls(nom, prenom, cin)

    @classmethod
    def mofidierPerson(cls, cin, newNom, newPrenom, newCin):
        for i in Person.personnes:
            if i["cin"] == cin:
                i["nom"] = newNom
                i["prenom"] = newPrenom
                i["cin"] = newCin

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, value):
        self._prenom = value

    @property
    def cin(self):
        return self._cin

    @cin.setter
    def cin(self, value):
        self._cin = value

    def __str__(self) -> str:
        return (
            f"la person du nom {self.nom} du prenom {self.prenom}, et du cin {self.cin}"
        )


a = Person("jeniah", "adam", "kb243538")

# print(Person.personnes)


class Apprenant(Person):
    apprenants = []

    def __init__(self, nom, prenom, cin, niveau, age):
        self.__niveau = niveau
        self.__age = age
        super().__init__(nom, prenom, cin)
        Apprenant.apprenants.append(
            {"nom": nom, "prenom": prenom, "cin": cin, "niveau": niveau, "age": age}
        )

    def supprimerApprenant(cin):
        for i in Apprenant.apprenants:
            if i["cin"] == cin:
                Apprenant.apprenants.remove(i)

    @classmethod
    def ajouterApprenant(cls, nom, prenom, cin, niveau, age):
        return cls(nom, prenom, cin, niveau, age)

    @classmethod
    def mofidierApprenant(cls, cin, newNom, newPrenom, newCin, newNiveau, newAge):
        for i in Apprenant.apprenants:
            if i["cin"] == cin:
                i["nom"] = newNom
                i["prenom"] = newPrenom
                i["cin"] = newCin
                i["niveau"] = newNiveau
                i["age"] = newAge

    @property
    def niveau(self):
        return self.__niveau

    @niveau.setter
    def niveau(self, value):
        self.__niveau = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value


# b = Apprenant("jeniah", "nom", "kb243538", "B1", 19)
# b.mofidierApprenant("kb243538", "jeniahA", "adam", "kb243538", "B1", 19)
# e = Apprenant("biba", "Anas", "kb243538", "B1", 19)
# Apprenant.supprimerApprenant("kb243538")
# print(Apprenant.apprenants)


class Professeur(Person):
    professeurs = []

    def __init__(self, nom, prenom, cin, filiere, matricule):
        self.__filiere = filiere
        self.__matricule = matricule
        super().__init__(nom, prenom, cin)
        Professeur.professeurs.append(
            {
                "nom": nom,
                "prenom": prenom,
                "cin": cin,
                "filiere": filiere,
                "matricule": matricule,
            }
        )
        with open("./data.json", "r") as file:
            data = json.load(file)

            data["professeurs"] = Professeur.professeurs

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    def supprimerProfesseur(cin):
        for i in Professeur.professeurs:
            if i["cin"] == cin:
                Professeur.professeurs.remove(i)

        with open("./data.json", "r") as file:
            data = json.load(file)
        data["professeurs"] = Professeur.professeurs

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    @classmethod
    def ajouterProfesseur(cls, nom, prenom, cin, filiere, matricule):
        return cls(nom, prenom, cin, filiere, matricule)

    @classmethod
    def mofidierProfesseur(
        cls, cin, newNom, newPrenom, newCin, newFiliere, newMatricule
    ):
        for i in Professeur.professeurs:
            if i["cin"] == cin:
                i["nom"] = newNom
                i["prenom"] = newPrenom
                i["cin"] = newCin
                i["filiere"] = newFiliere
                i["matricule"] = newMatricule
            with open("./data.json", "r") as file:
                data = json.load(file)
            data["professeurs"] = Professeur.professeurs
            with open("./data.json", "w") as file:
                json.dump(data, file, indent=2)

    @property
    def filiere(self):
        return self.__filiere

    @filiere.setter
    def filiere(self, value):
        self.__filiere = value

    @property
    def matricule(self):
        return self.__matricule

    @matricule.setter
    def matricule(self, value):
        self.__matricule = value


l = Professeur.ajouterProfesseur("jeniah", "adam", "kb243538", "dev", "1234")
m = Professeur.ajouterProfesseur("mrabet", "anas", "kb243348", "pc", "7600")
last = Professeur.ajouterProfesseur(
    "mbape", "jeniah", "123riyah", "ball", "kooraforlife"
)
# print(l.matricule)


class Responsable(Person):
    responsables = []

    def __init__(self, nom, prenom, cin, responsabilite, matricule):
        self.__responsabilite = responsabilite
        self.__matricule = matricule
        super().__init__(nom, prenom, cin)
        Responsable.responsables.append(
            {
                "nom": nom,
                "prenom": prenom,
                "cin": cin,
                "responsabilite": responsabilite,
                "matricule": matricule,
            }
        )

    def supprimerResponsable(cin):
        for i in Responsable.responsables:
            if i["cin"] == cin:
                Responsable.responsables.remove(i)

    @classmethod
    def ajouterResponsable(cls, nom, prenom, cin, responsabilite, matricule):
        return cls(nom, prenom, cin, responsabilite, matricule)

    @classmethod
    def mofidierResponsable(
        cls, cin, newNom, newPrenom, newCin, newResponsabilite, newMatricule
    ):
        for i in Professeur.professeurs:
            if i["cin"] == cin:
                i["nom"] = newNom
                i["prenom"] = newPrenom
                i["cin"] = newCin
                i["responsabilite"] = newResponsabilite
                i["matricule"] = newMatricule

    @property
    def responsabilite(self):
        return self.__responsabilite

    @responsabilite.setter
    def responsabilite(self, value):
        self.__responsabilite = value

    @property
    def matricule(self):
        return self.__matricule

    @matricule.setter
    def matricule(self, value):
        self.__matricule = value


# x = Responsable("jeniah", "adam", "kb243538", "biba", "1234")

# print(x.responsabilite)


class Utilisateur:
    utils = []

    # Write the new data to the JSON file
    def __init__(self, login, password, email):
        self.__login = login
        self.__password = password
        self.__email = email
        Utilisateur.utils.append({"login": login, "password": password, "email": email})
        # For adding the data to the json file

        with open("./data.json", "r") as file:
            data = json.load(file)

            data["utilisateurs"] = Utilisateur.utils

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    def supprimerUtilisateur(login):
        for i in Utilisateur.utils:
            if i["login"] == login:
                Utilisateur.utils.remove(i)
        with open("./data.json", "r") as file:
            data = json.load(file)
        data["utilisateurs"] = Utilisateur.utils

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    @classmethod
    def ajouterUtilisateur(cls, login, password, email):
        return cls(login, password, email)

    @classmethod
    def mofidierUtilisateur(cls, login, newLogin, newPassword, newEmail):
        for i in Utilisateur.utils:
            if i["login"] == login:
                i["login"] = newLogin
                i["password"] = newPassword
                i["email"] = newEmail

    @classmethod
    def authentifier(cls, login, password):
        f = open("./data.json", "r")
        for i in json.load(f)["utilisateurs"]:
            if i["login"] == login:
                if i["password"] == password:
                    return True
                else:
                    return False
        return "You're Not a User"

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        self.__login = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value


utilOne = Utilisateur("adam04", "123456", "jeniahadam@gmail.com")
utileTwo = Utilisateur("med07", "789456", "med@gmail.com")
utileThre = Utilisateur("jeniah", "7500", "jeniah7500@gmail.com")
utileFoor = Utilisateur("mosaab", "5550", "mosaab5550@gmail.com")
utileFive = Utilisateur.ajouterUtilisateur("mohamed", "4444", "mohamed4444@gmail.com")
utileSix = Utilisateur.ajouterUtilisateur("Yasser", "3333", "yasser3333@gmail.com")

# Utilisateur.supprimerUtilisateur("mosaab")
# Utilisateur.supprimerUtilisateur("jeniah")
# print(Utilisateur.authentifier("med07", "789456"))


class Seance:
    seances = []

    def __init__(self, idSeance, professeur, matiere, salle, dateSeance):
        self.__idSeance = idSeance
        self.__professeur = professeur
        self.__matiere = matiere
        self.__salle = salle
        self.__datSeance = dateSeance
        with open("./data.json", "r") as file:
            ar = json.load(file)["seances"]
            # print(ar)
        Seance.seances.append(
            {
                "idSeance": idSeance,
                "professeur": professeur.matricule,
                "matiere": matiere.idMatiere,
                "salle": salle.idSalle,
                "dateSeance": dateSeance,
            }
        )
        with open("./data.json", "r") as file:
            data = json.load(file)
            data["seances"] = Seance.seances

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    # supprimer une seance
    def supprimerSeance(idSeance):
        with open("./data.json", "r") as file:
            ar = json.load(file)["seances"]
            for i in ar:
                if i["idSeance"] == idSeance:
                    ar.remove(i)

        with open("./data.json", "r") as file:
            data = json.load(file)
        data["seances"] = ar

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    # ajouter une seance
    @classmethod
    def ajouterSeance(cls, idSeance, professeur, matiere, salle, dateSeance):
        return cls(idSeance, professeur, matiere, salle, dateSeance)

    # modifier une seance
    @classmethod
    def modifierSeance(
        cls, idSeance, newIdSeance, newProfesseur, newMatiere, newSalle, newDateSeance
    ):
        with open("./data.json", "r") as file:
            ar = json.load(file)["seances"]
        for i in ar:
            if i["idSeance"] == idSeance:
                i["idSeance"] = newIdSeance
                i["professeur"] = newProfesseur["matricule"]
                i["matiere"] = newMatiere["idMatiere"]
                i["salle"] = newSalle["idSalle"]
                i["dateSeance"] = newDateSeance

        with open("./data.json", "r") as file:
            data = json.load(file)
            data["seances"] = ar
        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    # afficher les séances attribuées à un professeur
    @classmethod
    def afficherSeanceProfesseur(cls, matricule):
        ar = []
        for i in Seance.seances:
            if i["professeur"] == matricule:
                ar.append(i)

        with open("./data.json", "r") as file:
            data = json.load(file)
            for i in data["seances"]:
                if i["professeur"] == matricule:
                    ar.append(i)
        return ar

    @classmethod
    def afficherSalleDispo(cls, idSalle, date):
        all = []
        for i in cls.seances:
            if i["salle"] == idSalle:
                all.append(i["dateSeance"])
        if date in all:
            return False
        else:
            return True

    @property
    def idSeance(self):
        return self.__idSeance

    @idSeance.setter
    def idSeance(self, value):
        self.__idSeance = value

    @property
    def professeur(self):
        return self.__professeur

    @professeur.setter
    def professeur(self, value):
        self.__professeur = value

    @property
    def matiere(self):
        return self.__matiere

    @matiere.setter
    def matiere(self, value):
        self.__matiere = value

    @property
    def salle(self):
        return self.__salle

    @salle.setter
    def salle(self, value):
        self.__salle = value

    @property
    def dateSeance(self):
        return self.__datSeance

    @dateSeance.setter
    def dateSeance(self, value):
        self.__datSeance = value

    def __str__(self):
        return f"la seance de l'id {self.idSeance}, de professeur {self.professeur}, de matiere {self.matiere}, dans la salle {self.matiere}, et dans le {self.dateSeance}"


f = Seance("fSeance", l, matiereOne, saleOne, "24/06/2024")
g = Seance("gSeance", l, matiereTwo, saleTwo, "25/06/2024")
n = Seance("nSeance", m, matiereOne, saleThree, "30/07/2024")
m = Seance("mSeance", m, matiereOne, saleThree, "23/05/2024")
scd = Seance.ajouterSeance("secondSeance", last, matiereTwo, saleThree, "20/25/2024")

# lt = Seance.ajouterSeance("lstSeanct", l, matiereOne, saleThree, "05/02/2024")


# Les interfaces graphique

# 1. Interface Authentification :

import tkinter as tk
from tkinter.font import Font
import customtkinter as ctk
from tkinter import ttk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")


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
        input_frame = ctk.CTkFrame(self, width=400, height=450, fg_color="#eaeaea")
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

        global hide_error

        def hide_error():
            error_label.place_forget()

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
                # import acceuil
            elif Utilisateur.authentifier(get_login, get_password) == False:
                make_error(frameTwo, "Incorrect Password", 333, colorInvalid)
            else:
                print(Utilisateur.authentifier(get_login, get_password))
                make_error(frameOne, "Incorrect Login", 360, colorInvalid)
        except:
            print("Error for the hide function")

        # print(f"login: {get_login}")
        # print(f"Password: {get_password}")


Login().mainloop()


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
        table.heading("professeur", text="Professeur matricule")
        table.heading("matiere", text="Matiere id")
        table.heading("salle", text="Salle id")
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
        pro = [i["professeur"] for i in self.get_data_from_json()]
        mats = [i["matiere"] for i in self.get_data_from_json()]
        sals = [i["salle"] for i in self.get_data_from_json()]
        newId = value_entry_idSeance.get()
        newPro = value_entry_professeur.get()
        newMatiere = value_entry_matiere.get()
        newSalle = value_entry_salle.get()
        newDate = value_entry_date.get()

        # newDate = value
        if value_entry_mod.get() in aridSeance:
            error_mod.place_forget()
            # For the new id checking
            if newId == "nouveau id" or newId == "" or newId in aridSeance:
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
            if newDate == "nouvelle date" or newSalle == "" or state == False:
                error_date.place(relx=0.5, anchor="center", y=550)
            elif state == True:
                error_date.place_forget()
                final.append(newDate)

            Seance.modifierSeance(
                value_entry_mod.get(), final[0], final[1], final[2], final[3], final[4]
            )
            table.delete(*table.get_children())
            for i in self.get_data_from_json():
                table.insert(parent="", index="end", values=list(i.values()))

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

        entry_filter = ctk.CTkEntry(
            frame_bar,
            text_color=Home.color,
            font=(Home.font, 14),
            fg_color="#f8f8f8",
            height=35,
            width=300,
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
        )
        button_filter.place(y=30, x=600)
        button_filter.configure(cursor="hand2")

    def get_data_from_json(self):       
        with open("./data.json", "r") as f:
            return json.load(f)["seances"]


a = Home().mainloop()
