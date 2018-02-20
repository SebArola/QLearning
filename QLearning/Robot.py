from Labyrinthe import Labyrinthe
from Deplacement import Deplacement
from Type import Type
from Case import Case


class Robot:
    def __init__(self,labyrinthe, max_deplacement):
        self.lab = labyrinthe
        self.case = Case(Type.Entree, self.lab.depart[0], self.lab.depart[2])
        self.penalite = 0.99 #epsilon
        self.gamma = 0.95
        self.nb_deplacement_max = max_deplacement
        self.Q #Q(s,a)
        
    def exploration(self):
        self.lab.deplacement_possible(self.case)
        
    