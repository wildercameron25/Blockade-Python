class Variables():
    #display dimensions
    DISPLAYWIDTH = None
    DISPLAYHEIGHT = None
    #different maps
    MAP = None
    #colors
    black = (0, 0, 0)
    yellow = (255, 255, 102)
    white = (255, 255, 255)
    green = (0, 255, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    #font size
    fontSize = 50
    #game state variables
    introScreen = True
    gameDone = False
    roundOver = False
    roundReady = False
    player1Ready = False
    player2Ready = False
    playAgain = True
    #score
    score = None

    def __init__(self, map = 1, width = 400, height = 300):
        self.DISPLAYWIDTH = width
        self.DISPLAYHEIGHT = height
        self.MAP = map
