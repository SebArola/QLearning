from Labyrinthe import Labyrinthe
from Deplacement import Deplacement
from Type import Type
from Case import Case
import random


class Robot:
    def __init__(self,labyrinthe, max_deplacement):
        self.lab = labyrinthe
        self.case = Case(Type.Entree, self.lab.depart[0], self.lab.depart[1])
        self.penalite = 0.99 #epsilon
        self.gamma = 0.95
        self.nb_deplacement_max = max_deplacement
        self.Q = {}#Q(s,a)
        
    def exploration(self):
        deplacement = self.lab.deplacement_possible(self.case)
        randi = random.randint(0, len(deplacement)-1)
        (renfort, case_arriver) = self.lab.se_deplacer(self.case, deplacement[randi])
        self.Q[(self.case, deplacement[randi])] = renfort + self.gamma * maxQ(case_arriver)
        self.case = case_arriver
    
    def maxQ(self,case):
        renfort = -10000
        for (c, d) in self.Q :
            if case.equal(c):
                if renfort < self.Q[(c,d)]:
                    renfort = self.Q[(c,d)]
        return renfort
    