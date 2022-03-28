#imports needed packages
import sys
import pygame
import gameFunctions as game
#initializes all pygame modules
pygame.init()

#sets up the display
dis=pygame.display.set_mode((game.var.DISPLAYWIDTH, game.var.DISPLAYHEIGHT))
#gives display window a title
pygame.display.set_caption("Blockade By Cameron Wilder")

#sets game clock
clock = pygame.time.Clock()

#game runs
while not game.var.gameDone:

    if game.var.introScreen:
        game.introScreen(dis)

    game.waitReadyState(dis)

    game.playerInput()

    game.checkPlayerPosition(dis)

    game.checkRoundState(dis)

    game.registerMovement()

    game.displayMovement(dis, clock)

#exits the program safely
pygame.quit()
sys.exit(0)