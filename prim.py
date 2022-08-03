# Greedy algorithm, finds a minimum spanning tree for a weighted undirected graph
import random
from properties import *

def add_neighbors(x, y, WIDTH, HEIGHT):

    # add the top wall to list
    if map[x][y - 1].blocked and y != 0:
        frontierwalls

    # add the bottom wall to list
    if map[x][y + 1].blocked and y != HEIGHT - 1:
        frontierwalls

    # add the left wall to list
    if map[x - 1][y].blocked and x != 0:
        frontierwalls

    # add the right wall to list
    if map[x + 1][y].blocked and x != WIDTH - 1:
        frontierwalls

def prim_generate_maze(map, WIDTH, HEIGHT):
    # fill map with walls
    map = [
        [Wall(True) for i in range(HEIGHT)]
        for i in range(WIDTH)
    ]


    # create starting point
    x = random.randint(2, WIDTH - 3)
    y = random.randint(2, HEIGHT - 3)
    map[x][y].blocked = False

    # list of unvisited walls
    frontierwalls = []
    frontierwalls.add_neighbors(x, y, WIDTH, HEIGHT)

    while len(frontierwalls) > 0:




        break

    return map
