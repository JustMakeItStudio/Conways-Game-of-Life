import pygame as pg
import numpy as np
from random import randint, getrandbits

class Grid:
    SCREEN_WIDTH = 500 # width (in px)
    SCREEN_HEIGHT = 500 # height (in px)
    TileWidth = 1 # initializing the width of tile (in px)
    TileHeight = 1 # initializing the height of tile (in px)
    tilesMatrix = [] # initializing the matrix of Tile instances
    WHITE=(255,255,255)
    BLUE=(0,0,255)
    BLACK=(0,0,0)
    RED = (255,0,0)

    def __init__(self, ni, nj):
        self.grid = [[0]*ni,[0]*nj] # Number of nodes in x and y direction
        self.ni = ni
        self.nj = nj
        pg.init()
        self.WIN = pg.display.set_mode((Grid.SCREEN_WIDTH, Grid.SCREEN_HEIGHT), pg.RESIZABLE) # creates a screen of 600px X 800px
        pg.display.set_caption('Tile Renderer V02')
        self.font = pg.font.Font(None,20)
        for i in range(self.ni):
            tempLst = []
            for j in range(self.nj):
                tempLst.append(Tile(xpos=i * Grid.TileWidth, ypos=j * Grid.TileHeight, state=0, i=i, j=j)) #  getrandbits(1)
            Grid.tilesMatrix.append(tempLst)
        for i in range(round((ni-1)*(nj-1)/10)):
            Grid.tilesMatrix[randint(0,ni-1)][randint(0,nj-1)].setState(1)
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
        running = True
        while (running):
            pg.display.update() # updates the screen
            self.drawGrid()
            ev = pg.event.get() # get all events
            for event in ev:
                if event.type == pg.MOUSEBUTTONUP:
                    pos = pg.mouse.get_pos() # x and y
                    running = self.pressed(pos)
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.VIDEORESIZE:
                    self.WIN = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
                    Grid.SCREEN_WIDTH = event.w
                    Grid.SCREEN_HEIGHT = event.h
                    self.initialize()
            if running is None: 
                running = True

    def pressed(self, pos):
        for x in range(self.ni):
            for y in range(self.nj):
                if (pos[0] > Grid.tilesMatrix[x][y].getX() and pos[0] < Grid.tilesMatrix[x][y].getX() + Grid.TileWidth):
                    if (pos[1] > Grid.tilesMatrix[x][y].getY() and pos[1] < Grid.tilesMatrix[x][y].getY() + Grid.TileHeight):
                        Grid.tilesMatrix[x][y].setState(1)
                        return True

    def drawGrid(self):
        text = None
        for i in range(self.ni):
            for j in range(self.nj):
                pg.draw.rect(self.WIN,Grid.WHITE,(Grid.tilesMatrix[i][j].getX(),Grid.tilesMatrix[i][j].getY(),Grid.TileWidth,Grid.TileHeight))
                if (Grid.tilesMatrix[i][j].getState() == 0):
                    color = Grid.BLACK
                elif (Grid.tilesMatrix[i][j].getState() == 1):
                    color = Grid.BLUE
                    #text = self.font.render("test", True, Grid.WHITE)
                    #text_rect = text.get_rect(center=(Grid.tilesMatrix[i][j].getX()+Grid.TileWidth/2, Grid.tilesMatrix[i][j].getY()+Grid.TileHeight/2))
                pg.draw.rect(self.WIN,color,(Grid.tilesMatrix[i][j].getX()+1,Grid.tilesMatrix[i][j].getY()+1,Grid.TileWidth-1,Grid.TileHeight-1))
                if text is not None: 
                    self.WIN.blit(text, text_rect)
                


#newGrid = Grid(50,40) # ni, nj