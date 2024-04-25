import maze.Maze
from maze import Maze
from maze.directions import directions
from ui import graphics


class Tile:
    def __init__(self, tile_type, row, column):
        self.tile_type = tile_type
        self.row = row
        self.column = column

    def draw(self):
       pass

    def get_neighb_tile(self, dir_n ):
        dx, dy = directions[dir_n]
        return Maze.get_tile(self.column + 0.5 + dx, self.row + 0.5 + dy)

    def dist_to_border(self, x, y, dir_n):
        x -= int(x)
        y -= int(y)
        if dir_n == 0:
            return 1 - x
        elif dir_n == 1:
            return y
        elif dir_n == 2:
            return x
        return 1 - y


class Wall_tile(Tile):
    def __init__(self, row, column):
        super().__init__("1", row, column)

    def draw(self):
        pass


class Room_tile(Tile):
    def __init__(self, row, column, sides, turn):
        super().__init__("0", row, column)
        self.sides = sides
        self.turn = turn
        if sides == 3:
            if turn == 'up':
                self.image = graphics.load_image("images/road3sidesupfree.png")
            elif turn == 'down':
                self.image = graphics.load_image("images/road3sidesdownfree.png")
            elif turn == 'left':
                self.image = graphics.load_image("images/road3sidesleftfree.png")
            else:
                self.image = graphics.load_image("images/road3sidesrightfree.png")
        elif sides == 2:
            if turn == 'leftndown':
                self.image = graphics.load_image("images/road2sidesleftndownfree.png")
            elif turn == 'leftnup':
                self.image = graphics.load_image("images/road2sidesleftnupfree.png")
            elif turn == 'rightndown':
                self.image = graphics.load_image("images/road2sidesrightndownfree.png")
            elif turn == 'rightnleft':
                self.image = graphics.load_image("images/road2sidesrightnleftfree.png")
            elif turn == 'rightnup':
                self.image = graphics.load_image("images/road2sidesrightnupfree.png")
            else:
                self.image = graphics.load_image("images/road2sidesupndownfree.png")
        else:
            if turn == 'up':
                self.image = graphics.load_image("images/road1sidesupblock.png")
            elif turn == 'down':
                self.image = graphics.load_image("images/road1sidesdownblock.png")
            elif turn == 'left':
                self.image = graphics.load_image("images/road1sidesleftblock.png")
            else:
                self.image = graphics.load_image("images/road1sidesrightblock.png")

    def draw(self):
        graphics.draw_image(self.image, self.column, self.row)
