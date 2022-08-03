from prim import *
from properties import *
import tcod


# Console width and height in tiles
WIDTH, HEIGHT = 80, 60  

# Maximum Number of Frames
LIMIT_FPS = 20

# Color of Wall and Ground
color_wall = tcod.Color(255, 255, 255)
color_ground = tcod.Color(0, 0, 0)


# Creates Map with no Walls
def make_map():

    # fill map with "unblocked" tiles
    map = [
        [Wall(False) for i in range(HEIGHT)]
        for i in range(WIDTH)
    ]

    # creates walls on the border of the window
    for i in range(HEIGHT):
        map[0][i].blocked = True
        map[WIDTH - 1][i].blocked = True

    for i in range(WIDTH):
        map[i][0].blocked = True
        map[i][HEIGHT - 1].blocked = True

    return map


# function to erase map
def erase_map(con):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            tcod.console_put_char_ex(con, x, y, ' ', tcod.white, tcod.black)


def render_all(map):
    # go through all tiles, and set their background color
    for y in range(HEIGHT):
        for x in range(WIDTH):
            wall = map[x][y].blocked
            if wall:
                tcod.console_set_char_background(con, x, y, color_wall, tcod.BKGND_SET)

    # draw all objects in the list
    for object in objects:
        object.draw(con)

    # blit the contents of "con" to the root console
    tcod.console_blit(con, 0, 0, WIDTH, HEIGHT, 0, 0, 0)


# handles user input
def handle_keys():
    key = tcod.console_check_for_keypress()

    if key.vk == tcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle fullscreen
        tcod.console_set_fullscreen(not tcod.console_is_fullscreen())
    elif key.vk == tcod.KEY_ESCAPE:
        # Escape: exit game
        return True

    # movement keys
    if tcod.console_is_key_pressed(tcod.KEY_UP):
        player.move(0, -1, map)

    elif tcod.console_is_key_pressed(tcod.KEY_DOWN):
        player.move(0, 1, map)

    elif tcod.console_is_key_pressed(tcod.KEY_LEFT):
        player.move(-1, 0, map)

    elif tcod.console_is_key_pressed(tcod.KEY_RIGHT):
        player.move(1, 0, map)


# Initialization of window
tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
tcod.console_init_root(WIDTH, HEIGHT, 'Maze-Generator', False)
tcod.sys_set_fps(LIMIT_FPS)
con = tcod.console_new(WIDTH, HEIGHT)

# create object representing the player
player = Object(WIDTH // 2, HEIGHT // 2, '@', tcod.white)

# the list of objects
objects = [player]

# generate map
map = make_map()

# decides on an algorithm to use when creating maze
map = prim_generate_maze(map, WIDTH, HEIGHT)

while not tcod.console_is_window_closed():

    # render the screen
    render_all(map)

    tcod.console_flush()

    # erase all objects at their old locations, before they move
    for object in objects:
        object.clear(con)

    # handle keys and exit game if needed
    exit = handle_keys()
    if exit:
        break
