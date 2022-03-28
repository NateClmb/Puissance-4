class Plateau :

    def __init__(self):
        self.plateau=[0]*42
        self.tour = 0

    def jeu_possible(self):
        for i in range(35,42):
            if get_case(i) == 0 :
                return True
        return False

        
     def Victoire(x=int()):
        """Vérifie si victoire.
        A voir si ca marche
        """
        avancement = [1,5,6,7]
        VictoiresPossibles = [0,0,0,0]
        for z in range(4):
            val = x+avancement[z]
            while get_case(val) ==Valeur:
                if not (val<42 and val%7>x%7):
                    break
                val += avancement[z]
                VictoiresPossibles[z]+=1
            val = x-avancement[z]
            while get_case(val) ==Valeur:
                if not (val<42 and val%7> x%7):
                    break
                val -= avancement[z]
                VictoiresPossibles[z]+=1
        
        for x in VictoiresPossibles :
            if x>= 3:
                return True
        return False


    def get_case(x):
       return self.plateau[x]

if __name__=="__main__":
    jeu = Plateau()
    print(jeu.tour)
    jeu.plateau= [1]*42
    print(jeu.jeu_possible())
