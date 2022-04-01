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
        on compte les cases de 1 à 42 et retourne la valeur correspondante
        '''
       return self.plateau[x]

    def Victoire(self, x=int()):
        """
        entrée : x=int() entre 0 et 42, correspond à la case ou l'on veut vérifier si elle permet une victoire
        sortie : Booléen, True = victoire.
        """
        avancement = [1,6,7,8]
        VictoiresPossibles = [0,0,0,0]
        Valeur = self.plateau[x]
        for z in range(4):
            val = x+avancement[z]
            while self.get_case(val) ==Valeur:
                if not (val<42 and (val%7>=x%7 or z==1 and val%7<=x) and val>0):
                    break
                val += avancement[z]
                VictoiresPossibles[z]+=1
            val = x-avancement[z]

            while self.get_case(val) ==Valeur:
                if not (val<42 and (val%7<= x%7 or z==3 and val%7<=x) and val>0):
                    break
                val -= avancement[z]
                if z%2 ==1:
                    VictoiresPossibles[z-2]+=1
                else :
                    VictoiresPossibles[z]+=1
        
        for x in VictoiresPossibles :
            if x>= 3:
                return True
        return False

if __name__=="__main__":
    jeu = Plateau()
    print(jeu.tour)
    jeu.plateau= [1]*42
    print(jeu.jeu_possible())

    jeu = Plateau()
    jeu.plateau= [0, 0, 0, 1 ,0 , 0, 1,
                  1, 1, 0, 0, 0, 1, 0, 
                  0, 0, 0, 0, 1, 0, 0, 
                  1, 0, 0, 0, 0, 0, 0, 
                  0, 0, 0, 0, 0, 0, 0, 
                  0, 0, 0, 0, 0, 0, 1]
    assert jeu.victoire(6)==False, "Erreur, victoire NE-SO True à la place de False"
    assert jeu.victoire(2)==False, "Erreur, victoire linéaire True à la place de False"
    assert jeu.victoire(21)==False, "Erreur, victoire horizontal True à la place de False"
    assert jeu.victoire(16)==False, "Erreur victoire NO-SE TRue à la place de False"
    assert jeu.tour ==0, "Erreur sur self.tour"
