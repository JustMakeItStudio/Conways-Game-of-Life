# Conway's Game Of Life Clone

Build in Python 3.
## The aim
Is to recreate the Conway's game of life using python. The tile rendering is given as a separate repository here:
```sh
https://github.com/rocku0/Tile-renderer
```
### Actual implementation
A tile world is created from the Grid class. Each tile has two states, 0 is dead (black), and 1 is alive (white). Every new generation the tree rules of the game are applied on the tile grid. 
##### The rules are:
1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.
 
To create the grid, navigate at the bottom of the Grid.py file, input the desired grid size as shown bellow, and run the Grid.py file.
```sh
Grid(10, 20) # ni, nj
# Creates a grid 10 tiles horizontally and 20 tiles vertically
```
You can pause and resume the game by pressing "SPACE", while paused you can draw live tiles with the mouse.
Now to speed up the ganerations, navigate to the gameloop function, and lower the number inside the "sleep()" function.
#### Libraries used:
- [pygame]
- [time]
- [random]

### Installation
To run the code you need Python3, and the libraries above installed on your computer.
To install a libray for python open the command prompt and follow the example bellow.

```sh
$ pip install pygame
```

To clone the repository, open the command prompt at the directory of choise and type:
```sh
$  git clone --recursive https://github.com/rocku0/Conways-Game-of-Life.git
```
### An example:
#### Draw this little dinosaur.
![image](https://user-images.githubusercontent.com/71210416/105625331-23163b00-5e31-11eb-8c22-f18357f0b4c8.png)
#### Now when you press SPACE:
![image](https://user-images.githubusercontent.com/71210416/105625385-99b33880-5e31-11eb-82f6-08a4767b801f.png)
#### And the menu appeares when you press p:
![image](https://user-images.githubusercontent.com/71210416/105625389-a20b7380-5e31-11eb-8ac3-68e6d927f54e.png)


**Use this as you like**

   [pygame]: <https://www.pygame.org/docs/>
   [time]: <https://docs.python.org/3/library/time.html>
   [random]: <https://docs.python.org/3/library/random.html>
