class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        self.__disponible = True

    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nombre_pages(self):
        return self.__nombre_pages

    def set_nombre_pages(self, nombre_pages):
        if int(nombre_pages) > 0:
            self.__nombre_pages = nombre_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    def verification(self):
        if self.__disponible:
            return True
        else:
            return False

    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible pour le moment.")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'a pas été emprunté.")

livre = Livre("python", "djamel", 300)

print(f"Disponibilité : {livre.verification()}")
livre.emprunter()
livre.emprunter()
print(f"Disponibilité : {livre.verification()}")
livre.rendre()
livre.rendre()
print(f"Disponibilité : {livre.verification()}")
