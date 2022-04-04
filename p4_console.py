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
            val = x
            while (val<42 and (val%7>=x%7 or z==1 and val%7<=x%7) and val>=0):
                if not self.get_case(val) ==Valeur:
                    break
                val += avancement[z]
                VictoiresPossibles[z]+=1

            val = x
            while (val<42 and (val%7<= x%7 or z==3 and val%7<=x%7) and val>=0):
                if not self.get_case(val) ==Valeur:
                    break
                val -= avancement[z]
                if z%2 ==1:
                    VictoiresPossibles[z-2]+=1
                else :
                    VictoiresPossibles[z]+=1
        
        for x in VictoiresPossibles :
            if x>= 5:
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

        
if __name__=="__main__":
    jeu = Plateau()
    jeu.plateau= [0, 0, 0,1 ,0 , 0, 1,
                  1, 1, 0, 0, 0, 1, 0, 
                  0, 0, 0, 0, 1, 0, 0, 
                  1, 0, 0, 0, 0, 0, 0, 
                  0, 0, 0, 0, 0, 0, 0, 
                  0, 0, 0, 0, 0, 0, 1]
    print(jeu.Victoire(6))




class Console:
    '''
    Régit les interactions entre la console et les joueurs
    Jeu : Puissance 4
    '''

    def __init__(self):
        self.lejeu = Plateau()

    def jouer(self,colonne):
        '''
        Permets de modifier dans le puissance 4 les valeurs du tableau
        '''
        ligne = self.lejeu.jeu(colonne)
        if ligne ==-1:
            return -1
        self.lejeu.plateau[ligne*7 + colonne] = self.lejeu.tour%2 +1
        self.lejeu.tour +=1
        return ligne

    def qui_joue(self):
        '''
        Renvoie le numéro du joueur qui doit jouer : 1 ou 2
        '''
        return self.lejeu.tour%2 +1
        

    def afficher(self):
        '''
        Affiche dans la console le jeu Puissance 4
        '''
        for x in range(6):
            for y in range(7):
                Jeton = " "
                if self.lejeu.get_case(x*7 +y)==1:
                    Jeton = "X"
                elif self.lejeu.get_case(x*7 +y)==2:
                    Jeton = "O"
                print("|"+Jeton, end= '')
            print("")

        
        
        
Onjoue = Console()
Onjoue.afficher()
