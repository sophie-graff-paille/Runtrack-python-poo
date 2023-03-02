class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def getnom(self):
        return self.__nom
    
    def setnom(self, nom):
        self.__nom = nom
        return self.__nom
    
    def getnombre_habitants(self):
        return self.__nombre_habitants
    
    def setnombre_habitants(self, nombre_habitants):
        self.__nombre_habitants = nombre_habitants
        return self.__nombre_habitants

ville1 = Ville("Paris", 1000000)
ville2 = Ville("Marseille", 861635)
print(f"La population de la ville de Paris est de {ville1.getnombre_habitants()} d'habitants")
print(f"La population de la ville de Marseille est de {ville2.getnombre_habitants()} d'habitants")

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def getnom(self):
        return self.__nom
    
    def setnom(self, nom):
        self.__nom = nom
        return self.__nom
    
    def getage(self):
        return self.__age
    
    def setage(self, age):
        self.__age = age
        return self.__age
    
    def getville(self):
        return self.__ville
    
    def setville(self, ville):      
        self.__ville = ville
        return self.__ville
    
    def ajouterPopulation(self):
        self.__ville.setnombre_habitants(self.__ville.getnombre_habitants() + 1)
        print(f"Mise à jour de la population de la ville de {self.__ville.getnom()} qui passe à {self.__ville.getnombre_habitants()} habitants")

personne1 = Personne("John", 45, ville1)
personne2 = Personne("Myrtille", 4, ville1)
personne3 = Personne("Chloé", 18, ville2)

personne1.ajouterPopulation()
personne2.ajouterPopulation()
personne3.ajouterPopulation()
