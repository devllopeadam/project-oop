import json

from classes.seance import Seance


class Salle:
    salles = []

    def __init__(self, idSalle, libelle, numero):
        self.__idSalle = idSalle
        self.__libelle = libelle
        self.__numero = numero

        Salle.salles.append({"idSalle": idSalle, "libelle": libelle, "numero": numero})

        with open("./data.json", "r") as file:
            data = json.load(file)

            data["salles"] = Salle.salles

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    # to delete a salle from the salles list
    def supprimerSalle(idSalle):
        with open("./data.json", "r") as file:
            ar = json.load(file)["salles"]
            for i in ar:
                if i["idSalle"] == idSalle:
                    ar.remove(i)
        with open("./data.json", "r") as file:
            data = json.load(file)
        data["salles"] = ar

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    # to add a salle to the salle list
    @classmethod
    def ajouterSalle(cls, idSalle, libelle, numero):
        with open("./data.json", "r") as f:
            data = json.load(f)
        ar = data["salles"]
        ar.append({"idSalle": idSalle, "libelle": libelle, "numero": numero})

        data["salles"] = ar
        with open("./data.json", "w") as f:
            json.dump(data, f, indent=2)

    # to modify the salle
    @classmethod
    def mofidierSalle(cls, idSalle, newIdSalle, newLibelle, newNumero):
        allSalle = []
        with open("./data.json", "r") as file:
            ar = json.load(file)["seances"]
        for i in ar:
            if i["salle"] == idSalle:
                allSalle.append(i)
        # for the modification of the salle
        with open("./data.json", "r") as file:
            ar = json.load(file)["salles"]
        for i in ar:
            if i["idSalle"] == idSalle:
                i["idSalle"] = newIdSalle
                i["libelle"] = newLibelle
                i["numero"] = newNumero

        with open("./data.json", "r") as file:
            data = json.load(file)
            data["salles"] = ar
        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)
        # for the modification of the seance salle
        for i in allSalle:
            Seance.modifierSeance(
                i["idSeance"],
                i["idSeance"],
                {
                    "nom": "any",
                    "prenom": "any",
                    "cin": "any",
                    "filiere": "any",
                    "matricule": i["professeur"],
                },
                {
                    "idMatiere": i["matiere"],
                    "libelle": "any",
                    "langue": "any",
                },
                {"idSalle": newIdSalle, "libelle": "any", "numero": "any"},
                i["dateSeance"],
            )

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
