from Case import Case
from Type import Type
from Deplacement import Deplacement

class Labyrinthe:
    def __init__(self):
        self.labyrinthe = []
        self.arrive
        self.depart
        
        self.chargerLabyrinthe()
        
    def chargerLabyrinthe(self):
        #Creation manuel du labyrinthe pour avancer rapidement
        for i in range(10):
            self.labyrinthe.append([])
            for j in range(10):
                self.labyrinthe[i].append(Case(Type.Libre, i,j))
        self.depart = (0,0)
        self.arrive = (9,9)
    
    def deplacement_possible(self, case):
        deplacement_possible = []
        for i in range(case.x-1 ,case.x+1 ):
            for j in range(case.y-1, case.y+1):
                if self.labyrinthe[i][j].type != Type.Mur :
                    if i-case.x==1 :
                        deplacement_possible.append(Deplacement.EST)
                    elif i-case.x == -1:
                        deplacement_possible.append(Deplacement.OUEST)
                    elif j-case.y == 1 :
                        deplacement_possible.append(Deplacement.SUD)
                    elif j-case.y == -1 :
                        deplacement_possible.append(Deplacement.NORD)
                    
        return deplacement_possible
    
    
    
    def se_deplacer(self, case, deplacement):
        renfort = 0
        if deplacement == Deplacement.NORD or deplacement == Deplacement.SUD:
            case_arriver = self.labyrinthe[case.x+deplacement.value][case.y]
        else:
            case_arriver = self.labyrinthe[case.x][case.y+deplacement.value]
        renfort = case_arriver.type.value        
        return (renfort, case_arriver)
    
    def getArrive(self):
        return self.arrive
    
    def getDepart(self):
        return self.depart
