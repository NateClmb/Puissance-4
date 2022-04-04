class Console:

    def __init__(self):
        self.lejeu = Plateau()

    def jeu(self,colonne): 
        case = colonne
        self.lejeu.get_case(case)
        while self.lejeu.get_case(case) > 0:
            case += 7
        self.lejeu.plateau[case]=(self.lejeu.tour % 2) +1
        return case
    
    def afficher(self):
        for x in range(6):
            for y in range(7):
                Jeton = "  "
                if self.lejeu.get_case(x*7 +y)==1:
                    Jeton = "X"
                elif self.lejeu.get_case(x*7 +y)==2:
                    Jeton = "O"
                print("|"+Jeton, end= '')
            print("")

        print('__________________________________')


def lancerJeu():
    gagner = False
    while not gagner:
        joueurTour = self.plateau.tour % 2
        print("C'est au joueur"+joueurTour+"de jouer !")
        colonne = input("Dans quelle colonne voulez-vous jouer ?")
        case = jeu(joueurTour,colonne) 
        jeu()
        afficher()
        gagner = self.plateau.victoire(case)
        
        
        
Onjoue = Console()
Onjoue.afficher()