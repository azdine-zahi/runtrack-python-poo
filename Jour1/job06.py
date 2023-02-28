class Animal: # Création de la classe Animal
    
    def __init__(self,age):
        self.age = 0
        
        print("l'age de l'animal est : ", self.age) # Affichage de l'age de l'animal

        
    def vieillir(self): # Création de la méthode viellir
        self.age += 1 # Incrémentation de l'age de l'animal
        print("L'âge de l'animal est maintenant de {} ans.".format(self.age))  # Affichage de l'age de l'animal
      
        
    def nommer(self, prenom): # Création de la méthode nommer
        self.prenom = prenom
        print("le nom de l'animal est: ", self.prenom)  # Affichage du prénom de l'animal
        
    


# Créer un objet Animal
mon_animal = Animal(0)

# Faire vieillir l'animal (affiche automatiquement le nouvel âge)
mon_animal.vieillir()  # Résultat : L'âge de l'animal est maintenant de 1 ans.

# Nommer l'animal
mon_animal.nommer("Noucheka")


