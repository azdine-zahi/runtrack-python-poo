class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
        self.en_marche = False
        self.reservoir = 50

    def get_marque(self):
        return self.marque

    def set_marque(self, marque):
        self.marque = marque

    def get_modele(self):
        return self.modele

    def set_modele(self, modele):
        self.modele = modele

    def get_annee(self):
        return self.annee

    def set_annee(self, annee):
        self.annee = annee

    def get_kilometrage(self):
        return self.kilometrage

    def set_kilometrage(self, kilometrage):
        self.kilometrage = kilometrage

    def get_en_marche(self):
        return self.en_marche

    def set_en_marche(self, en_marche):
        self.en_marche = en_marche

    def demarrer(self):
        if self.verifier_plein() > 5:
            self.en_marche = True
            print("La voiture peut démarré")
        else:
            print("Le réservoir est trop vide pour démarrer la voiture")

    def arreter(self):
        self.en_marche = False
        print("La voiture a été arrêtée")

    def verifier_plein(self):
        return self.reservoir

    def set_verifier_plein(self, reservoir):
        self.reservoir = reservoir


voiture = Voiture("bmw", "m5", 2018, 100000)

print(f" marque:{voiture.get_marque()}, modele:{voiture.get_modele()}, anne:{voiture.get_annee()}, kilometrage:{voiture.get_kilometrage()}")
print(f"le reservoir contient {voiture.verifier_plein()} litre")
voiture.demarrer()

voiture.set_verifier_plein(4)
print(f"le reservoir contient {voiture.verifier_plein()} litre")
voiture.demarrer()
voiture.arreter()





