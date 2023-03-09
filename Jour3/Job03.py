class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde, decouvert=False):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
    
    def afficher(self):
        print("Compte bancaire n°", self.__numero)
        print("Nom du titulaire :", self.__nom)
        print("Prénom du titulaire :", self.__prenom)
        print("Solde :", self.__solde, "€")
        if self.__decouvert:
            print("Le compte est à découvert.")
    
    def afficherSolde(self):
        print("Le solde du compte est de", self.__solde, "€")
    
    def versement(self, montant):
        self.__solde += montant
        print("Versement de", montant, "€ effectué.")
    
    def retrait(self, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Erreur : solde insuffisant.")
        else:
            self.__solde -= montant
            print("Retrait de", montant, "€ effectué.")
            print("Nouveau solde :", self.__solde, "€")
    
    def agios(self, taux):
        if self.__solde < 0:
            self.__solde -= self.__solde * taux
            print("Application des agios.")
            print("Nouveau solde :", self.__solde, "€")
    
    def virement(self, compte, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Erreur : solde insuffisant.")
        else:
            self.__solde -= montant
            compte.versement(montant)
            print("Virement de", montant, "€ effectué.")
            print("Nouveau solde du compte émetteur :", self.__solde, "€")
            print("Nouveau solde du compte destinataire :", compte.__solde, "€")


# Création d'un compte avec un solde de 1000€
compte1 = CompteBancaire("12345", "Dupont", "Jean", 1000)

# Affichage des informations sur le compte
compte1.afficher()

# Affichage du solde du compte
compte1.afficherSolde()

# Versement de 500€ sur le compte
compte1.versement(500)

# Retrait de 200€ du compte
compte1.retrait(200)

# Ajout de 5% d'agios sur le compte (si solde négatif)
compte1.agios(0.05)

# Création d'un compte à découvert avec un solde de -500€
compte2 = CompteBancaire("67890", "Durand", "Sophie", -500, True)

# Affichage des informations sur le compte
compte2.afficher()

# Virement de 400€ du compte 1 vers le compte 2
compte1.virement(compte2, 400)
