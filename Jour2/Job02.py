class Livre ():

    def __init__(self, titre, auteur, nombrePages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombrePages = nombrePages
    def get_titre(self):
        return self.__titre
    def get_auteur(self):
        return self.__auteur
    def get_nombrePages(self):
        return self.__nombrePages
    def set_titre(self, titre):
        self.__titre = titre
    def set_auteur(self, auteur):
        self.__auteur = auteur
    def set_nombrePages(self, nombrePages):
        if nombrePages > 0 and type(nombrePages) == int:
            self.__nombrePages = nombrePages
        else:
            print("[ ERREUR ] Le nombre de pages doit être un entier positif")

    def __str__(self):
        return "Titre: "+self.__titre+"    Auteur: "+self.__auteur+"    Nombre de pages: "+str(self.__nombrePages)

livre1 = Livre("kololo", "Gavi ", 58)
print(livre1)
livre1.set_nombrePages(200)
print(livre1)

livre1.set_nombrePages(-200)
print(livre1)


