class student:
    def __init__(self, nom, prenom,numero_etduiant,credit=False):
       self.__nom = nom
       self.__prenom = prenom
       self.numero_etduiant = numero_etduiant
       self.__credit = credit
       self.__level = self.__studentEval()


    def add_credits(self, credit):
        self.__credit += credit
        self.__level = self.__studentEval()


    def get_credit(self):
        return self.__credit

    def get_level(self):
        return self.__level
    def set_credit(self, credit):
        self.__credit = credit
        self.__level = self.__studentEval()
    def set_level(self, level):
        self.__level = level
        self.__studentEval()

    def __str__(self):
        return "Nom: "+self.__nom+"    Age: "+str(self.__prenom)+"    id : "+str(self.numero_etduiant)+"    Nombre de crédits: "+str(self.__credit)


    def __studentEval(self):
        if self.__credit >= 90:
            return "Excellent"
        elif self.__credit >= 80:
            return "Très bien"
        elif self.__credit >= 70:
            return "Bien"
        elif self.__credit >= 60:
            return "passable"
        else:
            return "Insuffisant"


    def studentInfo(self):
        print(self)
        print("Niveau: "+self.__level)

student1 = student("Kololo", "Gavi", 53749)
student1.add_credits(10)
student1.studentInfo()

student2 = student("John", "Doe", 145)
student2.add_credits(100)
student2.studentInfo()

