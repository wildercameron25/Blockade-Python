import pygame
#creates green player
class Player1():
    color = None
    size = 10
    xPos = None
    yPos = None
    xHistory = []
    yHistory = []
    trailLength = 0
    xChange = 0
    yChange = 0
    score = 0

    initXPos = None
    initYPos = None

    def __init__(self, color = (0, 255, 0), map = 1):
        self.color = color

    def move(self):
        self.xPos += self.xChange
        self.yPos += self.yChange
        self.trailLength += 1
        self.xHistory.append(self.xPos)
        self.yHistory.append(self.yPos)

    def draw(self, screen):
        for x, y in zip(self.xHistory, self.yHistory):
            pygame.draw.rect(screen, self.color, [x, y, self.size, self.size])

    def reset(self):
        self.xPos = self.initXPos
        self.yPos = self.initYPos
        self.xChange = 0
        self.yChange = 0
        self.trailLength = 0
        self.xHistory = []
        self.yHistory = []

#creates red player
class Player2():
    color = None
    size = 10
    xPos = None
    yPos = None
    xHistory = []
    yHistory = []
    trailLength = 0
    xChange = 0
    yChange = 0
    score = 0

    initXPos = None
    initYPos = None

    def __init__(self, color = (255, 0, 0), map = 1):
        self.color = color

    def move(self):
        self.xPos += self.xChange
        self.yPos += self.yChange
        self.trailLength += 1
        self.xHistory.append(self.xPos)
        self.yHistory.append(self.yPos)

    def draw(self, screen):
        for x, y in zip(self.xHistory, self.yHistory):
            pygame.draw.rect(screen, self.color, [x, y, self.size, self.size])

    def reset(self):
        self.xPos = self.initXPos
        self.yPos = self.initYPos
        self.xChange = 0
        self.yChange = 0
        self.trailLength = 0
        self.xHistory = []
        self.yHistory = []