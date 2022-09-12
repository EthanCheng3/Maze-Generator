# Greedy algorithm, finds a minimum spanning tree for a weighted undirected graph
import random
from properties import *


def prim_generate_maze(width, height):
    # fill map with walls
    map = [
        [Wall(True) for _ in range(height)]
        for _ in range(width)
    ]

    # create starting point
    x = random.randint(1, width - 2)
    y = random.randint(1, height - 2)
    map[x][y].blocked = False

    # list of unvisited walls around starting point
    # TODO: Implement heap to generate correctly, no weight on selection
    frontierwalls = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]
    counter = 0

    # while there are still walls in the list
    # TODO: logic is not joining passages (check corners for passage?) (or could be a data structure problem)
    while len(frontierwalls) != 0 and counter < 100000:
        # random wall to view
        rand = random.randint(0, len(frontierwalls) - 1)
        # changes current cell that is being viewed
        x = frontierwalls[rand][0]
        y = frontierwalls[rand][1]
        # if wall is border or out of index, remove from wall list
        if frontierwalls[rand][0] <= 0 or frontierwalls[rand][0] >= 79 or \
           frontierwalls[rand][1] <= 0 or frontierwalls[rand][1] >= 59:
            frontierwalls.pop(rand)
            counter += 1
        else:
            # counter for amount of passages around current cell
            passage = 0
            if not map[x + 1][y].blocked:
                passage += 1
            if not map[x - 1][y].blocked:
                passage += 1
            if not map[x][y + 1].blocked:
                passage += 1
            if not map[x][y - 1].blocked:
                passage += 1
            # if only on passage next to cell, turn current cell into passage and add nearby walls
            if passage == 1:
                map[x][y].blocked = False
                if map[x + 1][y].blocked:
                    frontierwalls.append([x + 1, y])
                if map[x - 1][y].blocked:
                    frontierwalls.append([x - 1, y])
                if map[x][y + 1].blocked:
                    frontierwalls.append([x, y + 1])
                if map[x][y - 1].blocked:
                    frontierwalls.append([x, y - 1])
            else:
                frontierwalls.pop(rand)
                counter += 1

    # Creates wall on the border of the window
    for i in range(height):
        map[0][i].blocked = True
        map[width - 1][i].blocked = True

    for i in range(width):
        map[i][0].blocked = True
        map[i][height - 1].blocked = True

    # TODO: Create start and exit (Once data structure is implemented, start at a border wall?)
    # startexit = 0
    # while startexit < 2:
    #     random.randint(0, width)
    #     random.randint(0, height)
        # if passage exists:
            # turn wall into passage
            # startexit += 1

    return map
