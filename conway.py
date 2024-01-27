#############################
### CONWAY'S GAME OF LIFE ###
#############################

# Play the game on 3 different manifolds! Call conway(initial_state, iteration_number, topology, padding)

## The manifolds:
# - Square (use 'lift' for topology, 'zeros' for padding)
# - Klein bottle (use 'lift' for topology, 'Klein' for padding)
# - Torus (use 'factor' for topology, omit padding) 

## Possible initial states:
# - Random 
# - Blinker
# - Glider
# - Pulsar

# More: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

import os
import shutil
from time import sleep
# import numpy as np

def padding(cells, padding_style):
# create a padding around the square to mimic neighbours on the far side
    
    if padding_style == "zeros":
        cells = [len(cells[0])*[0]] + cells + [len(cells[0])*[0]] 
        for i in range(len(cells)):
            cells[i] = [0] + cells[i] + [0]
    elif padding_style == "Klein":
        cells = [cells[-1][::-1]] + cells + [cells[0][::-1]]     
        for i in range(len(cells)):
            cells[i] = [cells[i][-1]] + cells[i] + [cells[i][0]]
    
    return cells


def next_gen(cells, *args):
# compute new system state (as 0/1 matrix) from old
    
    temp = [0]*len(cells[0])
    new_cells = [temp[:] for i in range(len(cells))]
    
    if args[0] == "lift":
        cells = padding(cells, args[1])
    
    n = len(cells)
    m = len(cells[0])

    if args[0] == "factor":
        for i in range(0, n):
            for j in range(0, m):
                live_nb = cells[(i-1) % n][j] + cells[(i-1) % n][(j-1) % m] + cells[i][(j-1) % m] + cells[(i+1) % n][(j-1) % m] + cells[(i+1) % n][j] + cells[(i+1) % n][(j+1) % m] + cells[i][(j+1) % m] + cells[(i-1) % n][(j+1) % m] 
                if (cells[i][j] == 1 and (live_nb == 2 or live_nb == 3)) or (cells[i][j] == 0 and live_nb == 3):
                    new_cells[i][j] = 1
    elif args[0] == "lift":
        for i in range(1, n-1):
            for j in range(1, m-1):
                live_nb = cells[i-1][j] + cells[i-1][j-1] + cells[i][j-1] + cells[i+1][j-1] + cells[i+1][j] + cells[i+1][j+1] + cells[i][j+1] + cells[i-1][j+1]
                if (cells[i][j] == 1 and (live_nb == 2 or live_nb == 3)) or (cells[i][j] == 0 and live_nb == 3):
                    new_cells[i-1][j-1] = 1

    return new_cells


def string_next_gen(cells):
# transform system state to string for ASCII art
    
    conway_string = ''
    for m in range(len(cells)):
        for n in range(len(cells[m])):
            if cells[m][n] == 1:
                conway_string += '██'
            else:
                conway_string += '▒▒'
        conway_string += '\n'
    return conway_string[:-1]



def main(initial_cells, time, *args):

    clear = lambda: os.system('cls')
    columns = shutil.get_terminal_size().columns
    clear()
    cells = initial_cells
    cells_by_lines = string_next_gen(cells).split("\n")
    print('\n\n\n')
    for line in cells_by_lines:
            print(line.center(columns))
    print('\n\n\n')
    sleep(0.4)
    for t in range(time):
        cells = next_gen(cells, *args)
        clear()
        cells_by_lines = string_next_gen(cells).split("\n")
        print('\n\n\n')
        for line in cells_by_lines:
            print(line.center(columns))
        print('\n\n\n')
        sleep(0.4)

######################################
### Some options for initial cells ###
######################################        

# random_cells = np.random.randint(2, size=(35, 50)).tolist()

glider = [
           [1,0,0,0,0,0,0],
            [0,1,1,0,0,0,0],
            [1,1,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]
        ]

blinker = [
           [0,1,0],
           [0,1,0],
           [0,1,0]
       ]

pulsar = [
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
           [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
           [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
           [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],
           [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
           [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
           [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
       ]


###########################
### Some possible games ###
########################### 

# main(glider, 150, "lift", "Klein")
# main(random_cells, 200, "lift", "zeros")
# main(random_cells, 200, "factor")
main(pulsar, 20, "lift", "zeros")

