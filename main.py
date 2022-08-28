from prim import *
from functions import *

# Console width and height in tiles
width, height = 80, 60

# Color of Wall and Ground
color_wall = tcod.Color(255, 255, 255)
color_ground = tcod.Color(0, 0, 0)

# Initialization of window
tileset = tcod.tileset.load_tilesheet(
        "arial10x10.png", 5, 5, tcod.tileset.CHARMAP_TCOD,
    )

con = tcod.console.Console(width, height, order="F")

# create object representing the player
player = Object(width // 2, height // 2, '@', tcod.white)

# the list of objects
objects = [player]

# generate map
map = make_map(width, height)

# decides on an algorithm to use when creating maze
map = prim_generate_maze(width, height)

# TODO: Have the map generation load with the window
# TODO: Player object is being generated, but not drawn
# Create a window based on this console and tileset.
with tcod.context.new(
        columns=con.width, rows=con.height, tileset=tileset,
) as context:
    # Main loop, runs until SystemExit is raised
    while True:
        # Clears screen
        con.clear()

        # Renders everything with updated coordinates
        render_all(con, map, objects, color_wall, width, height)

        # Erases all objects at their old locations, before they move
        for object in objects:
            object.clear(con)

        # Handles key inputs
        handle_keys(player, map)

        # Shows the console
        context.present(con)

        # This event loop will wait until at least one event is processed before exiting.
        for event in tcod.event.wait():
            context.convert_event(event)  # Sets tile coordinates for mouse events.
            # print(event)  # Print event names and attributes.
            if isinstance(event, tcod.event.Quit):
                raise SystemExit()
