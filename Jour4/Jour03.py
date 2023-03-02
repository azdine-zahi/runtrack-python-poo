class Rectangle:

    def __init__(self, longueur, largeur):
        self.__longueur=longueur
        self.__largeur=largeur

    def perimetre(self):
        return 2*(self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur*self.__largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self,longueur):
        self.__longueur=longueur
    
    def get_largeur(self):
        return self.__largeur
    

    def set_largeur(self,largeur):
        self.__largeur=largeur

    

class Parallelepipede(Rectangle):

    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.__hauteur=hauteur

    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self,hauteur):
        self.__hauteur=hauteur

    def volume(self):
        return self.surface()*self.__hauteur
    


r = Rectangle(5, 10)
print(r.perimetre())  # Output : 30
print(r.surface())  # Output : 50

r.set_longueur(7)
print(r.get_longueur())  # Output : 7

r.set_largeur(12)
print(r.get_largeur())  # Output : 12


p = Parallelepipede(3, 4, 5)
print(p.volume())  # Output : 60

p.set_longueur(6)
print(p.get_longueur())  # Output : 6

p.set_largeur(8)
print(p.get_largeur())  # Output : 8

p.set_hauteur(10)
print(p.get_hauteur())  # Output : 10


    