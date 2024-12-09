from pymongo import MongoClient

class Salle:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["center-formation"]
    collection = db["salles"]

    def __init__(self, idSalle, libelle, numero):
        self.__idSalle = idSalle
        self.__libelle = libelle
        self.__numero = numero

    @classmethod
    def supprimerSalle(cls, idSalle):
        cls.collection.delete_one({"_id": idSalle})

    @classmethod
    def ajouterSalle(cls, idSalle, libelle, numero):
        cls.collection.insert_one(
            {"_id": idSalle, "libelle": libelle, "numero": numero}
        )

    @classmethod
    def modifierSalle(cls, idSalle, newIdSalle, newLibelle, newNumero):
        cls.collection.update_one(
            {"_id": idSalle},
            {
                "$set": {
                    "idSalle": newIdSalle,
                    "libelle": newLibelle,
                    "numero": newNumero,
                }
            },
        )

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
        return f"La salle de l'id {self.idSalle}, de libelle {self.libelle}, et de numero {self.numero}"
