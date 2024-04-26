'''
Файл, ответственный за само существование тайла на поле и его свойствах - количество соединённых свободных тайлов,
тип тайла, его состояние и его картинка
'''

from maze import Maze
from maze.directions import directions
from ui import graphics

'''
Базовый класс, к нему ссылаютсят его "дет"
'''


class Tile:
    def __init__(self, tile_type, row, column):
        '''
        tile_type - тип тайла, либо "стена"(1) либо "проход"(0)
        row - ряд тайла в общей системе
        column - столбец ряда в общей системе
        '''
        self.tile_type = tile_type
        self.row = row
        self.column = column

    def draw(self):
        pass

    def get_neighb_tile(self, dir_n):
        # Находит следующий тайл, после того, на котором мы стоим в направлении, переданном через dir_n
        dx, dy = directions[dir_n]
        return Maze.get_tile(self.column + 0.5 + dx, self.row + 0.5 + dy)

    def dist_to_border(self, x, y, dir_n):
        # Находит расстояние до конца тайла в сторону, которая передана через dir_n от координат (x, y)
        x -= int(x)
        y -= int(y)
        if dir_n == 0:
            return 1 - x
        elif dir_n == 1:
            return y
        elif dir_n == 2:
            return x
        return 1 - y


'''
Ссылается на класс "Tile". Отвечает за существование клетки с пустым пространством, которая в подсчётах считается
стеной
'''


class Wall_tile(Tile):
    def __init__(self, row, column):
        super().__init__("1", row, column)

    def draw(self):
        pass


'''
Ссылается на класс "Tile". Отвечает за клетки с дорогами и также за то, что видит игрок и то, насколько всё красиво
'''


class Room_tile(Tile):
    def __init__(self, row, column, sides, turn):
        '''
        sides - вид клетки прохода - из неё 1, 2 или 3 выхода
        turn - куда повёрнута клетка - в формате строки вида left, right и т.п.
        '''
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
        '''
        Отрисовка тайла
        '''
        graphics.draw_image(self.image, self.column, self.row)
