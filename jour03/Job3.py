class Tache:
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self, taches):
        self.taches = taches
        taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, tache):
        self.taches.remove(tache)

    def marquerCommeFinie(self, tache):
        tache.statut = "finie"

    def afficherListe(self):
        for tache in self.taches:
            print(tache.titre, tache.description, tache.statut)

    def filtrerListe(self, statut):
        for tache in self.taches:
            if tache.statut == statut:
                print(tache.titre, tache.description, tache.statut)

tache1 = Tache("Devoirs", "Faire les devoirs du jour", "Terminée")
tache2 = Tache("Méditation", "Evacuer les tensions", "A faire")
tache3 = Tache("Lire", "Finir le livre", "A faire")

listeDeTaches = ListeDeTaches([])
listeDeTaches.ajouterTache(tache1)
listeDeTaches.ajouterTache(tache2)
listeDeTaches.ajouterTache(tache3)
listeDeTaches.supprimerTache(tache1)
listeDeTaches.marquerCommeFinie(tache2)
listeDeTaches.afficherListe()
listeDeTaches.filtrerListe("A faire")
       