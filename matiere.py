import json
from seance import Seance


class Matiere:
    matieres = []

    def __init__(self, idMatiere, libelle, langue):
        self.__idMatiere = idMatiere
        self.__libelle = libelle
        self.__langue = langue

        # Pour Lister Tout les matieres

        Matiere.matieres.append(
            {
                "idMatiere": idMatiere,
                "libelle": libelle,
                "langue": langue,
            }
        )
        with open("./data.json", "r") as file:
            data = json.load(file)

            data["matieres"] = Matiere.matieres

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    # to delete a specific matiere using the idMatiere
    def supprimerMatiere(idMatiere):
        with open("./data.json", "r") as file:
            ar = json.load(file)["matieres"]
            for i in ar:
                if i["idMatiere"] == idMatiere:
                    ar.remove(i)
        with open("./data.json", "r") as file:
            data = json.load(file)
        data["matieres"] = ar

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    # to add a matiere to the matieres list
    @classmethod
    def ajouterMatiere(cls, idMatiere, libelle, langue):
        with open("./data.json", "r") as f:
            data = json.load(f)
        ar = data["matieres"]
        ar.append(
            {
                "idMatiere": idMatiere,
                "libelle": libelle,
                "langue": langue,
            }
        )

        data["matieres"] = ar
        with open("./data.json", "w") as f:
            json.dump(data, f, indent=2)

    # to modify the matiere
    @classmethod
    def mofidierMatiere(cls, idMatiere, newIdMatiere, newLibelle, newLangue):
        allSea = []
        with open("./data.json", "r") as file:
            arS = json.load(file)["seances"]
        for i in arS:
            if i["matiere"] == idMatiere:
                allSea.append(i)

        with open("./data.json", "r") as file:
            ar = json.load(file)["matieres"]
        for i in ar:
            if i["idMatiere"] == idMatiere:
                i["idMatiere"] = newIdMatiere
                i["libelle"] = newLibelle
                i["langue"] = newLangue

        with open("./data.json", "r") as file:
            data = json.load(file)
            data["matieres"] = ar
        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

        for i in allSea:
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
                    "idMatiere": newIdMatiere,
                    "libelle": "any",
                    "langue": "any",
                },
                {"idSalle": i["salle"], "libelle": "any", "numero": "any"},
                i["dateSeance"],
            )

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
