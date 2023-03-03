class Personne:
    def __init__(self):
        self.age = 14

    def afficherAge(self):
        print(self.age)
    
    def bonjour(self):
        print("Hello")

    def modifierAge(self, age):
        self.age = age

class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self)

    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai", self.age, "ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        Personne.__init__(self)
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

personne1 = Personne()
sophie = Eleve()
sophie.affichageAge()
professeur = Professeur("Géographie")
professeur.enseigner()
print (professeur.__matiereEnseignee)