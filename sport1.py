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