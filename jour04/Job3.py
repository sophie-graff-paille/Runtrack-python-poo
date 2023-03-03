class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur
    
    def getlongueur(self):
        return self.__longueur
    
    def setlongueur(self, longueur):
        self.__longueur = longueur
        return self.__longueur

    def getlargeur(self):
        return self.__largeur
    
    def setlargeur(self, largeur):
        self.__largeur = largeur
        return self.__largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.__hauteur = hauteur

    def gethauteur(self):
        return self.__hauteur
    
    def sethauteur(self, hauteur):
        self.__hauteur = hauteur
        return self.__hauteur

    def volume(self):
        return self.surface() * self.__hauteur
    
rectangle = Rectangle(10, 5)
rectangle.perimetre()
rectangle.surface()
print(rectangle.perimetre(), rectangle.surface())
print(rectangle.getlongueur(), rectangle.getlargeur())
parallelepipede = Parallelepipede(10, 5, 6)
parallelepipede.volume()
print(parallelepipede.volume())
print(parallelepipede.getlongueur(), parallelepipede.getlargeur(), parallelepipede.gethauteur())
rectangle.setlongueur(20)
rectangle.setlargeur(10)
rectangle.perimetre()
rectangle.surface()
print(rectangle.perimetre(), rectangle.surface())