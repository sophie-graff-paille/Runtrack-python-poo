class Livre:
    def __init__(self, titre, auteur, nbPages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbPages = nbPages
        self.__disponible = True

    def getTitre(self):
        return self.__titre
    
    def setTitre(self, titre):
        self.__titre = titre
        return self.__titre
    
    def getAuteur(self):
        return self.__auteur
    
    def setAuteur(self, auteur):
        self.__auteur = auteur
        return self.__auteur
    
    def getNbPages(self):
        return self.__nbPages
    
    def setNbPages(self, nbPages):
        self.__nbPages = nbPages

    def changeNbPages(self, nbPages):
        self.__nbPages = nbPages
        if self.__nbPages > 0:
            print(f"Erratum : Le nombre réel de pages du livre est de {livre1.getNbPages()}.")
        else:
            self.__nbPages < 0
            print("Erreur : le nombre de pages ne peut être négatif.")

    def verification(self):
        if self.__disponible == True:
            return True
        else:
            return False

    def emprunter(self):
        if self.verification() == True:
            self.__disponible == False
            print("Le livre", self.__titre, "a été emprunté.")
        else:
            print("Le livre", self.__titre, "est disponible.")
    
    def rendre(self):
        if self.verification() == True:
            self.__disponible == False
            print("Le livre", self.__titre, "a été rendu.")
        else:
            print("Le livre", self.__titre, "est disponible.")

livre1 = Livre("Métaphysique des tubes", "Amelie Nothomb", 200)
print(f"Le livre {livre1.getTitre()} de {livre1.getAuteur()} contient {livre1.getNbPages()} pages.")
livre1.changeNbPages(-20)
livre1 = Livre("Métaphysique des tubes", "Amelie Nothomb", 200)
print("La disponibilité du livre =", livre1.verification())
livre1.emprunter()
livre1.rendre()