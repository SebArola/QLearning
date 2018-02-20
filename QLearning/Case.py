from Type import Type
class Case:  
    def __init__(self, type, posX, posY):
       self.type = type
       self.x = posX
       self.y = posY
    
    def __repr__(self):
        return '('+str(self.x)+','+str(self.y)+')'
    def equal(self, case):
        return self.x == case.x and self.y == case.y 