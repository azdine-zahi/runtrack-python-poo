class Personnage:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def gauche(self):
        self.x -=1

    def droite(self):
        self.x +=1

    def haut(self):
        self.y +=1

    def bas(self):
        self.y -=1

    def position(self):
        # afficher la position sous forme de tuple  (x,y)
        return(self.x,self.y)

repérage = Personnage(1, 2)
print(repérage.position())
repérage.gauche()
print(repérage.position())
repérage.droite()
print(repérage.position())
repérage.haut()
print(repérage.position())
repérage.bas()
print(repérage.position())