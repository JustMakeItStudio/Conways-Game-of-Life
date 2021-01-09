class Logic:
    def __init__(self, tilesMatrix):
        self.tilesMatrix = tilesMatrix
        self.ni = len(tilesMatrix)
        self.nj = len(tilesMatrix[1])
    
    def checker(self):
        num_neighbours = []
        for i in range(self.ni):
            temp = []
            for j in range(self.nj):
                temp.append(0) 
            num_neighbours.append(temp)

        for i in range(self.ni):
            for j in range(self.nj):
                # Center box
                if 0 < i < self.ni-1 and 0 < j < self.nj-1:
                    if self.tilesMatrix[i+1][j].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j] + 1 

                    if self.tilesMatrix[i-1][j].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                    if self.tilesMatrix[i][j+1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1
                        
                    if self.tilesMatrix[i][j-1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1
                    
                    if self.tilesMatrix[i+1][j+1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                    if self.tilesMatrix[i+1][j-1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                    if self.tilesMatrix[i-1][j+1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                    if self.tilesMatrix[i-1][j-1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                # Left vertical line 
                
                if i == 0 and 0 < j < self.nj-1:
                    if self.tilesMatrix[i+1][j].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                    if self.tilesMatrix[i][j+1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1
                        
                    if self.tilesMatrix[i][j-1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                    if self.tilesMatrix[i+1][j+1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1
                    if self.tilesMatrix[i+1][j-1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                # Top line
                if 0 < i < self.ni-1 and j == 0:
                    if self.tilesMatrix[i+1][j].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                    if self.tilesMatrix[i-1][j].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1
                        
                    if self.tilesMatrix[i][j+1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                    if self.tilesMatrix[i+1][j+1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1
                    if self.tilesMatrix[i-1][j+1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                # Right vertical line
                if i == self.ni-1 and 0 < j < self.nj-1:
                    if self.tilesMatrix[i-1][j].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                    if self.tilesMatrix[i][j+1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1
                        
                    if self.tilesMatrix[i][j-1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                    if self.tilesMatrix[i-1][j+1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1
                    if self.tilesMatrix[i-1][j-1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                # Bottom line
                if 0 < i < self.ni-1 and j == self.nj-1:
                    if self.tilesMatrix[i+1][j].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                    if self.tilesMatrix[i-1][j].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1
                        
                    if self.tilesMatrix[i][j-1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                    if self.tilesMatrix[i+1][j-1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1
                    if self.tilesMatrix[i-1][j-1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                # Top left corner
                if i == 0 and j == 0:
                    if self.tilesMatrix[i+1][j].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                    if self.tilesMatrix[i][j+1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1
                        
                    if self.tilesMatrix[i+1][j+1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                # Top right corner
                if i == self.ni-1 and j == 0:
                    if self.tilesMatrix[i-1][j].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                    if self.tilesMatrix[i][j+1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1
                        
                    if self.tilesMatrix[i-1][j+1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                # Bottom right corner
                if i == self.ni-1 and j == self.nj-1:
                    if self.tilesMatrix[i-1][j].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                    if self.tilesMatrix[i][j-1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1
                        
                    if self.tilesMatrix[i-1][j-1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                # Bottom left corner
                if i == 0 and j == self.nj-1:
                    if self.tilesMatrix[i+1][j].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1

                    if self.tilesMatrix[i][j-1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1
                        
                    if self.tilesMatrix[i+1][j-1].getState() == 1:
                        num_neighbours[i][j] = num_neighbours[i][j]+1
        self.checkNeighbours(num_neighbours)
        
    def checkNeighbours(self, num_neighbours):
        for i in range(self.ni):
            for j in range(self.nj):
                if num_neighbours[i][j] > 1 and num_neighbours[i][j] < 4 and self.tilesMatrix[i][j].getState() == 1:
                    self.tilesMatrix[i][j].setState(1)
                elif num_neighbours[i][j] == 3 and self.tilesMatrix[i][j].getState() == 0:
                    self.tilesMatrix[i][j].setState(1)
                else:
                    self.tilesMatrix[i][j].setState(0)

