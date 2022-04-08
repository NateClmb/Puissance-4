class Plateau :
    '''
    Cette classe est composée de 3 méthodes (__init__, jeu_possible, et get_case) 
    Permet de faire exister un jeu de Puissance 4 fonctionnel
    '''


    def __init__(self):
        '''
        Créer le plateau de 42 case 'vide' (égale à 0) et initialise le jeu en mettant un compteur tour à 0
        Pour ajouter des pions il faudra modifier la case (1 pour rouge, 2 pour jaune)
        '''
        self.plateau=[0]*42
        self.tour = 0

    def jeu_possible(self):
        '''
        Scanne le plateau, renvoie True si il y a au moins 1 case 'vide' (égale à 0), 
        renvoie False si toutes les cases sont pleines
        '''
        for i in range(35,42):
            if self.get_case(i) == 0 :
                return True
        return False

    def get_case(self, x):
        '''
        Renvoie la valeur x de la case. On ne prend pas en compte les lignes et les colonnes,
        on compte les cases de 0 à 41 et retourne la valeur correspondante
        '''
        return self.plateau[x]


    def victoire(self, x=int()):
        """
        entrée : x=int() entre 0 et 41, correspond à la case ou l'on veut vérifier si elle permet une victoire
        sortie : Booléen, True = victoire.
        """
        avancement = [1,6,7,8]
        VictoiresPossibles = [0,0,0,0]
        Valeur = self.plateau[x]
        for z in range(4):
            val = x+avancement[z]
            while val<42 and (val%7>=x%7 or z==1 and val%7<=x%7) and val>-1 and (val//7>x//7 or z==0):
                if not self.get_case(val) ==Valeur:
                    break
                val += avancement[z]
                VictoiresPossibles[z]+=1

            val = x-avancement[z]
            while val<42 and (val%7<= x%7 or z==1 and val%7>x%7) and val>=0 and (val//7<x//7 or z==0):
                if not self.get_case(val) ==Valeur:
                    break
                val -= avancement[z]
                VictoiresPossibles[z]+=1
        
        for x in VictoiresPossibles :
            if x>= 3:
                return True
        return False
    def jeu(self,colonne):
        case = colonne
        ligne = 0
        if self.plateau[colonne+5*7]==0:
            while self.get_case(case)!=0:
                case +=7
                ligne +=1

            return ligne
        else : 
            return -1
            
    def jouer(self,colonne):
        ligne = self.jeu(colonne)
        if ligne ==-1:
            return -1
        else :
            case = ligne*7+colonne
            self.plateau[case]= self.tour%2 +1
            self.tour+=1
            return ligne
            
    def qui_joue(self):
        return self.tour%2 +1

    def reset(self):
        '''
        Methode dangereuse : reset tout le plateau
        '''
        self.plateau=[0]*42
        self.tour = 0
        
if __name__=="__main__":
    jeu = Plateau()
    jeu.plateau= [1, 0, 0,1 ,0 , 1, 1,
                  0, 0, 0, 0, 0, 1, 1, 
                  0, 0, 2, 2, 1, 1, 0, 
                  1, 0, 2, 2, 1, 0, 0, 
                  0, 2, 0, 0, 0, 1, 1, 
                  2, 0, 0, 0, 0, 1, 1]
    print(jeu.victoire(35))


"""
[1,6,7,8]
 0, 0, 0, 0, 0, 0, 0]
 0, 0, 0, 0, 0, 0, 0, 
 1, 0, 0, 2, 1, 0, 0,
 0, 0, 2, 0, 1, 1, 0, 
 0, 0, 0, 0, 0, 1, 1,
 [1, 0, 0,1 ,0 , 0, 1,
"""
    



