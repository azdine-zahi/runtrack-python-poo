class Personne:

    def __init__(self, nom, prenom):
        self.nom=nom
        self.prenom=prenom

    def SePresenter(self):
        print("je suis " + self.nom + " " + self.prenom)

pre=Personne("John", "Doe")
pre.SePresenter() 
pres=Personne("Jean", "Dupon")
pres.SePresenter()