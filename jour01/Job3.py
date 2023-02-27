class Operation:
    def __init__(self):
        self.nombre1 = 12
        self.nombre2 = 3

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(resultat)

operation = Operation()
operation.addition()