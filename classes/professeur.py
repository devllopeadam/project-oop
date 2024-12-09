from pymongo import MongoClient
import json
from classes.person import Person
from classes.seance import Seance


class Professeur(Person):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["center-formation"]
    collection = db["professeurs"]

    def __init__(self, nom, prenom, cin, filiere, matricule):
        self.__filiere = filiere
        self.__matricule = matricule
        super().__init__(nom, prenom, cin)

    @classmethod
    def supprimerProfesseur(cls, matricule):
        cls.collection.delete_one({"matricule": matricule})

    @classmethod
    def ajouterProfesseur(cls, nom, prenom, cin, filiere, matricule):
        cls.collection.insert_one(
            {
                "_id": matricule,
                "nom": nom,
                "prenom": prenom,
                "cin": cin,
                "filiere": filiere,
            }
        )

    @classmethod
    def mofidierProfesseur(cls, matricule, newNom, newPrenom, newCin, newFiliere):
        cls.collection.update_one(
            {"matricule": matricule},
            {
                "$set": {
                    "nom": newNom,
                    "prenom": newPrenom,
                    "cin": newCin,
                    "filiere": newFiliere,
                }
            },
        )

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
