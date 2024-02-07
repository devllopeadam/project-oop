import json
from datetime import datetime


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
                "professeur": professeur["matricule"],
                "matiere": matiere["idMatiere"],
                "salle": salle["idSalle"],
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
        with open("./data.json", "r") as f:
            data = json.load(f)
        ar = data["seances"]
        ar.append(
            {
                "idSeance": idSeance,
                "professeur": professeur["matricule"],
                "matiere": matiere["idMatiere"],
                "salle": salle["idSalle"],
                "dateSeance": dateSeance,
            }
        )

        data["seances"] = ar
        with open("./data.json", "w") as f:
            json.dump(data, f, indent=2)

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
        with open("./data.json", "r") as file:
            data = json.load(file)
            for i in data["seances"]:
                if i["professeur"] == matricule:
                    ar.append(i)
        return ar

    @classmethod
    def afficherSalleDispo(cls, idSalle, date):
        ar = []
        with open("./data.json", "r") as file:
            data = json.load(file)["seances"]
        for i in data:
            if i["salle"] == idSalle:
                ar.append(i["dateSeance"])
        if date in ar:
            return True
        else:
            return False

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
