from pymongo import MongoClient


class Utilisateur:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["center-formation"]
    collection = db["utilisateurs"]

    def __init__(self, username, password, email):
        self.__username = username
        self.__password = password
        self.__email = email

    @classmethod
    def supprimerUtilisateur(cls, username):
        cls.collection.delete_one({"username": username})

    @classmethod
    def ajouterUtilisateur(cls, username, password, email):
        cls.collection.insert_one(
            {"username": username, "password": password, "email": email}
        )

    @classmethod
    def mofidierUtilisateur(cls, username, newusername, newPassword, newEmail):
        Utilisateur.collection.update_one(
            {"username": username},
            {
                "$set": {
                    "username": newusername,
                    "password": newPassword,
                    "email": newEmail,
                }
            },
        )

    @classmethod
    def authentifier(cls, username, password):
        user = cls.collection.find_one({"username": username})
        if user:
            if user["password"] == password:
                return True
            else:
                return False
        return "You're Not a User"

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

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
