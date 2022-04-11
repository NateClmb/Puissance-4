import sys
import pygame
from p4_plateau import *


def init():

    P4 = Plateau()
    pygame.init()
    pygame.font.init()


    screen = pygame.display.set_mode([950, 590])
    playing_screen = pygame.Surface((692, 590))
    info_screen = pygame.Surface((692, 200))
    info_screen.fill((0, 0, 0))
    myfont = pygame.font.SysFont('VCR OSD Mono', 30)
    mymediumfont = pygame.font.SysFont('VCR OSD Mono', 20)
    mylittlefont = pygame.font.SysFont('VCR OSD Mono', 13)
    pygame.display.set_caption("Puissance 4")
    jetonRouge = pygame.image.load(sys.path[0] + "/PionRouge.png")
    jetonJaune = pygame.image.load(sys.path[0] + "/PionJaune.png")
    plateau = pygame.image.load(sys.path[0] + "/Grille.png")
    playing_screen.blit(plateau, (0, 0))
    screen.blit(playing_screen, (0, 0))
    screen.blit(info_screen, (693, 591))
    screen.blit(myfont.render("Puissance 4", True, (255, 255, 255)), (720, 50))
    screen.blit(mylittlefont.render("-> Au tour du joueur rouge", True, (255, 255, 255)), (710, 200))
    screen.blit(mylittlefont.render("   Au tour du joueur jaune", True, (255, 255, 255)), (710, 250))

    pygame.display.flip()
    return screen, playing_screen, info_screen, myfont, mymediumfont, mylittlefont, P4, jetonRouge, jetonJaune



done = False
screen, playing_screen, info_screen, myfont, mymediumfont, mylittlefont, P4, jetonRouge, jetonJaune = init()
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

            if P4.qui_joue() == 1:
                screen.fill(pygame.Color("black"), (710, 200, 710, 200))
                screen.fill(pygame.Color("black"), (710, 200, 710, 250))
                screen.fill(pygame.Color("black"), (710, 400, 710, 400))
                screen.fill(pygame.Color("black"), (710, 450, 710, 450))
                screen.blit(mylittlefont.render("-> Au tour du joueur rouge", True, (255, 255, 255)), (710, 200))
                screen.blit(mylittlefont.render("   Au tour du joueur jaune", True, (255, 255, 255)), (710, 250))
                pygame.display.flip()
            if P4.qui_joue() == 2:
                screen.fill(pygame.Color("black"), (710, 200, 710, 200))
                screen.fill(pygame.Color("black"), (710, 200, 710, 250))
                screen.fill(pygame.Color("black"), (710, 400, 710, 400))
                screen.fill(pygame.Color("black"), (710, 450, 710, 450))
                screen.blit(mylittlefont.render("   Au tour du joueur rouge", True, (255, 255, 255)), (710, 200))
                screen.blit(mylittlefont.render("-> Au tour du joueur jaune", True, (255, 255, 255)), (710, 250))
                pygame.display.flip()
                    
            if lignedejeu==-1 :
                screen.blit(mymediumfont.render("  Plus de place", True, (255, 0, 0)), (710, 400))
                screen.blit(mymediumfont.render("sur cette colonne !", True, (255, 0, 0)), (710, 425))
                pygame.display.flip()

            else :
                if P4.qui_joue() == 1:
                    screen.blit(jetonJaune, (16 + 97 * colonne, 13 - 97.5 * lignedejeu + 486))
                    
                    pygame.display.flip()

                if P4.qui_joue() == 2:  
                    screen.blit(jetonRouge, (16 + 97 * colonne, 13 - 97.5 * lignedejeu + 486))
                    pygame.display.flip()

            if P4.victoire(lignedejeu*7+colonne) :
                if P4.qui_joue() == 1:
                    screen.fill(pygame.Color("black"), (710, 200, 710, 200))
                    screen.fill(pygame.Color("black"), (710, 200, 710, 250))
                    screen.fill(pygame.Color("black"), (710, 400, 710, 400))
                    screen.fill(pygame.Color("black"), (710, 450, 710, 450))
                    screen.blit(mymediumfont.render("Le joueur Jaune", True, (255, 255, 0)), (720, 250))
                    screen.blit(mymediumfont.render("  a gagné ! GG", True, (255, 255, 0)), (720, 275))
                    pygame.display.flip()
                    boucle1 = False
                    
                    while boucle1 == False:
                        playing_screen.lock
                        screen.blit(mymediumfont.render("Appuyez sur Entrée", True, (255, 255, 255)), (715, 400))
                        screen.blit(mymediumfont.render("   pour rejouer", True, (255, 255, 255)), (715, 450))
                        pygame.display.flip()
                        if event.type == pygame.KEYDOWN:
                            if event.key == K_RETURN:
                                P4.reset()
                                screen, playing_screen, info_screen, myfont, mymediumfont, mylittlefont, P4, jetonRouge, jetonJaune = init()
    
                else :
                    screen.fill(pygame.Color("black"), (710, 200, 710, 200))
                    screen.fill(pygame.Color("black"), (710, 200, 710, 250))
                    screen.fill(pygame.Color("black"), (710, 400, 710, 400))
                    screen.fill(pygame.Color("black"), (710, 450, 710, 450))
                    screen.blit(mymediumfont.render("Le joueur Rouge", True, (255, 0, 0)), (720, 250))
                    screen.blit(mymediumfont.render("  a gagné ! GG", True, (255, 0, 0)), (720, 275))
                    pygame.display.flip()
                    boucle2 = False
                    
                    while boucle2 == False:
                        playing_screen.lock
                        screen.blit(mymediumfont.render("Appuyez sur Entrée", True, (255, 255, 255)), (715, 400))
                        screen.blit(mymediumfont.render("   pour rejouer", True, (255, 255, 255)), (715, 450))
                        pygame.display.flip()
                        if event.type == pygame.KEYDOWN:
                            if event.key == K_RETURN:
                                P4.reset()
                                screen, playing_screen, info_screen, myfont, mymediumfont, mylittlefont, P4, jetonRouge, jetonJaune = init()

                        
            if not P4.jeu_possible():

                screen.fill(pygame.Color("black"), (710, 200, 710, 200))
                screen.fill(pygame.Color("black"), (710, 200, 710, 250))
                screen.fill(pygame.Color("black"), (710, 400, 710, 400))
                screen.fill(pygame.Color("black"), (710, 450, 710, 450))
                screen.blit(myfont.render("Personne n'a", True, (255, 255, 255)), (710, 250))
                screen.blit(myfont.render("   gagné", True, (255, 255, 255)), (710, 275))
                screen.blit(myfont.render(" On rejoue?", True, (255, 255, 255)), (710, 300))
                pygame.display.flip()
                
