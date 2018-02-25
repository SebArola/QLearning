from Labyrinthe import Labyrinthe
from Robot import Robot
from Case import Case
from Affichage import Affichage
from Deplacement import Deplacement
from Type import Type
from ChargerFichier import ChargerFichier
import tkinter as tk
import time
nb_case = 6;
size = 50;
max_deplacement =1000;
temps_attente = 0.05;

lab_txt = ChargerFichier("labyrinthe.txt")
labyrinthe = Labyrinthe(nb_case)
labyrinthe.chargerLabyrinthe(lab_txt)

fenetre = tk.Tk()
fenetre.title('Projet Q-Learning Labyrinthe')

affichage = Affichage(nb_case,fenetre)
can = affichage.chargerCanevas(labyrinthe.labyrinthe)

robot = Robot(labyrinthe,max_deplacement)

i=labyrinthe.depart[0]
j=labyrinthe.depart[1]
rect_robot = can.create_rectangle(j*size, i*size, j*size+size, i*size+size, fill = "blue")

i=0
while(i<max_deplacement):
    prev_x = robot.case.x
    prev_y = robot.case.y
    fenetre.update_idletasks()
    fenetre.update()
    robot.QLearning()
    can.move(rect_robot,(robot.case.y- prev_y)*size, (robot.case.x-prev_x)*size)
    time.sleep(temps_attente)
    i+=1
