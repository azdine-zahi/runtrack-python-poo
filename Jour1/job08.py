class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    
    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon
    
    def afficherInfos(self):
        print("Cercle de rayon", self.rayon)
    
    def circonference(self):
        return 2 * 3.14 * self.rayon
    
    def aire(self):
        return 3.14 * self.rayon ** 2
    
    def diametre(self):
        return 2 * self.rayon

cercle1 = Cercle(4)
cercle1.afficherInfos() # Affiche "Cercle de rayon 4"
print("Circonférence :", cercle1.circonference()) # Affiche "Circonférence : 25.12"
print("Diamètre :", cercle1.diametre()) # Affiche "Diamètre : 8"
print("Aire :", cercle1.aire()) # Affiche "Aire : 50.24"
cercle1.changerRayon(6)
cercle1.afficherInfos() # Affiche "Cercle de rayon 6"

cercle2 = Cercle(7)
cercle2.afficherInfos() # Affiche "Cercle de rayon 7"
print("Circonférence :", cercle2.circonference()) # Affiche "Circonférence : 43.96"
print("Diamètre :", cercle2.diametre()) # Affiche "Diamètre : 14"
print("Aire :", cercle2.aire()) # Affiche "Aire : 153.86"
