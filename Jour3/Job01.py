class Ville:

    def __init__(self, nom, nbr_habitants):
        self.__nom = nom
        self.__nbr_habitants = nbr_habitants

    def get_nom(self):
        return self.__nom
    
    def get_nbr_habitants(self):
        return self.__nbr_habitants
    
    def set_nbr_habitants(self):
        self.__nbr_habitants += 1
    


class Personne:

    def __init__(self, nom, age, ville):
        self.__nom=nom
        self.__age=age
        self.__ville=ville

    def get_nom(self):
        return self.__nom
    
    def get_age(self):
        return self.__age
    
    def get_ville(self):
        return self.__ville
    
    def ajouterPopulation(self):
        self.__ville.set_nbr_habitants()

    

Paris = Ville("Paris", 1000000)
print(f"Population de la ville de {Paris.get_nom()}: {Paris.get_nbr_habitants()} habitans ")

Marseille= Ville("Marseille", 861635)
print(f"Population de la ville {Marseille.get_nom()}: {Marseille.get_nbr_habitants()} habitants")

John= Personne("John", 45, Paris)
Myrtille= Personne("Myrtille", 4, Paris)
Chloé= Personne("Chloé", 18, Marseille)

John.ajouterPopulation()
Myrtille.ajouterPopulation()
print(f"Mise à jour de la population de la ville de {Paris.get_nom()}: {Paris.get_nbr_habitants()} habitans ")

Chloé.ajouterPopulation()
print(f"Mise à jour de la population de la ville de {Marseille.get_nom()}: {Marseille.get_nbr_habitants()} habitants")
