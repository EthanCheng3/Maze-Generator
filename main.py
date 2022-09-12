from functions import *
from prim import *

# Console width and height in tiles
width, height = 80, 60

# Color of Wall and Ground
color_wall = tcod.Color(255, 255, 255)
color_ground = tcod.Color(0, 0, 0)

# Initialization of window
tileset = tcod.tileset.load_tilesheet("arial10x10.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

# create object representing the player
player = Object(width // 2, height // 2, ord('@'), tcod.Color(255, 255, 255))
MOVE_KEYS = {
    tcod.event.K_UP: (0, -1),
    tcod.event.K_DOWN: (0, 1),
    tcod.event.K_LEFT: (-1, 0),
    tcod.event.K_RIGHT: (1, 0),
}

# the list of objects
objects = [player]

# generate map
map = make_map(width, height)

# decides on an algorithm to use when creating maze
# map = prim_generate_maze(width, height)

# TODO: Have the map generation load with the window

# Player object is being generated, but not drawn, draw is being called (LMAO, tileset was too small, 4 1/2 hours)

# Create a window based on this console and tileset.
with tcod.context.new(
        columns=width, rows=height, tileset=tileset, title="Maze Generator", vsync=True
) as context:
    # Console
    con = tcod.Console(width, height, order="F")
    # Main loop, runs until SystemExit is raised
    while True:
        # Clears screen
        con.clear()

        # Renders everything with updated coordinates
        render_all(con, map, objects, color_wall, width, height)

        # Shows the console
        context.present(con)

        # This event loop will wait until at least one event is processed before exiting.
        for event in tcod.event.wait():
            context.convert_event(event)  # Sets tile coordinates for mouse events.
            # print(event)  # Print event names and attributes.
            match event:
                case tcod.event.KeyDown():
                    if event.sym in MOVE_KEYS:
                        x, y = MOVE_KEYS[event.sym]
                        player.move(x, y, map)
                    elif event.sym == tcod.event.K_ESCAPE:
                        raise SystemExit()
                case tcod.event.Quit():
                    raise SystemExit()
