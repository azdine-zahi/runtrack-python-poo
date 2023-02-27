class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA)
    
    def afficher(self):
        print("Nom :", self.nom)
        print("Prix HT :", self.prixHT)
        print("TVA :", self.TVA)
        print("Prix TTC :", self.CalculerPrixTTC())
    
    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom
    
    def modifierPrix(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT
    
    def obtenirNom(self):
        return self.nom
    
    def obtenirPrixHT(self):
        return self.prixHT
    
    def obtenirTVA(self):
        return self.TVA



produit1 = Produit("Pomme", 1.5, 0.2)
produit1.afficher() # Affiche les informations du produit

produit2 = Produit("Banane", 2.0, 0.1)
produit2.afficher() # Affiche les informations du produit

produit1.modifierNom("Poire")
produit1.modifierPrix(2.0)

print("Nouveau prix HT de", produit1.obtenirNom(), ":", produit1.obtenirPrixHT())
