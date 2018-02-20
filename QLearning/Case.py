from Type import Type
class Case:  
    def __init__(self, type, posX, posY):
       self.type = type
       self.x = posX
       self.y = posY
    
    def equal(self, case):
        return self.x == case.x and self.y == case.y 