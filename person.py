class Person:
    personnes = []

    def __init__(self, nom, prenom, cin):
        self._nom = nom
        self._prenom = prenom
        self._cin = cin
        Person.personnes.append({"nom": nom, "prenom": prenom, "cin": cin})

    # to delete a salle from the personnes list

    def supprimerPerson(cin):
        for i in Person.personnes:
            if i["cin"] == cin:
                Person.personnes.remove(i)

    @classmethod
    def ajouterPerson(cls, nom, prenom, cin):
        return cls(nom, prenom, cin)

    @classmethod
    def mofidierPerson(cls, cin, newNom, newPrenom, newCin):
        for i in Person.personnes:
            if i["cin"] == cin:
                i["nom"] = newNom
                i["prenom"] = newPrenom
                i["cin"] = newCin

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, value):
        self._prenom = value

    @property
    def cin(self):
        return self._cin

    @cin.setter
    def cin(self, value):
        self._cin = value

    def __str__(self) -> str:
        return (
            f"la person du nom {self.nom} du prenom {self.prenom}, et du cin {self.cin}"
        )
