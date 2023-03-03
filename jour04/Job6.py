class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque = " + self.marque)
        print("Modele = " + self.modele)
        print("Annee = " + str(self.annee))
        print("Prix = " + str(self.prix))

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
        self.nbPortes = 4

    def informationsVehicule(self):
        print("Marque = " + self.marque)
        print("Modele = " + self.modele)
        print("Annee = " + str(self.annee))
        print("Prix = " + str(self.prix))
        print("Nombre de portes = " + str(self.nbPortes))

    def demarrer(self):
        print("La Mercedes démarre")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.roue = 2

    def informationsVehicule(self):
        print("Marque = " + self.marque)
        print("Modele = " + self.modele)
        print("Annee = " + str(self.annee))
        print("Prix = " + str(self.prix))
        print("Nombre de roues = " + str(self.roue))

    def demarrer(self):
        print("La Yamaha a démarré aussi !")

voiture = Voiture("Mercedes", "Class A", 2020, 18500)
voiture.informationsVehicule()
moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)
moto.informationsVehicule()
Vehicule.demarrer(voiture)
voiture.demarrer()
Vehicule.demarrer(moto)
moto.demarrer()