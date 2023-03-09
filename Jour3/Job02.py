class CompteBancaire:

    def __init__(self, numero_de_compte, nom, prenom, solde, decouvert=False):
        self.__numero_de_compte=numero_de_compte
        self.__nom=nom
        self.__prenom=prenom
        self.__solde=solde
        self.__decouvert=decouvert


    def get_numero_de_compte(self):
        return self.__numero_de_compte
    
    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom
    
    def get_solde(self):
        return self.__solde
    
    def get_decouvert(self):
        return self.__solde
    
    def afficher(self):

        print (f"Le numéro de compte est:{self.__numero_de_compte}")
        print (f"Le nom du client est: {self.__nom}")
        print (f"Le prénom du client est :{self.__prenom}")
        print (f"Le solde du compte est: {self.__solde} €")
        if self.__decouvert:
            print("Le compte est à découvert")


    def afficherSolde(self):

        print (f"Le solde du compte est de:{self.__solde} €")

    def versement(self, montant_du_versment):
        self.__solde += montant_du_versment
        print(f"Le nouveau solde après versement est: {self.__solde}")

    def retrait(self, montant_a_retirer):
        if self.__solde-montant_a_retirer<0 and not self.__decouvert:
            print("Erreur: solde insuffisant")
        else:
            self.__solde-= montant_a_retirer
            print("retrait de", montant_a_retirer, "€ effectue.")
            print("Nouveau solde:", self.__solde, "€")
    
    def agios(self, taux):
        if self.__solde<0:
            self.__solde -= self.__solde*taux
            print("Applicationdes agios.")
            print("Nouveau solde", self.__solde, "€")

    def virement(self, numero_du_compte, montant_virement):
        if self.__solde-montant_virement<0 and not self.__decouvert:
            print("Erreur: solde insuffisant.")
        else:
            self.__solde-=montant_virement
            compte.versement(montant_virement)
            print("Virement de",montant_virement,"€ effectué.")
            print("Nouveau solde du compte émetteur:", self.__solde, "€")
            print("Nouveau solde du compte destinaire:", compte.__solde, "€")

        

# Création d'un compte avec un solde de 1000€
compte=CompteBancaire(1342876590, "ZAHI", "Azdine", 1000)

# Affichage des informations sur le compte
compte.afficher()

# Affichage du solde du compte
compte.afficherSolde()

# Versement de 500€ sur le compte
compte.versement(500)

# Retrait de 200€ du compte
compte.retrait(200)

# Ajout de 5% d'agios sur le compte (si solde négatif)
compte.agios(0.05)

# Création d'un compte à découvert avec un solde de -500€
compte2 = CompteBancaire(6789034598, "Durand", "Sophie", -500, True)

# Affichage des informations sur le compte
compte2.afficher()

# Virement de 400€ du compte 1 vers le compte 2
compte.virement(compte2, 400)