class console:

    def jeu(joueur,col):
        col = [0,6]
        reponse = 0
        while reponse < 7:
            for joueur in tour:
                reponse = int(input("Dans quelle colonne de 1 à 6 veux-tu jouer ?"))
                for x in range(len[col]):
                    if reponse == col[x]:
                        """poser le pion"""
                    else:
                        x +=1