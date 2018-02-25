#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 21:05:11 2018

@author: matahi
"""

#import Tkinter as tk
import tkinter as tk
from ChargerFichier import ChargerFichier 

class Affichage():
    fenetre = tk.Tk()
    fenetre.title('Projet Q-Learning Labyrinthe')
    labyrinthe = ChargerFichier("labyrinthe.txt")
   
 
    # taille d'une case
    size = 50
    #Nombre de case
    nb_case = 10;
    
     #Taille du labyrinthe
    can_width = size * nb_case;
    can_height = size * nb_case;
    
    can = tk.Canvas(fenetre, width=can_width, height=can_height)
    can.grid()
    for i in range(nb_case):
        for j in range(nb_case):
             if(labyrinthe[i][j] == 'v'):
                 can.create_rectangle(j*size, i*size, j*size+size, i*size+size, fill = "white")
             if(labyrinthe[i][j] == 'e'):
                 can.create_rectangle(j*size, i*size, j*size+size, i*size+size, fill = "green")
             if(labyrinthe[i][j] == 'm'):
                 can.create_rectangle(j*size, i*size, j*size+size, i*size+size, fill = "grey")
             if(labyrinthe[i][j] == 's'):
                 can.create_rectangle(j*size, i*size, j*size+size, i*size+size, fill = "red")
             if(labyrinthe[i][j] == 'p'):
                 can.create_rectangle(j*size, i*size, j*size+size, i*size+size, fill = "orange")    
             if(labyrinthe[i][j] == 'r'):
                 can.create_rectangle(j*size, i*size, j*size+size, i*size+size, fill = "blue")  
    fenetre.mainloop()