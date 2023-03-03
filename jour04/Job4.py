class Forme:
    def __init__(self):
        pass

    def aire(self):
        self = 0
        return self
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        Forme.__init__(self)
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur
    
rectangle = Rectangle(6, 10)
print(rectangle.aire())