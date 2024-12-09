from pymongo import MongoClient
from datetime import datetime


class Seance:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["center-formation"]
    collection = db["seances"]

    def __init__(self, idSeance, prof_id, matiere_id, salle_id, dateSeance):
        self.__idSeance = idSeance
        self.__prof_id = prof_id
        self.__matiere_id = matiere_id
        self.__salle_id = salle_id
        self.__dateSeance = dateSeance

    @classmethod
    def supprimerSeance(cls, idSeance):
        result = cls.collection.delete_one({"_id": idSeance})
        if result.deleted_count == 0:
            raise ValueError(f"No seance found with id {idSeance}")

    @classmethod
    def ajouterSeance(cls, idSeance, prof_id, matiere_id, salle_id, dateSeance):
        cls.collection.insert_one(
            {
                "_id": idSeance,
                "prof_id": prof_id,
                "matiere_id": matiere_id,
                "salle_id": salle_id,
                "dateSeance": dateSeance,
            }
        )

    @classmethod
    def modifierSeance(
        cls,
        idSeance,
        newDateSeance,
    ):
        result = cls.collection.update_one(
            {"_id": idSeance},
            {
                "$set": {
                    "dateSeance": newDateSeance,
                }
            },
        )
        if result.matched_count == 0:
            raise ValueError(f"No seance found with id {idSeance}")

    @classmethod
    def afficherSeanceProfesseur(cls, prof_id):
        seances = cls.collection.find({"prof_id": prof_id})
        return list(seances)

    @classmethod
    def afficherSalleDispo(cls, salle_id, date):
        seance = cls.collection.find_one({"salle_id": salle_id, "dateSeance": date})
        return seance is None

    @property
    def idSeance(self):
        return self.__idSeance

    @idSeance.setter
    def idSeance(self, value):
        self.__idSeance = value

    @property
    def prof_id(self):
        return self.__prof_id

    @prof_id.setter
    def prof_id(self, value):
        self.__prof_id = value

    @property
    def matiere_id(self):
        return self.__matiere_id

    @matiere_id.setter
    def matiere_id(self, value):
        self.__matiere_id = value

    @property
    def salle_id(self):
        return self.__salle_id

    @salle_id.setter
    def salle_id(self, value):
        self.__salle_id = value

    @property
    def dateSeance(self):
        return self.__dateSeance

    @dateSeance.setter
    def dateSeance(self, value):
        self.__dateSeance = value

    def __str__(self):
        return (
            f"La séance avec l'id {self.idSeance}, professeur {self.prof_id}, "
            f"matière {self.matiere_id}, dans la salle {self.salle_id}, "
            f"est prévue le {self.dateSeance}."
        )
