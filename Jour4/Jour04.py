class Forme:

    def __init__(self) -> None:
        pass

    def aire(self):
        return 0
    

class Rectangle(Forme):
    
    def __init__(self, largeur, hauteur):
        self.largeur=largeur
        self.hauteur=hauteur

    def aire(self):
        return self.largeur*self.hauteur
    

mon_rectangle = Rectangle(4, 5)
print(mon_rectangle.aire())  # imprime 20
