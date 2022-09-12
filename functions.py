from properties import *


# Creates Map with no Walls
def make_map(width, height):
    # fill map with "unblocked" tiles
    map = [
        [Wall(False) for _ in range(height)]
        for _ in range(width)
    ]

    # Creates wall on the border of the window
    for i in range(height):
        map[0][i].blocked = True
        map[width - 1][i].blocked = True

    for i in range(width):
        map[i][0].blocked = True
        map[i][height - 1].blocked = True

    return map


# function to erase map
def erase_map(con, width, height):
    for y in range(height):
        for x in range(width):
            tcod.console_put_char_ex(con, x, y, ' ', tcod.white, tcod.black)


def render_all(con, map, objects, color_wall, width, height):
    # go through all tiles, and set their background color
    for y in range(height):
        for x in range(width):
            wall = map[x][y].blocked
            if wall:
                tcod.console_set_char_background(con, x, y, color_wall, tcod.BKGND_SET)

    for object in objects:
        object.draw(con)

    return map
