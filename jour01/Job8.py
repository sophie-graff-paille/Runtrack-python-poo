from math import *

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, newrayon):
        self.rayon = newrayon

    def afficherInfos(self):
        print(self.rayon, self.circonférence(), self.diamètre(), self.aire())

    def circonférence(self):
        return 2 * pi * self.rayon
    
    def aire(self):
        return pi * (self.rayon ** 2)
    
    def diamètre(self):
        return 2 * self.rayon
    
rayon1 = 4
cercle = Cercle(4)
cercle1 = Cercle(rayon1)
cercle.afficherInfos()
print(cercle.circonférence())
print(cercle.diamètre())
print(cercle.aire())

rayon2 = 7
cercle = Cercle(7)
cercle2 = Cercle(rayon2)
cercle.afficherInfos()
print(cercle.circonférence())
print(cercle.diamètre())
print(cercle.aire())