class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prénom = prenom

    def SePresenter(self):
        return self.nom + self.prénom    

personne1 = Personne("GraffPaille", "Sophie")
print(personne1.SePresenter())

personne2 = Personne("Paille", "Pierre")
print(personne2.SePresenter())