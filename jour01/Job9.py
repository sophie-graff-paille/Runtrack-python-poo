class Produit:
    def __init__(self, nom, prixHT):
        self.nom = nom
        self.prix = prixHT
        self.TVA = 0.2

    def CalculerPrixTTC(self):
        return self.prix * (1 + self.TVA)
    
    def afficher(self):
        return f"Nom : {self.nom} \nPrix HT : {self.prix} \nTVA : {self.TVA} \nPrix TTC : {self.CalculerPrixTTC()}"

    def changernomProduit(self):
        self.nom = input("Entrez le nouveau nom du produit: ")
        return f"Le nouveau nom du produit est {self.nom}"

    def changerPrixHT(self):
        self.prix = input("Entrez le nouveau prix HT du produit: ")
        return f"Le nouveau prix HT du produit est {self.prix}"

    def afficherinfoProduit(self):
        return f"Nom : {self.nom} \nPrix HT : {self.prix} \nTVA : {self.TVA} \nPrix TTC : {self.CalculerPrixTTC()}"


Produit1 = Produit("Cahier", 10)
print(Produit1.afficher())
print(Produit1.afficherinfoProduit())
print(Produit1.changernomProduit())
print(Produit1.changerPrixHT())

Produit2 = Produit("Stylo", 3)
print(Produit2.afficher())
print(Produit2.afficherinfoProduit())
print(Produit2.changernomProduit())
print(Produit2.changerPrixHT())