from pymongo import MongoClient


class Matiere:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["center-formation"]
    collection = db["matieres"]

    def __init__(self, idMatiere, libelle, langue):
        self.__idMatiere = idMatiere
        self.__libelle = libelle
        self.__langue = langue

    @classmethod
    def supprimerMatiere(cls, idMatiere):
        cls.collection.delete_one({"_id": idMatiere})

    @classmethod
    def ajouterMatiere(cls, idMatiere, libelle, langue):
        cls.collection.insert_one(
            {
                "_id": idMatiere,
                "libelle": libelle,
                "langue": langue,
            }
        )

    @classmethod
    def mofidierMatiere(cls, idMatiere, newLibelle, newLangue):
        cls.collection.update_one(
            {"_id": idMatiere},
            {
                "$set": {
                    "libelle": newLibelle,
                    "langue": newLangue,
                }
            },
            0.0,
        )

    @classmethod
    def getAllMatieres(cls):
        # Retrieve all matieres from MongoDB
        return list(cls.collection.find({}))

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
        self.__langue = value

    def __str__(self):
        return f"La matiere de l'id {self.idMatiere} de libelle {self.libelle}, et de langue {self.langue}"
