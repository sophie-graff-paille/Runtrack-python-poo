liste_plats_commandés = [{"plat": "salade quinoa", "prixHT": 8, "statut": ""}, {"plat": "choucroute", "prixHT": 15, "statut": ""}, {"plat": "tiramisu", "prix": 8}]
liste_statut_commande = ["en cours", "terminée", "annulée"]

class Commande:
    def __init__(self, numéro_commande, liste_plats_commandés, statut_commande):
        self.__numéro_commande = numéro_commande
        self.__liste_plats_commandés = liste_plats_commandés
        self.__statut_commande = statut_commande

    def setnuméro_commande(self, numéro_commande):
        self.__numéro_commande = numéro_commande

    def getnuméro_commande(self):
        return self.__numéro_commande
    
    def setliste_plats_commandés(self, liste_plats_commandés):
        self.__liste_plats_commandés = liste_plats_commandés

    def getliste_plats_commandés(self):
        return self.__liste_plats_commandés
    
    def setstatut_commande(self, statut_commande):
        self.__statut_commande = statut_commande

    def getstatut_commande(self):
        return self.__statut_commande
    
    def add_plats(self, plat):
        self.__liste_plats_commandés.append(plat)

    def annuler_commande(self):
        self.__statut_commande = "annulée"

    def calculer_total_commande(self):
        total = 0
        for plat in self.__liste_plats_commandés:
            total += plat["prixHT"]
        return total
    
    def calculer_tva(self):
        tva = 0
        for plat in self.__liste_plats_commandés:
            tva += plat["prixHT"] * 0.2
        return tva
    
    def afficher_commande(self):
        print("Commande n°", self.__numéro_commande)
        print("Liste des plats commandés :")
        for plat in self.__liste_plats_commandés:
            print(plat["plat"], plat["prixHT"])
        print("Statut de la commande :", self.__statut_commande)
        print(f"Total de la commande HT : {self.calculer_total_commande()}€ TVA incluse : {self.calculer_tva()}€)")

commande1 = Commande(1, liste_plats_commandés[0], liste_statut_commande[0])
commande1.add_plats("choucroute")
commande1.afficher_commande()
   