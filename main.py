import json
import re


# class Matiere
class Matiere:
    matieres = []

    def __init__(self, idMatiere, libelle, langue):
        self.__idMatiere = idMatiere
        self.__libelle = libelle
        self.__langue = langue

        # Pour Lister Tout les matieres

        Matiere.matieres.append(
            {
                "idMatiere": self.idMatiere,
                "libelle": self.libelle,
                "langue": self.langue,
            }
        )
        with open("./data.json", "r") as file:
            data = json.load(file)

            data["matieres"] = Matiere.matieres

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    # to delete a specific matiere using the idMatiere
    def supprimerMatiere(idMatiere):
        for i in Matiere.matieres:
            if i["idMatiere"] == idMatiere:
                Matiere.matieres.remove(i)
        with open("./data.json", "r") as file:
            data = json.load(file)
        data["matieres"] = Matiere.matieres

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    # to add a matiere to the matieres list
    @classmethod
    def ajouterMatiere(cls, idMatiere, libelle, langue):
        return cls(idMatiere, libelle, langue)

    # to modify the matiere
    @classmethod
    def mofidierMatiere(cls, idMatiere, newIdMatiere, newLibelle, newLangue):
        for i in Matiere.matieres:
            if i["idMatiere"] == idMatiere:
                i["idMatiere"] = newIdMatiere
                i["libelle"] = newLibelle
                i["langue"] = newLangue
            with open("./data.json", "r") as file:
                data = json.load(file)
            data["matieres"] = Matiere.matieres
            with open("./data.json", "w") as file:
                json.dump(data, file, indent=2)

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
        for i in Salle.salles:
            if i["idSalle"] == idSalle:
                Salle.salles.remove(i)
        with open("./data.json", "r") as file:
            data = json.load(file)
        data["salles"] = Salle.salles

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
        for i in Salle.salles:
            if i["idSalle"] == idSalle:
                i["idSalle"] = newIdSalle
                i["libelle"] = newLibelle
                i["numero"] = newNumero
            with open("./data.json", "r") as file:
                data = json.load(file)
            data["salles"] = Salle.salles
            with open("./data.json", "w") as file:
                json.dump(data, file, indent=2)

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


class Apprenant(Person):
    apprenants = []

    def __init__(self, nom, prenom, cin, niveau, age):
        self.__niveau = niveau
        self.__age = age
        super().__init__(nom, prenom, cin)
        Apprenant.apprenants.append(
            {"nom": nom, "prenom": prenom, "cin": cin, "niveau": niveau, "age": age}
        )

    def supprimerApprenant(cin):
        for i in Apprenant.apprenants:
            if i["cin"] == cin:
                Apprenant.apprenants.remove(i)

    @classmethod
    def ajouterApprenant(cls, nom, prenom, cin, niveau, age):
        return cls(nom, prenom, cin, niveau, age)

    @classmethod
    def mofidierApprenant(cls, cin, newNom, newPrenom, newCin, newNiveau, newAge):
        for i in Apprenant.apprenants:
            if i["cin"] == cin:
                i["nom"] = newNom
                i["prenom"] = newPrenom
                i["cin"] = newCin
                i["niveau"] = newNiveau
                i["age"] = newAge

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
        for i in Professeur.professeurs:
            if i["cin"] == cin:
                Professeur.professeurs.remove(i)

        with open("./data.json", "r") as file:
            data = json.load(file)
        data["professeurs"] = Professeur.professeurs

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    @classmethod
    def ajouterProfesseur(cls, nom, prenom, cin, filiere, matricule):
        return cls(nom, prenom, cin, filiere, matricule)

    @classmethod
    def mofidierProfesseur(
        cls, cin, newNom, newPrenom, newCin, newFiliere, newMatricule
    ):
        for i in Professeur.professeurs:
            if i["cin"] == cin:
                i["nom"] = newNom
                i["prenom"] = newPrenom
                i["cin"] = newCin
                i["filiere"] = newFiliere
                i["matricule"] = newMatricule
            with open("./data.json", "r") as file:
                data = json.load(file)
            data["professeurs"] = Professeur.professeurs
            with open("./data.json", "w") as file:
                json.dump(data, file, indent=2)

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

    def supprimerResponsable(cin):
        for i in Responsable.responsables:
            if i["cin"] == cin:
                Responsable.responsables.remove(i)

    @classmethod
    def ajouterResponsable(cls, nom, prenom, cin, responsabilite, matricule):
        return cls(nom, prenom, cin, responsabilite, matricule)

    @classmethod
    def mofidierResponsable(
        cls, cin, newNom, newPrenom, newCin, newResponsabilite, newMatricule
    ):
        for i in Professeur.professeurs:
            if i["cin"] == cin:
                i["nom"] = newNom
                i["prenom"] = newPrenom
                i["cin"] = newCin
                i["responsabilite"] = newResponsabilite
                i["matricule"] = newMatricule

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


class Utilisateur:
    utils = []

    # Write the new data to the JSON file
    def __init__(self, login, password, email):
        self.__login = login
        self.__password = password
        self.__email = email
        Utilisateur.utils.append({"login": login, "password": password, "email": email})
        # For adding the data to the json file

        with open("./data.json", "r") as file:
            data = json.load(file)

            data["utilisateurs"] = Utilisateur.utils

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    def supprimerUtilisateur(login):
        for i in Utilisateur.utils:
            if i["login"] == login:
                Utilisateur.utils.remove(i)
        with open("./data.json", "r") as file:
            data = json.load(file)
        data["utilisateurs"] = Utilisateur.utils

        with open("./data.json", "w") as file:
            json.dump(data, file, indent=2)

    @classmethod
    def ajouterUtilisateur(cls, login, password, email):
        return cls(login, password, email)

    @classmethod
    def mofidierUtilisateur(cls, login, newLogin, newPassword, newEmail):
        for i in Utilisateur.utils:
            if i["login"] == login:
                i["login"] = newLogin
                i["password"] = newPassword
                i["email"] = newEmail

    @classmethod
    def authentifier(cls, login, password):
        f = open("./data.json", "r")
        for i in json.load(f)["utilisateurs"]:
            if i["login"] == login:
                if i["password"] == password:
                    return True
                else:
                    return False
        return "You're Not a User"

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        self.__login = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value


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
                "professeur": professeur.matricule,
                "matiere": matiere.idMatiere,
                "salle": salle.idSalle,
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
        return cls(idSeance, professeur, matiere, salle, dateSeance)

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
        all = []
        for i in cls.seances:
            if i["salle"] == idSalle:
                all.append(i["dateSeance"])
        if date in all:
            return False
        else:
            return True

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
