class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
        print("L'âge de l'animal", self.age, "ans")

    def vieillir(self):
        self.age += 1

    def nommer(self, prenom):
        self.prenom = prenom

animal = Animal()
animal.vieillir()
prenom = input("Entrez le prénom de l'animal: ")
animal.nommer(prenom)
print("L'âge de l'animal", animal.age, "ans")
print("L'animal se nomme", animal.prenom)