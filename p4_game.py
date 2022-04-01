class Plateau :

    def __init__(self):
        self.plateau=[0]*42
        self.tour = 0

    def jeu_possible(self):
        for i in range(35,42):
            if self.get_case(i) == 0 :
                return True
        return False

    def get_case(self, x):
       return self.plateau[x]

if __name__=="__main__":
    jeu = Plateau()
    print(jeu.tour)
    jeu.plateau= [1]*42
    print(jeu.jeu_possible())