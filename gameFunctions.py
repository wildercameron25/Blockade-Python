import variable
import players
import time
import pygame   

player1 = players.Player1()
player2 = players.Player2()
var = variables.Variables()

#displays a string on display
def message(display, msg, color, xLoc, yLoc, size=50):
    fontStyle = pygame.font.SysFont(None, size)
    mesg = fontStyle.render(msg, True, color)
    display.blit(mesg, [xLoc, yLoc])
#waits for player input
def waitReadyState(display):
    while not var.roundReady:
        display.fill(var.black)
        pygame.draw.rect(display, player1.color, [player1.xPos, player1.yPos, player1.size, player1.size])
        pygame.draw.rect(display, player2.color, [player2.xPos, player2.yPos, player2.size, player2.size])
        message(display, "Input Direction to Begin", var.white, var.DISPLAYWIDTH/4, var.DISPLAYHEIGHT/2, 30)
        pygame.display.update()

        for event in pygame.event.get():
            #checks if player quit
           if event.type == pygame.QUIT:
               var.roundReady = True
               var.gameDone = True
           elif event.type == pygame.KEYDOWN:
               #checks for key input from player2
                if not var.player2Ready and event.key == pygame.K_LEFT:
                    player2.xChange = -10
                    player2.yChange = 0
                    var.player2Ready = True
                elif not var.player2Ready and event.key == pygame.K_RIGHT:
                    player2.xChange = 10
                    player2.yChange = 0
                    var.player2Ready = True
                elif not var.player2Ready and event.key == pygame.K_UP:
                    player2.xChange = 0
                    player2.yChange = -10
                    var.player2Ready = True
                elif not var.player2Ready and event.key == pygame.K_DOWN:
                    player2.xChange = 0
                    player2.yChange = 10
                    var.player2Ready = True
                #check for key input from player1
                if not var.player1Ready and event.key == pygame.K_a:
                    player1.xChange = -10
                    player1.yChange = 0
                    var.player1Ready = True
                elif not var.player1Ready and event.key == pygame.K_d:
                    player1.xChange = 10
                    player1.yChange = 0
                    var.player1Ready = True
                elif not var.player1Ready and event.key == pygame.K_w:
                    player1.xChange = 0
                    player1.yChange = -10
                    var.player1Ready = True
                elif not var.player1Ready and event.key == pygame.K_s:
                    player1.xChange = 0
                    player1.yChange = 10
                    var.player1Ready = True
            
        if var.player2Ready and var.player1Ready:
            display.fill(var.black)
            pygame.draw.rect(display, player1.color, [player1.xPos, player1.yPos, player1.size, player1.size])
            pygame.draw.rect(display, player2.color, [player2.xPos, player2.yPos, player2.size, player2.size])
            message(display, "Start in:", var.white, var.DISPLAYWIDTH/4, var.DISPLAYHEIGHT/2, 30)
            message(display, "3", var.white, var.DISPLAYWIDTH/4, var.DISPLAYHEIGHT/2 + 50, 30)
            pygame.display.update()
            time.sleep(1)
            display.fill(var.black)
            pygame.draw.rect(display, player1.color, [player1.xPos, player1.yPos, player1.size, player1.size])
            pygame.draw.rect(display, player2.color, [player2.xPos, player2.yPos, player2.size, player2.size])
            message(display, "Start in:", var.white, var.DISPLAYWIDTH/4, var.DISPLAYHEIGHT/2, 30)
            message(display, "2", var.white, var.DISPLAYWIDTH/4, var.DISPLAYHEIGHT/2 + 50, 30)
            pygame.display.update()
            time.sleep(1)
            display.fill(var.black)
            pygame.draw.rect(display, player1.color, [player1.xPos, player1.yPos, player1.size, player1.size])
            pygame.draw.rect(display, player2.color, [player2.xPos, player2.yPos, player2.size, player2.size])
            message(display, "Start in:", var.white, var.DISPLAYWIDTH/4, var.DISPLAYHEIGHT/2, 30)
            message(display, "1", var.white, var.DISPLAYWIDTH/4, var.DISPLAYHEIGHT/2 + 50, 30)
            pygame.display.update()
            time.sleep(1)
            var.player2Ready = False
            var.player1Ready = False
            var.roundReady = True
#checks for player movement input
def playerInput():
    for event in pygame.event.get():
        #checks if exit is clicked
        if event.type == pygame.QUIT:
            var.gameDone = True
        if event.type == pygame.KEYDOWN:
            #checks for key input from player2
            if event.key == pygame.K_LEFT:
                player2.xChange = -10
                player2.yChange = 0
            elif event.key == pygame.K_RIGHT:
                player2.xChange = 10
                player2.yChange = 0
            elif event.key == pygame.K_UP:
                player2.xChange = 0
                player2.yChange = -10
            elif event.key == pygame.K_DOWN:
                player2.xChange = 0
                player2.yChange = 10
            #check for key input from player1
            if event.key == pygame.K_a:
                player1.xChange = -10
                player1.yChange = 0
            elif event.key == pygame.K_d:
                player1.xChange = 10
                player1.yChange = 0
            elif event.key == pygame.K_w:
                player1.xChange = 0
                player1.yChange = -10
            elif event.key == pygame.K_s:
                player1.xChange = 0
                player1.yChange = 10
#checks if either player is out of bounds or if either player hit a trail
def checkPlayerPosition(display):
    #checks if player2 hit edge
    if player2.xPos >= var.DISPLAYWIDTH or player2.xPos <= 0 or player2.yPos >= var.DISPLAYHEIGHT or player2.yPos <= 0:
        var.roundOver = True
        message(display, "Point Player 1", var.yellow, var.DISPLAYWIDTH/4, var.DISPLAYHEIGHT/2)
        pygame.display.update()
        player1.score += 1
        time.sleep(2)
    #checks if player1 hit edge
    if player1.xPos >= var.DISPLAYWIDTH or player1.xPos <= 0 or player1.yPos >= var.DISPLAYHEIGHT or player1.yPos <= 0:
        var.roundOver = True
        message(display, "Point Player 2", var.yellow, var.DISPLAYWIDTH/4, var.DISPLAYHEIGHT/2)
        pygame.display.update()
        player2.score += 1
        time.sleep(2)
    #checks if player2 hit player1 trail
    for x, y in zip(player1.xHistory, player1.yHistory):
        if player2.xPos == x and player2.yPos == y:
            var.roundOver = True
            message(display, "Point Player 1", var.yellow, var.DISPLAYWIDTH/4, var.DISPLAYHEIGHT/2)
            pygame.display.update()
            player1.score += 1
            time.sleep(2)
    #checks if player1 hit player2 trail
    for x, y in zip(player2.xHistory, player2.yHistory):
        if player1.xPos == x and player1.yPos == y:
            var.roundOver = True
            message(display, "Point Player 2", var.yellow, var.DISPLAYWIDTH/4, var.DISPLAYHEIGHT/2)
            pygame.display.update()
            player2.score += 1
            time.sleep(2)
    #checks if player1 hit own trail
    for i in range(player1.trailLength):
        if i > 0:
            if player1.xPos == player1.xHistory[i-1] and player1.yPos == player1.yHistory[i-1]:
                var.roundOver = True
                message(display, "Point Player 2", var.yellow, var.DISPLAYWIDTH/4, var.DISPLAYHEIGHT/2)
                pygame.display.update()
                player2.score += 1
                time.sleep(2)
    #checks if player2 hit own trail
    for i in range(player2.trailLength):
        if i > 0:
            if player2.xPos == player2.xHistory[i-1] and player2.yPos == player2.yHistory[i-1]:
                var.roundOver = True
                message(display, "Point Player 1", var.yellow, var.DISPLAYWIDTH/4, var.DISPLAYHEIGHT/2)
                pygame.display.update()
                player1.score += 1
                time.sleep(2)
#checks if a player has lost
def checkRoundState(display):
    if var.roundOver:
        display.fill(var.black)
        #reset player 2
        player2.reset()
        #resets player1
        player1.reset()
        #updates score
        var.score = str(player1.score) + " vs " + str(player2.score)
        message(display, var.score, var.white, var.DISPLAYWIDTH*0.375, var.DISPLAYHEIGHT/2)
        pygame.display.update()
        time.sleep(2)
        var.roundOver = False
        var.roundReady = False
#adds current position of players to history
def registerMovement():
    #registers player movement
    try:
        player2.move()
        player1.move()
    except:
        None
#displays player momvement on display
def displayMovement(display, clock, speed = 20):
    #displays player movement
    display.fill(var.black)
    player1.draw(display)
    player2.draw(display)
    pygame.display.update()
    #controls player speed
    clock.tick(speed)


def introScreen(display):
    message(display, "Select Screen Size", (255, 255, 255), display.get_width() * 0.1, display.get_height() * (1/30), var.fontSize)
    message(display, "Small", (255, 255, 255), display.get_width() * 0.125, display.get_height() * (7/30), var.fontSize)
    message(display, "Medium", (255, 255, 255), display.get_width() * 0.5, display.get_height() * (7/30), var.fontSize)
    message(display, "Large", (255, 255, 255), display.get_width() * 0.125, display.get_height() * 0.5, var.fontSize)
    message(display, "Instructions", (255, 255, 255), display.get_width() * 0.45, display.get_height() * 0.5, var.fontSize)
    message(display, "Confirm", (255, 255, 255), display.get_width() * 0.3125, display.get_height() * 0.75, var.fontSize)
    pygame.display.update()
    while var.introScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                var.gameDone = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                #checks if 'Small' was clicked
                if pos[0] > display.get_width() * 0.125 and pos[0] < display.get_width() * 0.3625 and pos[1] > display.get_height() * (7/30) and pos[1] < display.get_height() * 0.32:
                    var.fontSize = 50
                    display = pygame.display.set_mode((400, 300))
                    display.fill(var.black)
                    message(display, "Select Screen Size", (255, 255, 255), display.get_width() * 0.1, display.get_height() * (1/30), var.fontSize)
                    message(display, "Small", (255, 255, 255), display.get_width() * 0.125, display.get_height() * (7/30), var.fontSize)
                    message(display, "Medium", (255, 255, 255), display.get_width() * 0.5, display.get_height() * (7/30), var.fontSize)
                    message(display, "Large", (255, 255, 255), display.get_width() * 0.125, display.get_height() * 0.5, var.fontSize)
                    message(display, "Instructions", (255, 255, 255), display.get_width() * 0.45, display.get_height() * 0.5, var.fontSize)
                    message(display, "Confirm", (255, 255, 255), display.get_width() * 0.3125, display.get_height() * 0.75, var.fontSize)
                    pygame.display.update()
                    time.sleep(0.2)
                #checks if 'Medium' was clicked
                if pos[0] > display.get_width() * 0.5 and pos[0] < display.get_width() * 0.825 and pos[1] > display.get_height() * (7/30) and pos[1] < display.get_height() * 0.32:
                    var.fontSize = 100
                    display = pygame.display.set_mode((800, 600))
                    display.fill(var.black)
                    message(display, "Select Screen Size", (255, 255, 255), display.get_width() * 0.1, display.get_height() * (1/30), var.fontSize)
                    message(display, "Small", (255, 255, 255), display.get_width() * 0.125, display.get_height() * (7/30), var.fontSize)
                    message(display, "Medium", (255, 255, 255), display.get_width() * 0.5, display.get_height() * (7/30), var.fontSize)
                    message(display, "Large", (255, 255, 255), display.get_width() * 0.125, display.get_height() * 0.5, var.fontSize)
                    message(display, "Instructions", (255, 255, 255), display.get_width() * 0.45, display.get_height() * 0.5, var.fontSize)
                    message(display, "Confirm", (255, 255, 255), display.get_width() * 0.3125, display.get_height() * 0.75, var.fontSize)
                    pygame.display.update()
                    time.sleep(0.2)
                #checks if 'Large' was clicked
                if pos[0] > display.get_width() * 0.125 and pos[0] < display.get_width() * 0.355 and pos[1] > display.get_height() * 0.5 and pos[1] < (display.get_height() * (181/300)):
                    var.fontSize = 125
                    display = pygame.display.set_mode((1000, 750))
                    display.fill(var.black)
                    message(display, "Select Screen Size", (255, 255, 255), display.get_width() * 0.1, display.get_height() * (1/30), var.fontSize)
                    message(display, "Small", (255, 255, 255), display.get_width() * 0.125, display.get_height() * (7/30), var.fontSize)
                    message(display, "Medium", (255, 255, 255), display.get_width() * 0.5, display.get_height() * (7/30), var.fontSize)
                    message(display, "Large", (255, 255, 255), display.get_width() * 0.125, display.get_height() * 0.5, var.fontSize)
                    message(display, "Instructions", (255, 255, 255), display.get_width() * 0.45, display.get_height() * 0.5, var.fontSize)
                    message(display, "Confirm", (255, 255, 255), display.get_width() * 0.3125, display.get_height() * 0.75, var.fontSize)
                    pygame.display.update()
                    time.sleep(0.2)
                #checks if 'Instructions' was clicked
                if pos[0] > display.get_width() * 0.45 and pos[0] < display.get_width() * 0.9625 and pos[1] > display.get_height() * 0.5 and pos[1] < display.get_height() * (44/75):
                    display.fill(var.black)
                    pygame.display.update()
                    time.sleep(0.2)
                #checks if 'Confirm' was clicked
                if pos[0] > display.get_width() * 0.3125 and pos[0] < display.get_width() * 0.6425 and pos[1] > display.get_height() * 0.75 and pos[1] < display.get_height() * 0.84:
                    display.fill(var.black)
                    pygame.display.update()
                    var.introScreen = False