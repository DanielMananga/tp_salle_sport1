class Membres:
    def __init__(self,numero,nom,succursale,duree,prix,actif):
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
    def numero(self,numero):
        self.__numero = numero

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,nom):
        self.__nom = nom

    @property
    def succursale(self):
        return self.__succursale
    @succursale.setter
    def succursale(self,succursale):
        self.__succursale = succursale

    @property
    def duree(self):
        return self.__duree
    @duree.setter
    def duree(self,duree):
        if duree > 0:
            self.__duree = duree
        else:
            print("Durée invalide.")

    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self,prix):
        if prix > 0:
            self.__prix = prix
        else:
            print("Prix invalide.")

    @property
    def actif(self):
        return self.__actif
    @actif.setter
    def actif(self,actif):
        if actif.lower() == "oui" or actif.lower() == "non":
            self.__actif = actif
        else:
            print("Valeur invalide pour actif.")

    def afficher(self):
        print(f"numéro : {self.__numero}")
        print(f"nom : {self.__nom}")
        print(f"succursale : {self.__succursale}")
        print(f"durée : {self.__duree}")
        print(f"prix : {self.__prix}")
        print(f"actif : {self.__actif}")


me=Membres(1,"Daniel","Toronto",-3,-500,"0")
me.afficher()

import time
import random

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


# ----- Partie 10 : Hachage -----

def hacher_membre(nom, succursale):
    return hash(nom + succursale)


def test_hachage_vs_boucle():
    noms = ["Daniel", "Barry", "Sow", "Kevin", "Julie", "Marc", "Sophie", "Karim", "Ali", "Nadia"]
    succursales = ["Centre-ville", "Est", "Ouest", "Nord", "Sud"]

    membres_generes = []
    for i in range(1000):
        nom = random.choice(noms) + str(i)
        succursale = random.choice(succursales)
        membres_generes.append((nom, succursale))

    # méthode par ensemble de hachage
    debut = time.time()
    vus_hash = set()
    doublons_hash = 0
    for nom, succursale in membres_generes:
        cle = hacher_membre(nom, succursale)
        if cle in vus_hash:
            doublons_hash += 1
        else:
            vus_hash.add(cle)
    fin = time.time()
    temps_hash = fin - debut

    # méthode par recherche linéaire
    debut = time.time()
    vus_liste = []
    doublons_liste = 0
    for nom, succursale in membres_generes:
        trouve = False
        for n, s in vus_liste:
            if n == nom and s == succursale:
                trouve = True
                break
        if trouve:
            doublons_liste += 1
        else:
            vus_liste.append((nom, succursale))
    fin = time.time()
    temps_liste = fin - debut

    print("\n===== Partie 10 : Hachage vs recherche linéaire =====")
    print("Temps avec ensemble de hachage :", temps_hash)
    print("Temps avec recherche linéaire :", temps_liste)


# ----- Partie 11 : Dictionnaires -----

def construire_index(membres):
    index_membres = {}
    for membre in membres:
        index_membres[membre.numero] = membre
    return index_membres


def rechercher_par_numero(index_membres, numero):
    if numero in index_membres:
        return index_membres[numero]
    else:
        return "Membre introuvable."


def rechercher_boucle(membres, numero):
    for membre in membres:
        if membre.numero == numero:
            return membre
    return "Membre introuvable."


def test_dictionnaire_vs_boucle():
    membres_test = []
    for i in range(10000):
        m = MembreStandard(i, "Nom" + str(i), "Succursale" + str(random.randint(1, 5)), 12, 50, "Oui", "Oui")
        membres_test.append(m)

    numero_cherche = 9999

    debut = time.time()
    rechercher_boucle(membres_test, numero_cherche)
    fin = time.time()
    temps_boucle = fin - debut

    index_membres = construire_index(membres_test)

    debut = time.time()
    rechercher_par_numero(index_membres, numero_cherche)
    fin = time.time()
    temps_dict = fin - debut

    print("\n===== Partie 11 : Dictionnaire vs recherche linéaire =====")
    print("Temps recherche par boucle :", temps_boucle)
    print("Temps recherche par dictionnaire :", temps_dict)
    print("Le dictionnaire est plus rapide car il accède directement à la valeur par sa clé, sans parcourir toute la liste.")


# ----- Programme principal -----

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

test_hachage_vs_boucle()
test_dictionnaire_vs_boucle()

prochain_numero = 5

while True:
    print("\n1. Ajouter un membre standard")
    print("2. Ajouter un membre premium")
    print("3. Afficher tous les membres")
    print("4. Afficher les membres actifs")
    print("5. Afficher les membres premium")
    print("6. Sauvegarder les membres")
    print("7. Charger les membres")
    print("8. Rechercher un membre par numéro")
    print("0. Quitter")
    choix = input("Choix : ")

    if choix == "1":
        nom = input("Nom : ")
        succursale = input("Succursale : ")
        duree = int(input("Durée : "))
        prix = float(input("Prix : "))
        actif = input("Actif (Oui/Non) : ")
        casier = input("Casier (Oui/Non) : ")
        membre = MembreStandard(prochain_numero, nom, succursale, duree, prix, actif, casier)
        membres.append(membre)
        prochain_numero += 1
        print("Membre ajouté.")

    elif choix == "2":
        nom = input("Nom : ")
        succursale = input("Succursale : ")
        duree = int(input("Durée : "))
        prix = float(input("Prix : "))
        actif = input("Actif (Oui/Non) : ")
        coach = input("Coach personnel (Oui/Non) : ")
        membre = MembrePremium(prochain_numero, nom, succursale, duree, prix, actif, coach)
        membres.append(membre)
        prochain_numero += 1
        print("Membre ajouté.")

    elif choix == "3":
        for membre in membres:
            membre.afficher()
            print()

    elif choix == "4":
        afficher_membres_actifs(membres)

    elif choix == "5":
        afficher_membres_premium(membres)

    elif choix == "6":
        sauvegarder_membres(membres)
        print("Membres sauvegardés.")

    elif choix == "7":
        membres = charger_membres()
        print("Membres chargés.")

    elif choix == "8":
        index_membres = construire_index(membres)
        numero = int(input("Numéro à chercher : "))
        resultat = rechercher_par_numero(index_membres, numero)
        if resultat == "Membre introuvable.":
            print(resultat)
        else:
            resultat.afficher()

    elif choix == "0":
        print("Au revoir.")
        break

    else:
        print("Choix invalide.")