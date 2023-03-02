class Vehicule:

    def __init__(self, marque, annee, prix, modele):
        self.marque=marque
        self.annee=annee
        self.prix=prix
        self.modele=modele
    
    def informationsVehicule(self):
        print("Marque =",self.marque)
        print("Model =",self.modele)
        print("Année =",self.annee)
        print("Prix =",self.prix)
        
        

class Voiture(Vehicule):

    def __init__(self,marque, annee, prix, modele):
        self.porte=4
        super().__init__(marque, annee, prix, modele)


    def informationsVehicule(self):
        Vehicule.informationsVehicule(self)
        print("Nombre de porte =", self.porte)


voiture=Voiture("Mercedes", 2020, 18500, "Class A")
voiture.informationsVehicule()


class Moto(Vehicule):

    def __init__(self, marque, annee, prix, modele):
        self.roue=2
        super().__init__(marque, annee, prix, modele)

    def informationsVehicule(self):
        Vehicule.informationsVehicule(self)
        print ("Nombre de roue", self.roue)


moto=Moto("Yamaha", 1987, 4500, "1200 Vmax")
moto.informationsVehicule()