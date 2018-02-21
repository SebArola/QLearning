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
        
    def maxQ(self,case):
        renfort = -10000
        cMax = 0
        dMax = 0
        for (c, d) in self.Q :
            if case.equal(c):
                if renfort < self.Q[(c,d)]:
                    renfort = self.Q[(c,d)]
                    cMax = c
                    dMax = d
        return (renfort,cMax,dMax)
        
    def exploration(self):
        deplacement = self.lab.deplacement_possible(self.case)
        randi = random.randint(0, len(deplacement)-1)
        print(deplacement[randi])
        (renfort, case_arriver) = self.lab.se_deplacer(self.case, deplacement[randi])
        self.Q[(self.case, deplacement[randi])] = renfort + self.gamma * self.maxQ(case_arriver)[0]
        self.case = case_arriver
      
    def QLearning(self):
        i=0
        while(i<self.nb_deplacement_max):
            self.exploration()
            i+=1
        self.afficherQ()
    
    def afficherQ(self):
        for i in range(10):
            for j in range(10):
                (r,c,d) = self.maxQ(self.lab.labyrinthe[i][j])
                
                print(str((c,d)) + ' ', end='')
            print()
        
    
lab = Labyrinthe()
lab.afficherLab()
robot = Robot(lab,1000)
robot.QLearning()


    