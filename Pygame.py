import pygame
tamere = 0
pygame.init()
screen = pygame.display.set_mode([950, 590])
white = [255, 255, 255]


screen.fill(white)
jetonRouge = pygame.image.load("/home/colomban/Documents/NSI/Puissance4/modules/jeton-rouge.png")
jetonJaune = pygame.image.load("/home/colomban/Documents/NSI/Puissance4/modules/jeton-jaune.png")
plateau = pygame.image.load("/home/colomban/Documents/NSI/Puissance4/modules/plateau.png")
screen.blit(plateau, (0, 0))
pygame.display.flip()

# Run until the user asks to quit

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    if pygame.mouse.get_pressed()[0]:
        screen.blit(jetonJaune, (16 + 97 * 2, 13 - 97.5 * 5 + 486))
        pygame.display.flip()
  
    


    # Done! Time to quit.

pygame.quit()