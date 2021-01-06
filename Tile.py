class Tile:
    def __init__(self, xpos, ypos, state, i, j):
        self.xpos = xpos # pixel count in x direction from the left
        self.ypos = ypos # pixel count in y direction from the top
        self.state = state # 0: Dead (unclicked), 1: Alive (Clicked) 
        self.i = i # An integer showing the node in the x axis
        self.j = j # An integer showing the node in the y axis
    
    def getX(self):
        return self.xpos
    def getY(self):
        return self.ypos
    def getState(self):
        return self.state

    def setX(self, x):
        self.xpos = x
    def setY(self, y):
        self.ypos = y
    def setState(self, state):
        self.state = state
      