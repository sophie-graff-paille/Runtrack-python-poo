class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, ref):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__ref = ref
        self.__découvert = True

    def getnumero_compte(self):
        return self.__numero_compte
    
    def setnumero_compte(self, numero_compte):
        self.__numero_compte = numero_compte
        return self.__numero_compte
    
    def getnom(self):
        return self.__nom
    
    def setnom(self, nom):  
        self.__nom = nom
        return self.__nom
    
    def getprenom(self):
        return self.__prenom
    
    def setprenom(self, prenom):
        self.__prenom = prenom
        return self.__prenom
    
    def getsolde(self):
        return self.__solde
    
    def setsolde(self, solde):
        self.__solde = solde
        return self.__solde
    
    def getdécouvert(self):
        return self.__découvert
    
    def setdécouvert(self, découvert):
        self.__découvert = découvert
        return self.__découvert

    def afficher(self):
        print("Numéro de compte :", self.__numero_compte)
        print("Nom :", self.__nom)
        print("Prénom :", self.__prenom)
        print("Solde :", self.__solde)
        print("Référence :", self.__ref)

    def afficherSolde(self):
        print("Le solde du compte est de ", self.__solde)

    def versement(self, montant):
        self.__solde += montant

    def retrait(self, montant):
        self.__découvert = True
        self.__solde -= montant
        if self.__solde < 0:
            print("Solde insuffisant ! Découvert autorisé. Votre nouveau solde est de", self.__solde, "€")

    def agios(self):
        if self.__solde < -1000:
            self.__solde -= 20
            print("Votre solde est négatif. Agios appliqués. Votre nouveau solde est de", self.__solde, "€")

    def virement(self, montant, destinataire):
        self.__solde -= montant
        destinataire.__solde += montant
        print("Le virement de", montant, "€ du compteBancaire1 a bien été effectué. Votre nouveau solde est de", destinataire.__solde, "€")

compteBancaire1 = CompteBancaire(38, "GraffPaille", "Sophie", 8000, 2)
compteBancaire2 = CompteBancaire(39, "Paille", "Pierre", -1250, 1)
compteBancaire1.afficher()
compteBancaire1.versement(1500)
compteBancaire1.afficherSolde()
compteBancaire1.retrait(5500)
compteBancaire1.afficherSolde()
compteBancaire2.agios()
compteBancaire1.virement(1270, compteBancaire2)
compteBancaire1.afficherSolde()