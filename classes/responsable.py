from classes.person import Person
import json


class Responsable(Person):
    responsables = []

    def __init__(self, nom, prenom, cin, responsabilite, matricule):
        self.__responsabilite = responsabilite
        self.__matricule = matricule
        super().__init__(nom, prenom, cin)
        Responsable.responsables.append(
            {
                "nom": nom,
                "prenom": prenom,
                "cin": cin,
                "responsabilite": responsabilite,
                "matricule": matricule,
            }
        )
        with open("./data.json", "r") as file:
            data = json.load(file)

            data["professeurs"] = Responsable.responsables

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    def supprimerResponsable(cin):
        with open("./data.json", "r") as file:
            ar = json.load(file)["responsables"]
            for i in ar:
                if i["cin"] == cin:
                    ar.remove(i)
        with open("./data.json", "r") as file:
            data = json.load(file)
        data["responsables"] = ar

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    @classmethod
    def ajouterResponsable(cls, nom, prenom, cin, responsabilite, matricule):
        with open("./data.json", "r") as f:
            data = json.load(f)
        ar = data["responsables"]
        matricules = [i["matricule"] for i in ar]
        # for filtring the new data is the same to the old data
        if matricule not in matricules:
            ar.append(
                {
                    "nom": nom,
                    "prenom": prenom,
                    "cin": cin,
                    "responsabilite": responsabilite,
                    "matricule": matricule,
                }
            )

        data["responsables"] = ar
        with open("./data.json", "w") as f:
            json.dump(data, f, indent=2)

    @classmethod
    def mofidierResponsable(
        cls, cin, newNom, newPrenom, newCin, newResponsabilite, newMatricule
    ):
        with open("./data.json", "r") as file:
            ar = json.load(file)["responsables"]
        for i in ar:
            if i["cin"] == cin:
                if i["cin"] == cin:
                    i["nom"] = newNom
                    i["prenom"] = newPrenom
                    i["cin"] = newCin
                    i["responsabilite"] = newResponsabilite
                    i["matricule"] = newMatricule
        with open("./data.json", "r") as file:
            data = json.load(file)
            data["responsables"] = ar
        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    @property
    def responsabilite(self):
        return self.__responsabilite

    @responsabilite.setter
    def responsabilite(self, value):
        self.__responsabilite = value

    @property
    def matricule(self):
        return self.__matricule

    @matricule.setter
    def matricule(self, value):
        self.__matricule = value


# s = Responsable.ajouterResponsable("mohamed", "jeniah", "kb234", "etudiant", "1234")r
