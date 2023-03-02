class Student:
    def __init__(self, nom, prenom, numstudent):
        self.__nom = nom
        self.__prenom = prenom
        self.__numstudent = numstudent
        self.__nbcredit = 0
        self.__level = self.studentEval()

    def setnom(self, nom):
        self.__nom = nom
        return self.__nom

    def getnom(self):
        return self.__nom
    
    def setprenom(self, prenom):
        self.__prenom = prenom
        return self.__prenom
    
    def getprenom(self):
        return self.__prenom
    
    def setnumstudent(self, numstudent):
        self.__numstudent = numstudent
        return self.__numstudent
    
    def getnumstudent(self):
        return self.__numstudent

    def add_credit(self, nbcredit):
        if nbcredit > 0: 
            self.__nbcredit += nbcredit
            print(f"Le nombre de crédits de {self.__prenom} {self.__nom} est de {self.__nbcredit} points.")
            self.__level = self.studentEval()
        else:
            self.__nbcredit < 0
            print("Erreur : le nombre de crédits doit être un entier positif.")

    def studentEval(self):
        if self.__nbcredit >= 90:
            return "Excellent"
        elif self.__nbcredit >= 80:
            return "Très bien"
        elif self.__nbcredit >= 70:
            return "Bien"
        elif self.__nbcredit >= 60:
            return "Passable"
        else:
            return "Insuffisant"
        
    def studentInfo(self):
        print(f"Nom = {self.__nom}\nPrénom = {self.__prenom} \nid = {self.__numstudent} \nNiveau = {self.__level}")
     
student1 = Student("Doe", "John", 145)
student1.add_credit(10)
student1.add_credit(10)
student1.add_credit(100)
student1.studentEval()
student1.studentInfo()