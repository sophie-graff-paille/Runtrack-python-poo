class Voiture:
    def __init__(self, marque, modèle, année, kilométrage):
        self.__marque = marque
        self.__modèle = modèle
        self.__année = année
        self.__kilométrage = kilométrage
        self.__en_marche = False
        self.__réservoir = 50

    def setmarque(self, marque):
        self.__marque = marque
        return self.__marque
    
    def getmarque(self):
        return self.__marque
    
    def setmodèle(self, modèle):
        self.__modèle = modèle
        return self.__modèle
    
    def getmodèle(self):
        return self.__modèle
    
    def setannée(self, année):
        self.__année = année
        return self.__année
    
    def getannée(self):
        return self.__année
    
    def setkilométrage(self, kilométrage):
        self.__kilométrage = kilométrage
        return self.__kilométrage
    
    def getkilométrage(self):
        return self.__kilométrage
    
    def démarre(self):
        self.__en_marche = True
        return self.__en_marche
    
    def arrêter(self):
        self.__en_marche = False
        return self.__en_marche
    
    def vérifier_plein(self):
        if self.__réservoir == 0:
            return False
        else:
            return True
        
    def démarrer(self):
        if self.vérifier_plein() == True and self.__réservoir > 5:
            self.__en_marche = True
            print("La voiture peut démarrer")
        else:
            print("Il n'y a pas assez d'essence pour démarrer")

voiture = Voiture("Nissan", "Juke", 2015, 10000)
voiture.démarrer()