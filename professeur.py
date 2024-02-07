import json
from person import Person
from seance import Seance


class Professeur(Person):
    professeurs = []

    def __init__(self, nom, prenom, cin, filiere, matricule):
        self.__filiere = filiere
        self.__matricule = matricule
        super().__init__(nom, prenom, cin)
        Professeur.professeurs.append(
            {
                "nom": nom,
                "prenom": prenom,
                "cin": cin,
                "filiere": filiere,
                "matricule": matricule,
            }
        )
        with open("./data.json", "r") as file:
            data = json.load(file)

            data["professeurs"] = Professeur.professeurs

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    def supprimerProfesseur(cin):
        with open("./data.json", "r") as file:
            ar = json.load(file)["professeurs"]
            for i in ar:
                if i["cin"] == cin:
                    ar.remove(i)
        with open("./data.json", "r") as file:
            data = json.load(file)
        data["professeurs"] = ar

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    @classmethod
    def ajouterProfesseur(cls, nom, prenom, cin, filiere, matricule):
        with open("./data.json", "r") as f:
            data = json.load(f)
        ar = data["professeurs"]
        ar.append(
            {
                "nom": nom,
                "prenom": prenom,
                "cin": cin,
                "filiere": filiere,
                "matricule": matricule,
            }
        )

        data["professeurs"] = ar
        with open("./data.json", "w") as f:
            json.dump(data, f, indent=2)

    @classmethod
    def mofidierProfesseur(
        cls, cin, newNom, newPrenom, newCin, newFiliere, newMatricule
    ):
        with open("./data.json", "r") as file:
            arS = json.load(file)["seances"]
        with open("./data.json", "r") as file:
            ar = json.load(file)["professeurs"]

        for i in ar:
            if i["cin"] == cin:
                ele = i["matricule"]
                i["nom"] = newNom
                i["prenom"] = newPrenom
                i["cin"] = newCin
                i["filiere"] = newFiliere
                i["matricule"] = newMatricule
        for i in arS:
            if i["professeur"] == ele:
                seM = i
            else:
                False

        with open("./data.json", "r") as file:
            data = json.load(file)
            data["professeurs"] = ar
        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

        # for the modification of the seance salle
        Seance.modifierSeance(
            seM["idSeance"],
            seM["idSeance"],
            {
                "nom": "biba",
                "prenom": "khawa",
                "cin": "adlfk",
                "filiere": "adfas",
                "matricule": newMatricule,
            },
            {
                "idMatiere": seM["matiere"],
                "libelle": "pour la langue francaise",
                "langue": "Francais",
            },
            {"idSalle": seM["salle"], "libelle": "libelle", "numero": "numero"},
            seM["dateSeance"],
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
