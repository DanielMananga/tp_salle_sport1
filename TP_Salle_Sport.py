class Membres:
    def __init__(self,numero,nom,succursale,duree,prix,actif):
        self.__numero = numero
        self.__nom = nom
        self.__succursale = succursale
        self.__duree = duree
        self.__prix = prix
        self.__actif = actif
    def afficher(self):
        print(f"numéro : {self.__numero}")
        print(f"nom : {self.__nom}")
        print(f"succursale : {self.__succursale}")
        print(f"durée : {self.__duree}")
        print(f"prix : {self.__prix}")
        print(f"actif : {self.__actif}")
me=Membres(1,"Daniel","Toronto",3,500,"Oui")
me.afficher()