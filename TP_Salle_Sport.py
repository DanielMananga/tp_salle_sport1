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


def sauvegarder_membres(membres):
    fichier = open("membres.txt", "w")

    for membre in membres:
        if isinstance(membre, MembreStandard):
            ligne = f"STANDARD;{membre.numero};{membre.nom};{membre.succursale};{membre.duree};{membre.prix};{membre.actif};{membre.casier}\n"
        elif isinstance(membre, MembrePremium):
            ligne = f"PREMIUM;{membre.numero};{membre.nom};{membre.succursale};{membre.duree};{membre.prix};{membre.actif};{membre.coach}\n"

        fichier.write(ligne)

    fichier.close()


def charger_membres():
    membres = []

    fichier = open("membres.txt", "r")

    for ligne in fichier:
        infos = ligne.strip().split(";")

        type_membre = infos[0]
        numero = int(infos[1])
        nom = infos[2]
        succursale = infos[3]
        duree = int(infos[4])
        prix = float(infos[5])
        actif = infos[6]

        if type_membre == "STANDARD":
            casier = infos[7]
            membre = MembreStandard(numero, nom, succursale, duree, prix, actif, casier)
        elif type_membre == "PREMIUM":
            coach = infos[7]
            membre = MembrePremium(numero, nom, succursale, duree, prix, actif, coach)

        membres.append(membre)

    fichier.close()

    return membres



def afficher_membres_actifs(membres):
    print("\n===== Membres actifs =====")

    for membre in membres:
        if membre.actif == "Oui":
            membre.afficher()
            print()


def afficher_membres_premium(membres):
    print("\n===== Membres Premium =====")

    for membre in membres:
        if isinstance(membre, MembrePremium):
            membre.afficher()
            print()


m1 = MembreStandard(1, "Daniel Mananga", "Centre-ville", 12, 45, "Oui", "Oui")
m2 = MembreStandard(2, "Barry Amadou", "Est", 6, 40, "Non", "Non")
m3 = MembrePremium(3, "Sow Amadou", "Centre-ville", 12, 80, "Oui", "Oui")
m4 = MembrePremium(4, "Kevin Mayele", "Ouest", 24, 75, "Oui", "Non")

membres = [m1, m2, m3, m4]


print("===== Liste des membres =====\n")

for membre in membres:
    membre.afficher()
    print()


sauvegarder_membres(membres)

print("Les membres ont été sauvegardés dans membres.txt\n")


liste = charger_membres()

print("===== Membres chargés =====\n")

for membre in liste:
    membre.afficher()
    print()


afficher_membres_actifs(liste)

afficher_membres_premium(liste)