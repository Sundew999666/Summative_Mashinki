'''
Этот файл отвечает за самое главное в проекте - машинки
Здесь описан стандартный шаблон машины, а также два их вида - с неадекватным и адекватным водителем
'''

from maze import Maze
from maze.directions import directions
from maze.tiles import Wall_tile, Room_tile
from ui import graphics
from random import choice
import settings

EPS = 0.1  # некоторый возможный разброс для колллизий


class Car:
    def __init__(self, x, y, num, dir=0):
        '''
        x, y - координаты машинки
        size - размер машинки, относительно тайла
        speed - скорость машинки в тайлах
        num - "имя" машинки(её номер от рождения)
        dir - направление движения машинки
        broken - состояние - сломана ли машина
        '''
        self.x, self.y = int(x) + 0.2, int(y) + 0.2
        self.size = 1 / 15
        self.speed = 1
        self.num = num
        self.dir = dir
        self.broken = False

    def draw(self):
        # Отрисовка машины
        graphics.draw_circle("yellow", self.x, self.y, self.size)

    def update(self, delta_time):
        # Обновление машины
        pass


# немного интеллекта
class StupidCar(Car):
    def __init__(self, x, y, num, dir=0):
        super().__init__(x, y, num, dir)

    def draw(self):
        '''
        Отрисовка машинки
        '''
        graphics.draw_circle("red", self.x, self.y, self.size)

    def check(self, mouses):
        '''
        Проверка на то, что мы не встретились с другой машиной. Если так - ставим состояние "сломан" себе и ей
        '''
        for i in range(len(mouses)):
            if self.num != mouses[i].num and (abs(self.x - mouses[i].x) <= EPS and abs(self.y - mouses[i].y) <= EPS):
                self.broken = True
                return mouses[i]
        return None

    def update(self, delta_time):
        '''
        Обновление движения машинки
        '''
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
                    elif cur_tile.sides == 3 and cur_tile.turn == "up" and cur_tile.dist_to_border(self.x, self.y,
                                                                                                   0) > 0.75:
                        self.dir = (self.dir + 1) % 4
                    elif cur_tile.sides == 3 and cur_tile.turn == "down" and cur_tile.dist_to_border(self.x, self.y,
                                                                                                     0) < 0.75:
                        self.dir = (self.dir + 1) % 4
                    else:
                        self.dir = (self.dir - 1) % 4
            sp = choice([1, 0, -1, 0, 0, 1])
            if self.speed > 0.2 and self.speed < 3:
                self.speed += sp * 0.05
            elif self.speed < 0.2:
                self.speed += 0.05
            else:
                self.speed -= 0.05
        else:
            pass


class SmartCar(Car):
    def __init__(self, x, y, num, dir=0):
        super().__init__(x, y, num, dir)

    def draw(self):
        '''
        Отрисовка машинки
        '''
        graphics.draw_circle("green", self.x, self.y, self.size)

    def check(self, mouses):
        '''
        Проверка на то, что мы не пересеклись с другой машинкой
        '''
        for i in range(len(mouses)):
            if self.num != mouses[i].num and (abs(self.x - mouses[i].x) <= EPS and abs(self.y - mouses[i].y) <= EPS):
                self.broken = True
                return mouses[i]
        return None

    def update(self, delta_time):
        '''
        Обновление движения машинки
        '''
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
                    elif cur_tile.sides == 3 and cur_tile.turn == "up" and cur_tile.dist_to_border(self.x, self.y,
                                                                                                   0) > 0.75:
                        self.dir = (self.dir + 1) % 4
                    elif cur_tile.sides == 3 and cur_tile.turn == "down" and cur_tile.dist_to_border(self.x, self.y,
                                                                                                     0) < 0.75:
                        self.dir = (self.dir + 1) % 4
                    else:
                        self.dir = (self.dir - 1) % 4
            if isinstance(next_tile, Room_tile) and next_tile.sides == 2 and next_tile.turn in ['rightnleft',
                                                                                                'upndown'] and self.speed < 2:
                self.speed += 0.025
            elif isinstance(next_tile, Room_tile) and next_tile.sides == 2 and next_tile.turn not in ['rightnleft',
                                                                                                      'upndown'] and self.speed > 0.75:
                self.speed -= 0.05
            if cur_tile.turn not in ['rightnleft', 'upndown']:
                cur_tile_dtd = cur_tile.dist_to_border(self.x, self.y, 3)
                cur_tile_dtr = cur_tile.dist_to_border(self.x, self.y, 0)
                if cur_tile.turn == "leftndown":
                    if 0.17 < cur_tile_dtd < 0.22 and 0.82 > cur_tile_dtr > 0.74:
                        if self.dir == 0:
                            self.dir = (self.dir - 1) % 4
                        elif self.dir == 1:
                            self.dir = (self.dir + 1) % 4
                if cur_tile.turn == "leftnup":
                    if 0.82 > cur_tile_dtd > 0.74 and 0.82 > cur_tile_dtr > 0.74:
                        if self.dir == 0:
                            self.dir = (self.dir + 1) % 4
                        elif self.dir == 3:
                            self.dir = (self.dir - 1) % 4
                if cur_tile.turn == "rightndown":
                    if 0.17 < cur_tile_dtd < 0.22 and 0.18 < cur_tile_dtr < 0.22:
                        if self.dir == 2:
                            self.dir = (self.dir + 1) % 4
                        elif self.dir == 1:
                            self.dir = (self.dir - 1) % 4
                if cur_tile.turn == "rightnup":
                    if 0.17 < cur_tile_dtr < 0.22 and 0.82 > cur_tile_dtd > 0.74:
                        if self.dir == 2:
                            self.dir = (self.dir - 1) % 4
                        elif self.dir == 3:
                            self.dir = (self.dir + 1) % 4
        else:
            pass
