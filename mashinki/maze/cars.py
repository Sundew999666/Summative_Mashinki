from maze import Maze
from maze.directions import directions
from maze.tiles import Wall_tile, Room_tile
from ui import graphics
from random import choice
import settings

EPS = 0.1

class Car:
    def __init__(self, x, y, dir = 0):
        self.x, self.y = x, y
        self.size = 1 / 15 # доля тайла, тайлы 1x1
        self.speed = 1 # тайлов в секунду
        self.dir = dir
        self.broken = False

    def draw(self):
        graphics.draw_circle("yellow", self.x, self.y, self.size)

    def update(self, delta_time):
        # Ничего не умеет вообще
        pass


# немного интеллекта
class StupidCar(Car):
    def __init__(self, x, y, it, dir=0):
        super().__init__(x, y, dir)
        self.x, self.y = int(x)+0.2, int(y)+0.2
        self.size = 1 / 15  # доля тайла, тайлы 1x1
        self.speed = 1  # тайлов в секунду
        self.dir = dir
        self.it = it

    def draw(self):
        graphics.draw_circle("red", self.x, self.y, self.size)

    def check(self, mouses):
        for i in range(len(mouses)):
            if self.it != mouses[i].it and (abs(self.x-mouses[i].x) <= EPS and abs(self.y-mouses[i].y) <= EPS):
                self.broken = True
                return mouses[i]
        return None


    def update(self, delta_time):
        if not self.broken:
            f1, f2 = 0, 0
            cur_tile = Maze.get_tile(self.x, self.y)
            dx, dy = directions[self.dir]
            self.x += dx * self.speed * delta_time
            self.y += dy * self.speed * delta_time
            next_tile = cur_tile.get_neighb_tile(self.dir)
            if cur_tile.dist_to_border(self.x, self.y, self.dir) < 0.2 and (
                    next_tile is None or isinstance(next_tile, Wall_tile)):
                if isinstance(cur_tile.get_neighb_tile((self.dir - 1) % 4), Room_tile):
                    f1 = 1
                if isinstance(cur_tile.get_neighb_tile((self.dir + 1) % 4), Room_tile):
                    f2 = 1
                print(f1, f2)
                if f1 == 1:
                    if f2 == 1:
                        d = choice([-1, 1])
                        self.dir = (self.dir + d) % 4
                    else:
                        self.dir = (self.dir - 1) % 4
                elif f2 == 1:
                    self.dir = (self.dir + 1) % 4
                else:
                    if cur_tile.sides == 3 and cur_tile.turn == "right" and cur_tile.dist_to_border(self.x, self.y, 3) > 0.25:
                        self.dir = (self.dir + 1) % 4
                    elif cur_tile.sides == 3 and cur_tile.turn == "left" and cur_tile.dist_to_border(self.x, self.y, 3) < 0.25:
                        self.dir = (self.dir + 1) % 4
                    else:
                        self.dir = (self.dir - 1) % 4
            sp = choice([1, 0, -1, 0, 0, 1])
            if self.speed > 0.2 and self.speed < 3:
                self.speed += sp*0.05
            elif self.speed < 0.2:
                self.speed += 0.05
            else:
                self.speed -= 0.05
        else:
            pass

class SmartCar(Car):
    def __init__(self, x, y, it, dir=0):
        super().__init__(x, y, dir)
        self.x, self.y = int(x)+0.2, int(y)+0.2
        self.size = 1 / 15  # доля тайла, тайлы 1x1
        self.speed = 1  # тайлов в секунду
        self.dir = dir
        self.it = it

    def draw(self):
        graphics.draw_circle("green", self.x, self.y, self.size)

    def check(self, mouses):
        for i in range(len(mouses)):
            if self.it != mouses[i].it and (abs(self.x-mouses[i].x) <= EPS and abs(self.y-mouses[i].y) <= EPS):
                self.broken = True
                return mouses[i]
        return None


    def update(self, delta_time):
        if not self.broken:
            f1, f2 = 0, 0
            cur_tile = Maze.get_tile(self.x, self.y)
            dx, dy = directions[self.dir]
            self.x += dx * self.speed * delta_time
            self.y += dy * self.speed * delta_time
            next_tile = cur_tile.get_neighb_tile(self.dir)
            if cur_tile.dist_to_border(self.x, self.y, self.dir) < 0.2 and (
                    next_tile is None or isinstance(next_tile, Wall_tile)):
                if isinstance(cur_tile.get_neighb_tile((self.dir - 1) % 4), Room_tile):
                    f1 = 1
                if isinstance(cur_tile.get_neighb_tile((self.dir + 1) % 4), Room_tile):
                    f2 = 1
                if f1 == 1:
                    if f2 == 1:
                        d = choice([-1, 1])
                        self.dir = (self.dir + d) % 4
                    else:
                        self.dir = (self.dir - 1) % 4
                elif f2 == 1:
                    self.dir = (self.dir + 1) % 4
                else:
                    if cur_tile.sides == 3 and cur_tile.turn == "right" and cur_tile.dist_to_border(self.x, self.y,
                                                                                                    3) > 0.25:
                        self.dir = (self.dir + 1) % 4
                    elif cur_tile.sides == 3 and cur_tile.turn == "left" and cur_tile.dist_to_border(self.x, self.y,
                                                                                                     3) < 0.25:
                        self.dir = (self.dir + 1) % 4
                    else:
                        self.dir = (self.dir - 1) % 4
            if isinstance(next_tile, Room_tile) and next_tile.sides == 2 and next_tile.turn in ['rightnleft', 'upndown'] and self.speed < 3:
                self.speed += 0.025
            elif isinstance(next_tile, Room_tile) and next_tile.sides == 2 and next_tile.turn not in ['rightnleft', 'upndown'] and self.speed > 0.5:
                self.speed -= 0.05
        else:
            pass



