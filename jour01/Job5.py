class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(self.x, self.y)    

    def afficherX(self):
        print(self.x)

    def afficherY(self):
        print(self.y)
    
    def changerX(self, newx):
        self.x = newx
        
    def changerY(self, newy):
        self.y = newy

p = Point(100, 200)
p.afficherLesPoints()
p.afficherX()
p.afficherY()
newx = p.changerX(300)
newy = p.changerY(400)