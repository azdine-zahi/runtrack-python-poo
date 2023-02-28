
class Point():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print("Les coordonnées du point sont : ({}, {})".format(self.x, self.y))
    def afficherX(self):
        print("La coordonnée x du point est : {}".format(self.x))
    def afficherY(self):
        print("La coordonnée y du point est : {}".format(self.y))
    def changerX(self, x):
        self.x = x
    def changerY(self, y):
        self.y = y

# Créer un objet Point avec les coordonnées (3, 7)
coordonnée = Point(3, 7)

# Afficher les coordonnées du point
coordonnée.afficherLesPoints() # Résultat : Les coordonnées du point sont : (3, 7)

# Afficher la coordonnée x du point
coordonnée.afficherX() # Résultat : La coordonnée x du point est : 3

# Afficher la coordonnée y du point
coordonnée.afficherY()  # Résultat : La coordonnée y du point est : 7

# Changer la coordonnée x du point à 5
coordonnée.changerX(5)

# Changer la coordonnée y du point à 8
coordonnée.changerY(8)

# Afficher les nouvelles coordonnées du point
coordonnée.afficherLesPoints() # Résultat : Les coordonnées du point sont : (5, 8)
