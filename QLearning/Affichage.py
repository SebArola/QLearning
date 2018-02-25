#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 21:05:11 2018

@author: matahi
"""

# import Tkinter as tk
import tkinter as tk
from ChargerFichier import ChargerFichier 

class Affichage():
    
    def __init__(self, nb_case, fenetre):
       
        # taille d'une case
        self.size = 50
        # Nombre de case
        self.nb_case = nb_case;
        
         # Taille du labyrinthe
        self.can_width = self.size * self.nb_case;
        self.can_height = self.size * self.nb_case;
        
        self.can = tk.Canvas(fenetre, width=self.can_width, height=self.can_height)
        self.can.grid()
        
    def chargerCanevas(self, labyrinthe):
        for i in range(self.nb_case):
            for j in range(self.nb_case):
                     if(labyrinthe[i][j].type.name == 'Libre'):
                         self.can.create_rectangle(j * self.size, i * self.size, j * self.size + self.size, i * self.size + self.size, fill="white")
                     if(labyrinthe[i][j].type.name == 'Entree'):
                         self.can.create_rectangle(j * self.size, i * self.size, j * self.size + self.size, i * self.size + self.size, fill="green")
                     if(labyrinthe[i][j].type.name == 'Mur'):
                         self.can.create_rectangle(j * self.size, i * self.size, j * self.size + self.size, i * self.size + self.size, fill="grey")
                     if(labyrinthe[i][j].type.name == 'Sortie'):
                         self.can.create_rectangle(j * self.size, i * self.size, j * self.size + self.size, i * self.size + self.size, fill="red")
                     if(labyrinthe[i][j].type.name == 'Piege'):
                         self.can.create_rectangle(j * self.size, i * self.size, j * self.size + self.size, i * self.size + self.size, fill="orange")    
                     
        return self.can 
