class Plateau :

    def __init__(self):
        self.plateau=[0]*42
        self.tour = 0

    def jeu_possible(self):
        for i in range(35,42):
            if self.get_case(i) == 0 :
                return True
        return False

        
    def Victoire(self, x=int()):
        """Vérifie si victoire.
        A voir si ca marche
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
        return VictoiresPossibles


    def get_case(self,x):
       return self.plateau[x]

if __name__=="__main__":
    jeu = Plateau()
    jeu.plateau= [0, 0, 0,1 ,0 , 0, 1,
                  1, 1, 0, 0, 0, 1, 0, 
                  0, 0, 0, 0, 1, 0, 0, 
                  1, 0, 0, 0, 0, 0, 0, 
                  0, 0, 0, 0, 0, 0, 0, 
                  0, 0, 0, 0, 0, 0, 1]
    print(jeu.Victoire(6))
