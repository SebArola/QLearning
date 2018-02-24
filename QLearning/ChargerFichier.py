#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 17:31:51 2018

@author: matahi
"""
import sys
def ChargerFichier(filename):
    try:
        fichier = open(filename).readlines()
    except:
        print >> sys.stderr, "pb / file", filename
        fichier.close()
            
    return fichier

#test = ChargerFichier("labyrinthe.txt")
#print(test)