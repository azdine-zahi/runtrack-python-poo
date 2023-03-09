class Joeur:

    def __ini__(self, nom, numero, position, nbr_buts_marques, passes_decisives, catons_jaunes_recus, cartons_rouges_recus):
        self.nom=nom
        self.numero=numero
        self.position=position
        self.nbr_buts_marques=nbr_buts_marques
        self.passes_decisives=passes_decisives
        self.cartons_jaunes_recus=catons_jaunes_recus
        self.cartons_rouges_recus=cartons_rouges_recus

    def marquerUnBut(self):
        self.nbr_buts_marques +=1

    def effecuterUnePasseDecisive(self):
        self.passes_decisives +=1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes_recus +=1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges_recus +=1

    def afficherStatistiques(self):
        print("Le nom du joueur est:",self.nom)
        print("Le numéro de joueur est:",self.numero)
        print("La position du joueur est:", self.position)
        print("Le nombre de buts marqués est:", self.nbr_buts_marques)
        print("Le nombre de passes decisives effectuées est:",self.passes_decisives)
        print("Le nombre de cartons jaunes reçues est :",self.cartons_jaunes_recus)
        print("Le nombre de cartons rouges reçues est :", self.cartons_rouges_recus)


class Equipe:

    def __init__(self, nom_equipe, liste_joueurs):
        self.nom_equipe=nom_equipe
        self.liste_joueurs=liste_joueurs

    def ajouterUnJoueur(self):
        self.liste_joueurs +=1