from person import Person
import json


class Apprenant(Person):
    apprenants = []

    def __init__(self, nom, prenom, cin, niveau, age):
        self.__niveau = niveau
        self.__age = age
        super().__init__(nom, prenom, cin)
        Apprenant.apprenants.append(
            {"nom": nom, "prenom": prenom, "cin": cin, "niveau": niveau, "age": age}
        )

        with open("./data.json", "r") as file:
            data = json.load(file)

            data["apprenants"] = self.apprenants

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    def supprimerApprenant(cin):
        with open("./data.json", "r") as file:
            ar = json.load(file)["apprenants"]
            for i in ar:
                if i["cin"] == cin:
                    ar.remove(i)
        with open("./data.json", "r") as file:
            data = json.load(file)
        data["apprenants"] = ar

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    @classmethod
    def ajouterApprenant(cls, nom, prenom, cin, niveau, age):
        with open("./data.json", "r") as f:
            data = json.load(f)
        ar = data["apprenants"]
        for i in ar:
            if i["cin"] != cin:
                print(i)
                ar.append(
                    {
                        "nom": nom,
                        "prenom": prenom,
                        "cin": cin,
                        "niveau": niveau,
                        "age": age,
                    }
                )

        data["apprenants"] = ar
        with open("./data.json", "w") as f:
            json.dump(data, f, indent=2)

    @classmethod
    def mofidierApprenant(cls, cin, newNom, newPrenom, newCin, newNiveau, newAge):
        with open("./data.json", "r") as file:
            ar = json.load(file)["apprenants"]
        for i in ar:
            if i["cin"] == cin:
                i["nom"] = newNom
                i["prenom"] = newPrenom
                i["cin"] = newCin
                i["niveau"] = newNiveau
                i["age"] = newAge
        with open("./data.json", "r") as file:
            data = json.load(file)
            data["apprenants"] = ar
        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    @property
    def niveau(self):
        return self.__niveau

    @niveau.setter
    def niveau(self, value):
        self.__niveau = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value


Apprenant.ajouterApprenant("jeniah", "prenom", "kb248", "2anne", 19)
