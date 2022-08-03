import tcod


# properties of a wall
class Wall:
    def __init__(self, blocked):
        self.blocked = blocked

# properties of an object
class Object:
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy, map):
        # move by the given amount, as long as tile is not blocked
        if not map[self.x + dx][self.y + dy].blocked:
            self.x += dx
            self.y += dy

    def draw(self, con):
        # set the color and then draw the character that represents this object at its position
        tcod.console_set_default_foreground(con, self.color)
        tcod.console_put_char(con, self.x, self.y, self.char, tcod.BKGND_NONE)

    def clear(self, con):
        # erase the character that represents this object
        tcod.console_put_char(con, self.x, self.y, ' ', tcod.BKGND_NONE)
