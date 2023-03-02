class Forme:

    def __init__(self) -> None:
        pass

    def aire(self):
        return 0
    
class Cercle(Forme):

    def __init__(self, radius):
        self.radius=radius

    def aire (self):
        return 3.14*self.radius**2
    

mon_cercle=Cercle(7)
print(mon_cercle.aire())