import json
from pymongo import *


class Utilisateur:
    client = MongoClient(
        "mongodb://localhost:27017/"
    )  # Replace with your MongoDB connection string
    db = client["center-formation"]  # Database name
    collection = db["utilisateurs"]  # Collection name

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
        with open("./data.json", "r") as file:
            ar = json.load(file)["utilisateurs"]
            for i in ar:
                if i["login"] == login:
                    ar.remove(i)
        with open("./data.json", "r") as file:
            data = json.load(file)
        data["utilisateurs"] = ar

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    @classmethod
    def ajouterUtilisateur(cls, login, password, email):
        with open("./data.json", "r") as f:
            data = json.load(f)
        ar = data["utilisateurs"]
        # logins = [i["login"] for i in ar]
        # for filtring the new data is the same to the old data
        # if login not in logins:
        ar.append({"login": login, "password": password, "email": email})

        data["utilisateurs"] = ar
        with open("./data.json", "w") as f:
            json.dump(data, f, indent=2)

    @classmethod
    def mofidierUtilisateur(cls, login, newLogin, newPassword, newEmail):
        with open("./data.json", "r") as file:
            ar = json.load(file)["utilisateurs"]
        for i in ar:
            if i["login"] == login:
                i["login"] = newLogin
                i["password"] = newPassword
                i["email"] = newEmail

        with open("./data.json", "r") as file:
            data = json.load(file)
            data["utilisateurs"] = ar
        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

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
