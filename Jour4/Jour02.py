class Personne:

    def __init__(self, age=14):
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
        

    def enseigner(self):
        print("Le cours va commencer")



# Instanciation d'une Personne et d'un Eleve
p1 = Personne()
e1 = Eleve()



e1.bonjour()
e1.allerEnCours()
e1.modifierAge(15)
e1.affichageAge()

p1 = Professeur("Mathématiques", age=45)
p1.bonjour()
p1.enseigner()