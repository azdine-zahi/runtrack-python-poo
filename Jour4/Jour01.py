class Personne:

    def __init__(self, age):
        self.age=int(age)

    def afficherAge(self):
        print ("j'ai",self.age, "ans")

    def bonjour(self):
        print("hello")

    def modifierAge(self,nouveau_age):
        self.age=nouveau_age




class Eleve(Personne):

    def allerEnCours(self):
        print("je vais en cours")

    def affichageAge(self):
        print("J'ai",self.age,"ans")



class Professeur(Personne):

    def __init__(self, matiereEnseignee, age=30):
        Personne.__init__(self,age)
        self.matiereEnseignee=matiereEnseignee
        print ("Je suis le prof de", self.matiereEnseignee, "et j'ai", self.age, "ans")

    def enseigner(self):
        print("Le cours va commencer")



# Instanciation d'une Personne et d'un Eleve
p1 = Personne()
e1 = Eleve()

# Affichage de l'âge par défaut de l'Eleve
e1.afficherAge()  # Output: J'ai 14 ans

# Instanciation d'un Eleve et d'un Professeur
e1 = Eleve()
p1 = Professeur("Mathématiques", age=45)