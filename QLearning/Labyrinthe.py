from Case import Case
from Type import Type

class Labyrinthe:
    def __init__(self):
        self.labyrinthe = []
        self.arrive = []
        self.depart = []
        
        self.chargerLabyrinthe()
        
    def chargerLabyrinthe(self):
        #Creation manuel du labyrinthe pour avancer rapidement
        for i in range(10):
            self.labyrinthe.append([])
            for j in range(10):
                self.labyrinthe[i].append(Case(Type.Libre, i,j))
                