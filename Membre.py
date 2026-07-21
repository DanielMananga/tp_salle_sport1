class Membres:
    def __init__(self, numero, nom, succursale, duree, prix, actif):
        self.__numero = numero
        self.__nom = nom
        self.__succursale = succursale
        self.__duree = None
        self.__prix = None
        self.__actif = None

        self.duree = duree
        self.prix = prix
        self.actif = actif

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def succursale(self):
        return self.__succursale

    @succursale.setter
    def succursale(self, succursale):
        self.__succursale = succursale

    @property
    def duree(self):
        return self.__duree

    @duree.setter
    def duree(self, duree):
        if duree > 0:
            self.__duree = duree
        else:
            print("Durée invalide.")

    @property
    def prix(self):
        return self.__prix

    @prix.setter
    def prix(self, prix):
        if prix > 0:
            self.__prix = prix
        else:
            print("Prix invalide.")

    @property
    def actif(self):
        return self.__actif

    @actif.setter
    def actif(self, actif):
        if actif.lower() == "oui" or actif.lower() == "non":
            self.__actif = actif.capitalize()
        else:
            print("Valeur invalide pour actif.")

    def afficher(self):
        print("Numéro :", self.numero)
        print("Nom :", self.nom)
        print("Succursale :", self.succursale)
        print("Durée :", self.duree)
        print("Prix :", self.prix)
        print("Actif :", self.actif)


class MembreStandard(Membres):
    def __init__(self, numero, nom, succursale, duree, prix, actif, casier):
        super().__init__(numero, nom, succursale, duree, prix, actif)
        self.casier = casier

    def afficher(self):
        super().afficher()
        print("Casier :", self.casier)


class MembrePremium(Membres):
    def __init__(self, numero, nom, succursale, duree, prix, actif, coach):
        super().__init__(numero, nom, succursale, duree, prix, actif)
        self.coach = coach

    def afficher(self):
        super().afficher()
        print("Coach personnel :", self.coach)


m1 = MembreStandard(1, "Julie Tremblay", "Centre-ville", 12, 45, "Oui", "Oui")
m2 = MembreStandard(2, "Marc Bouchard", "Est", 6, 40, "Non", "Non")
m3 = MembrePremium(3, "Sophie Nguyen", "Centre-ville", 12, 80, "Oui", "Oui")
m4 = MembrePremium(4, "Karim Haddad", "Ouest", 24, 75, "Oui", "Non")

membres = [m1, m2, m3, m4]

for membre in membres:
    membre.afficher()
    print("")