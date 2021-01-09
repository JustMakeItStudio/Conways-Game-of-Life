import pygame as pg
from random import randint, getrandbits
from Tile import Tile
from Logic import Logic


class Grid():
    SCREEN_WIDTH = 500 # width (in px)
    SCREEN_HEIGHT = 500 # height (in px)
    TileWidth = 1 # initializing the width of tile (in px)
    TileHeight = 1 # initializing the height of tile (in px)
    tilesMatrix = [] # initializing the matrix of Tile instances
    WHITE=(255,255,255)
    BLACK=(0,0,0)
    RANDOM_COLOR = (randint(0,255),randint(0,100),randint(0,255))

    def __init__(self, ni, nj):
        self.speed = 10 # frames per second when the game is running
        self.ni = ni
        self.nj = nj
        pg.init()
        self.WIN = pg.display.set_mode((Grid.SCREEN_WIDTH, Grid.SCREEN_HEIGHT), pg.RESIZABLE) 
        pg.display.set_caption('Conway\'s Game of Life v02')
        for i in range(self.ni):
            tempLst = []
            for j in range(self.nj):
                tempLst.append(Tile(xpos=i * Grid.TileWidth, ypos=j * Grid.TileHeight, state=0, i=i, j=j)) #  getrandbits(1)
            Grid.tilesMatrix.append(tempLst)
        for i in range(100):
            Grid.tilesMatrix[randint(0,ni-1)][randint(0,nj-1)].setState(1)
        self.logic = Logic(Grid.tilesMatrix)
        self.SCREEN_CENTER = (Grid.SCREEN_WIDTH/2, Grid.SCREEN_HEIGHT/2)
        self.gameLoop()

    def initialize(self):    
        Grid.TileHeight = Grid.SCREEN_HEIGHT / self.nj
        Grid.TileWidth = Grid.SCREEN_WIDTH / self.ni
        for i in range(self.ni):
            tempLst = []
            for j in range(self.nj):
                Grid.tilesMatrix[i][j].setX(i * Grid.TileWidth)
                Grid.tilesMatrix[i][j].setY(j * Grid.TileHeight)

    def gameLoop(self):
        clock = pg.time.Clock()
        running = True
        started = False
        one = 1
        while (running):
            if (started): 
                self.logic.checker()
                clock.tick(self.speed)
            ev = pg.event.get() # get all events
            for event in ev:
                if event.type == pg.MOUSEBUTTONUP:
                    pos = pg.mouse.get_pos() # x and y
                    self.pressed(pos)
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.VIDEORESIZE:
                    self.WIN = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
                    Grid.SCREEN_WIDTH = event.w
                    Grid.SCREEN_HEIGHT = event.h
                    self.initialize()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        if one > 0:
                            started = True
                            one = -1
                        else:
                            started = False
                            one = +1
                    if event.key == pg.K_p:
                        self.mainMenu()
            if pg.mouse.get_pressed()[0]:
                self.pressed(pg.mouse.get_pos())# x and y
            self.drawGrid()
            pg.display.update() # updates the screen

    def mainMenu(self):
        inMenu = True
        while inMenu:
            boxX = Grid.SCREEN_WIDTH/6
            boxY = Grid.SCREEN_HEIGHT/6
            boxWidth = Grid.SCREEN_WIDTH - boxX * 2
            boxHight = Grid.SCREEN_HEIGHT - boxY * 2 
            boxCenterX = boxWidth/2 + boxX
            boxCenterY = boxHight/2 + boxY

            Returnwidth=200
            Returnheight=60            
            Settingswidth=200
            Settingsheight=60
            Exitwidth=200
            Exitheight=60
            spaceY = 40

            ReturnxPos=boxCenterX-Returnwidth/2
            ReturnyPos=boxCenterY-spaceY-Returnheight-Settingsheight/2

            SettingsxPos=boxCenterX-Settingswidth/2
            SettingsyPos=boxCenterY-Settingsheight/2

            ExitxPos=boxCenterX-Exitwidth/2
            ExityPos=boxCenterY+spaceY+Exitheight/2

            pg.draw.rect(self.WIN,(10,10,10),(boxX, boxY , boxWidth, boxHight))
            self.drawText(text='Start', color=self.BLACK, xPos=ReturnxPos, yPos=ReturnyPos, width=Returnwidth, height=Returnheight, size=80)
            self.drawText(text='Settings', color=self.BLACK, xPos=SettingsxPos, yPos=SettingsyPos, width=Settingswidth, height=Settingsheight, size=60)
            self.drawText(text='Exit', color=self.BLACK, xPos=ExitxPos, yPos=ExityPos, width=Exitwidth, height=Exitheight, size=60)
            pg.display.update() # displays the drawScreen() stuff on the actual screen
            inMenu = self.checkForEventsINMAInMenus(MENU=True)

    def checkForEventsINMAInMenus(self, MENU=False, SETTINGS=False):
        inMenu = True
        ev = pg.event.get() # get all events
        for event in ev:
            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos() # x and y
                #inMenu = False
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.VIDEORESIZE:
                self.WIN = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
                Grid.SCREEN_WIDTH = event.w
                Grid.SCREEN_HEIGHT = event.h
                self.initialize()
            keys = pg.mouse.get_pressed()  #checking pressed keys
            if keys[0]:
                pos = pg.mouse.get_pos() # x and y
                inMenu = self.pressedMenu(pos, menu=MENU, settings=SETTINGS)
        return inMenu

    def settingsMenu(self):
        insettingsMenu = True
        while insettingsMenu:
            boxX = Grid.SCREEN_WIDTH/6
            boxY = Grid.SCREEN_HEIGHT/6
            boxWidth = Grid.SCREEN_WIDTH - boxX * 2
            boxHight = Grid.SCREEN_HEIGHT - boxY * 2 
            boxCenterX = boxWidth/2 + boxX
            boxCenterY = boxHight/2 + boxY

            Returnwidth=200
            Returnheight=60            
            Settingswidth=200
            Settingsheight=60
            Backwidth=200
            Backheight=60
            spaceY = 40

            ReturnxPos=boxCenterX-Returnwidth/2
            ReturnyPos=boxCenterY-spaceY-Returnheight-Settingsheight/2

            SettingsxPos=boxCenterX-Settingswidth/2
            SettingsyPos=boxCenterY-Settingsheight/2

            BackxPos=boxCenterX-Backwidth/2
            BackyPos=boxCenterY+spaceY+Backheight/2

            pg.draw.rect(self.WIN,(10,10,10),(boxX, boxY , boxWidth, boxHight))
            self.drawText(text='Setting 1', color=self.BLACK, xPos=ReturnxPos, yPos=ReturnyPos, width=Returnwidth, height=Returnheight, size=60)
            self.drawText(text='Setting 2', color=self.BLACK, xPos=SettingsxPos, yPos=SettingsyPos, width=Settingswidth, height=Settingsheight, size=60)
            self.drawText(text='Back', color=self.BLACK, xPos=BackxPos, yPos=BackyPos, width=Backwidth, height=Backheight, size=60)
            pg.display.update() # displays the drawScreen() stuff on the actual screen
            insettingsMenu = self.checkForEventsINMAInMenus(SETTINGS=True)

    def drawText(self, text, color, xPos, yPos, width, height, size):
        pg.draw.rect(self.WIN, Grid.RANDOM_COLOR, (xPos, yPos, width, height))
        font = pg.font.Font(None, size)
        text_ = font.render(text, True, color)
        text_rect = text_.get_rect(center=(xPos+width/2, yPos+height/2))
        if text_ is not None: self.WIN.blit(text_, text_rect)

    def pressedMenu(self, pos, menu=False, settings=False):
        boxX = Grid.SCREEN_WIDTH/6
        boxY = Grid.SCREEN_HEIGHT/6
        boxWidth = Grid.SCREEN_WIDTH - boxX * 2
        boxHight = Grid.SCREEN_HEIGHT - boxY * 2 
        boxCenterX = boxWidth/2 + boxX
        boxCenterY = boxHight/2 + boxY

        Returnwidth=200
        Returnheight=60            
        Settingswidth=200
        Settingsheight=60
        Exitwidth=200
        Exitheight=60
        spaceY = 40

        ReturnxPos=boxCenterX-Returnwidth/2
        ReturnyPos=boxCenterY-spaceY-Returnheight-Settingsheight/2

        SettingsxPos=boxCenterX-Settingswidth/2
        SettingsyPos=boxCenterY-Settingsheight/2

        ExitxPos=boxCenterX-Exitwidth/2
        ExityPos=boxCenterY+spaceY+Exitheight/2

        pressedSomething = False
        # Return
        if (pos[0] > ReturnxPos and pos[0] < (ReturnxPos + Returnwidth)):
            if (pos[1] > ReturnyPos and pos[1] < (ReturnyPos + Returnheight)):
                if menu:
                    return False
                if settings:
                    return False
                pressedSomething = True
        # Settings
        if (pos[0] > SettingsxPos and pos[0] < SettingsxPos + Settingswidth):
            if (pos[1] > SettingsyPos and pos[1] < SettingsyPos + Settingsheight):
                self.settingsMenu()
                pressedSomething = True
                return True
        # Exit
        if (pos[0] > ExitxPos and pos[0] < ExitxPos + Exitwidth):
            if (pos[1] > ExityPos and pos[1] < ExityPos + Exitheight):
                if menu:
                    quit()
                if settings:
                    pressedSomething = True
                    return False
        if not pressedSomething:
            return True
    
    def pressed(self, pos):
        for x in range(self.ni):
            for y in range(self.nj):
                if (pos[0] > Grid.tilesMatrix[x][y].getX() and pos[0] < Grid.tilesMatrix[x][y].getX() + Grid.TileWidth):
                    if (pos[1] > Grid.tilesMatrix[x][y].getY() and pos[1] < Grid.tilesMatrix[x][y].getY() + Grid.TileHeight):
                        Grid.tilesMatrix[x][y].setState(1)

    def drawGrid(self):
        self.WIN.fill(Grid.BLACK)
        for i in range(self.ni):
            for j in range(self.nj):
                if (Grid.tilesMatrix[i][j].getState() == 0):
                    color = Grid.BLACK
                elif (Grid.tilesMatrix[i][j].getState() == 1):
                    color = Grid.RANDOM_COLOR
                pg.draw.rect(self.WIN,color,(Grid.tilesMatrix[i][j].getX()+1,Grid.tilesMatrix[i][j].getY()+1,Grid.TileWidth-1,Grid.TileHeight-1))
                

Grid(50,50) # ni, nj