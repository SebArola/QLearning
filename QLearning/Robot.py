from Labyrinthe import Labyrinthe
from Deplacement import Deplacement
from Type import Type
from Case import Case
from tkinter import *
import random


class Robot:
    def __init__(self,labyrinthe, max_deplacement):
        self.lab = labyrinthe
        self.case = self.lab.labyrinthe[self.lab.depart[0]][self.lab.depart[1]]
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
        if(len(deplacement)>0):
            randi = random.randint(0, len(deplacement)-1)
            (renfort, case_arriver) = self.lab.se_deplacer(self.case, deplacement[randi])
            self.Q[(self.case, deplacement[randi])] = renfort + self.gamma * self.maxQ(case_arriver)[0]
            self.case = case_arriver
        else :
            print("Dead end")
    def exploitation(self):
        (renfort, cMax, dMax) =  self.maxQ(self.case)
        if (type(dMax) is not int):
            (renfort, case_arriver) = self.lab.se_deplacer(self.case,dMax)
            self.case = case_arriver
      
    def QLearning(self):
        randi = random.random()
        if(randi >self.penalite):
            self.exploitation()
            print('Exploitation')
        else :
            self.exploration()
        if self.case.x == self.lab.arrive[0] and self.case.y == self.lab.arrive[1]:
            self.case.x = self.lab.depart[0] 
            self.case.y = self.lab.depart[1]
        self.penalite = self.penalite - 0.001
    
    def afficherQ(self):
        for i in range(6):
            for j in range(6):
                (r,c,d) = self.maxQ(self.lab.labyrinthe[i][j])
                
                print(str((c,d)) + ' ', end='')
            print()
        
# taille = 10
# taille_img = 64
# lab = Labyrinthe(taille)
# lab.afficherLab()
# robot = Robot(lab,1000)
# robot.QLearning()
# 
# root = Tk()
# root.title('QLearning')
# can = Canvas(root, width=taille_img*(taille), height=taille_img*(taille), bg="black")
# #...
# img = [[]]
# for i in range(taille):
#     img.append([])
#     for j in range(taille):
#         img[i].append(PhotoImage(file='image/'+str(lab.labyrinthe[i][j].type.name)+'.png'))
#         print(img[i][j])
#         can.create_image((i*taille_img)+(taille_img/2)+1,(j*taille_img)+(taille_img/2)+1,image = img[i][j])
#         can.pack()
#         
# can.pack()
#     
# root.mainloop()
