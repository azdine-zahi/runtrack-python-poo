class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur


rectangle = Rectangle(10, 5)

print(f"Longueur : {rectangle.get_longueur()}")
print(f"Largeur : {rectangle.get_largeur()}")

rectangle.set_longueur(15)
rectangle.set_largeur(8)
print("\n")
print(f"Longueur : {rectangle.get_longueur()}")
print(f"Largeur : {rectangle.get_largeur()}")
