from Case import Case
from Type import Type
from Deplacement import Deplacement


class Labyrinthe:
    def __init__(self, taille):
        self.labyrinthe = []
        self.arrive = 0
        self.depart = 0
        self.taille = taille
        self.chargerLabyrinthe(taille)
        
    def chargerLabyrinthe(self,taille):
        #Creation manuel du labyrinthe pour avancer rapidement
        for i in range(taille):
            self.labyrinthe.append([])
            for j in range(taille):
                self.labyrinthe[i].append(Case(Type.Libre, i,j))
        self.depart = (0,0)
        self.arrive = (taille-1,taille-1)
        self.labyrinthe[0][0].type = Type.Entree
        self.labyrinthe[taille-1][taille-1].type = Type.Sortie
    
    def deplacement_possible(self, case):
        deplacement_possible = []
        for i in range(case.x-1 ,case.x+2 ):
            if i>=0 and i<self.taille :
                if self.labyrinthe[i][case.y].type != Type.Mur :
                    if i-case.x==1 :
                        deplacement_possible.append(Deplacement.SUD)
                    elif i-case.x == -1:
                        deplacement_possible.append(Deplacement.NORD)
        for j in range(case.y-1, case.y+2):
            if j>=0 and j<self.taille :
                if self.labyrinthe[case.x][j].type != Type.Mur :         
                    if j-case.y == 1 :
                        deplacement_possible.append(Deplacement.EST)
                    elif j-case.y == -1 :
                        deplacement_possible.append(Deplacement.OUEST)
        #print(deplacement_possible)          
        return deplacement_possible
     
    def se_deplacer(self, case, deplacement):
        renfort = 0
        if deplacement == Deplacement.NORD or deplacement == Deplacement.SUD:
            case_arriver = self.labyrinthe[int(case.x+deplacement.value/abs(deplacement.value))][case.y]
        else:
            case_arriver = self.labyrinthe[case.x][case.y+deplacement.value]
        renfort = case_arriver.type.value        
        return (renfort, case_arriver)
    
    def getArrive(self):
        return self.arrive
    
    def getDepart(self):
        return self.depart
    
    def afficherLab(self):
        for i in range(self.taille):
            for j in range(self.taille):
                print(str(self.labyrinthe[i][j].type.name) + ' ', end='')
            print()
