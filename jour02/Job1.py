class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def setLongueur(self, longueur):
        self.__longueur = longueur
        return self.__longueur
    
    def getLongueur(self):
        return self.__longueur
    
    def setLargeur(self, largeur):
        self.__largeur = largeur
        return self.__largeur
    
    def getLargeur(self):
        return self.__largeur

rectangle1 = Rectangle(10, 5)
print(f"La longueur du rectangle est de {rectangle1.getLongueur()} et sa largeur de {rectangle1.getLargeur()}")
rectangle1.setLongueur(8)
rectangle1.setLargeur(3)
print(f"La nouvelle longueur du rectangle est de {rectangle1.getLongueur()} et sa nouvelle largeur de {rectangle1.getLargeur()}")

