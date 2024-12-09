from pymongo import MongoClient

class Person:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["center-formation"]
    collection = db["personnes"]

    def __init__(self, nom, prenom, cin):
        self._nom = nom
        self._prenom = prenom
        self._cin = cin

    @classmethod
    def supprimerPerson(cls, cin):
        cls.collection.delete_one({"cin": cin})

    @classmethod
    def ajouterPerson(cls, nom, prenom, cin):
        cls.collection.insert_one({"cin": cin, "nom": nom, "prenom": prenom})

    @classmethod
    def mofidierPerson(cls, cin, newNom, newPrenom, newCin):
        cls.collection.update_one(
            {"cin": cin}, {"$set": {"nom": newNom, "prenom": newPrenom, "cin": newCin}}
        )

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
