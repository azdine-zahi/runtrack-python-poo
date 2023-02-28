from dataclasses import dataclass

@dataclass
class commande():
    __num_commande: int
    __liste_plats_commandes: dict
    __statut_commande: str

    def ajouter_plat(self, plat, prix):
        self.__liste_plats_commandes[plat] = prix

    def annuler_commande(self):
        self.__statut_commande = "annulée"

    def calculer_total(self):
        total = 0
        for plat, prix in self.__liste_plats_commandes.items():
            total += prix
        return total

    def afficher_commande(self):
        print(f"Commande numéro {self.__num_commande} :")
        for plat, prix in self.__liste_plats_commandes.items():
            print(f"{plat} : {prix}€")
        print(f"Total : {self.calculer_total()}€")

    def calculer_tva(self):
        return self.calculer_total() * 0.2

    def __str__(self):
        return f"Commande numéro {self.__num_commande} : {self.__liste_plats_commandes} {self.__statut_commande}"


commande1 = commande(1, {"Pizza": 10, "Coca": 20}, "en cours")
print(commande1)
commande1.ajouter_plat("Pourboir", 5)
print(commande1)
commande1.afficher_commande()
print(commande1.calculer_tva())
