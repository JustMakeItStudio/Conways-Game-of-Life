
class Logic:
    def __init__(self, tilesMatrix):
        self.tilesMatrix = tilesMatrix
        self.nj = len(tilesMatrix)
        self.ni = len(tilesMatrix[1])
        print(self.ni)
        print(self.nj)
    
    def checker(self):
        for i in range(self.ni):
            for j in range(self.nj):
                num_neighbours[i][j] = 0

        for i in range(self.ni):
            for j in range(self.nj):
                # Center box
                if 0 < i < self.ni-1 and 0 < j < self.nj-1:
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i+1][j].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]

                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i-1][j].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]

                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i][j+1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]
                        
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i][j-1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]
                    
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i+1][j+1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i+1][j-1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i-1][j+1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i-1][j-1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]

                # Left vertical line
                if i == 0 and 0 < j < self.nj-1:
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i+1][j].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]

                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i][j+1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]
                        
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i][j-1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]

                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i+1][j+1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i+1][j-1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]

                # Top line
                if 0 < i < self.ni-1 and j == 0:
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i+1][j].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]

                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i-1][j].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]
                        
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i][j+1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]

                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i+1][j+1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i-1][j+1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]
                # Right vertical line
                if i == self.ni-1 and 0 < j < self.nj-1:
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i-1][j].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]

                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i][j+1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]
                        
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i][j-1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]

                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i-1][j+1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i-1][j-1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]
                # Bottom line
                if 0 < i < self.ni-1 and j == self.nj-1:
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i+1][j].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]

                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i-1][j].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]
                        
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i][j-1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]

                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i+1][j-1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i-1][j-1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]
                # Top left corner
                if i == 0 and j == 0:
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i+1][j].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]

                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i][j+1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]
                        
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i+][j+1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]

                # Top right corner
                if i == self.ni-1 and j == 0:
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i-1][j].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]

                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i][j+1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]
                        
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i-1][j+1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]

                # Bottom right corner
                if i == self.ni-1 and j == self.nj-1:
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i-1][j].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]

                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i][j-1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]
                        
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i-1][j-1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]
                # Bottom left corner
                if i == 0 and j == self.nj-1:
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i+1][j].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]

                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i][j-1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]
                        
                    if Grid.tilesMatrix[i][j].getState() == 1 and Grid.tilesMatrix[i+1][j-1].getState() == 1:
                        num_neighbours[i][j] += num_neighbours[i][j]
        self.checkNeighbours(num_neighbours)
        