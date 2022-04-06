import sys
import pygame
from p4_plateau import *


P4 = Plateau()
pygame.init()
pygame.font.init()


screen = pygame.display.set_mode([950, 590])
playing_screen = pygame.Surface((692, 590))
info_screen = pygame.Surface((692, 200))
info_screen.fill((0, 0, 0))
pygame.display.set_caption("Puissance 4")

white = [255, 255, 255]
black = [0, 0, 0]

#Pour ce code, nous utilisons 3 images : le plateau, le pion rouge et le pion jaune, il faut donc au préalable les télécharger
#Vous les retrouverez sur CheekyNate/Puissance-4.

jetonRouge = pygame.image.load(sys.path[0] + "/pion_rouge.png")
jetonJaune = pygame.image.load(sys.path[0] + "/pion_jaune.png")
plateau = pygame.image.load(sys.path[0] + "/plateau.png")
playing_screen.blit(plateau, (0, 0))
screen.blit(playing_screen, (0, 0))
screen.blit(info_screen, (693, 591))
pygame.display.flip()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # This block is executed once for each MOUSEBUTTONDOWN event.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if 17 <= pos[0] <= 99:
                colonne = 0
            elif 115 <= pos[0] <= 195:
                colonne = 1
            elif 211 <= pos[0] <= 291:
                colonne = 2
            elif 309 <= pos[0] <= 388:
                colonne = 3
            elif 404 <= pos[0] <= 484:
                colonne = 4
            elif 501 <= pos[0] <= 581:
                colonne = 5
            elif 597 <= pos[0] <= 678:
                colonne = 6
            
            lignedejeu = P4.jouer(colonne)
            if lignedejeu==-1 :
                print("bonjour")
            else :
                if P4.qui_joue() == 1:
                    screen.blit(jetonJaune, (16 + 97 * colonne, 13 - 97.5 * lignedejeu + 486))
                    pygame.display.flip()

                if P4.qui_joue() == 2:
                    screen.blit(jetonRouge, (16 + 97 * colonne, 13 - 97.5 * lignedejeu + 486))
                    pygame.display.flip()
            if P4.victoire(lignedejeu*7+colonne) :
                print('tamere')

            if not P4.jeu_possible():

                print('cest fini')
