import settings
from maze.mice import StupidCar, SmartCar
from maze.tiles import Room_tile, Wall_tile


maze = []
stupidcar = []
smartcar = []
##########################################################
# Грузим карту
with open(settings.map_file) as f:
    map_txt = f.readlines()

# Строим карту из настоящих объектных тайлов
for row, line in enumerate(map_txt):
    maze.append([])
    for column, tile_type in enumerate(line[:-1]):
        fup, fdown, fleft, fright = 0, 0, 0, 0
        if tile_type == "0":
            if map_txt[row-1][column] == '1':
                fup = 1
            if map_txt[row+1][column] == '1':
                fdown = 1
            if map_txt[row][column-1] == '1':
                fleft = 1
            if map_txt[row][column+1] == '1':
                fright = 1
            s = fup+fdown+fleft+fright
            if s == 2:
                if fup == 0:
                    if fleft == 0:
                        maze[row].append(Room_tile(row, column, 2, 'leftnup'))
                    elif fright == 0:
                        maze[row].append(Room_tile(row, column, 2, 'rightnup'))
                    else:
                        maze[row].append(Room_tile(row, column, 2, 'upndown'))
                elif fdown == 0:
                    if fleft == 0:
                        maze[row].append(Room_tile(row, column, 2, 'leftndown'))
                    elif fright == 0:
                        maze[row].append(Room_tile(row, column, 2, 'rightndown'))
                    else:
                        maze[row].append(Room_tile(row, column, 2, 'upndown'))
                else:
                    maze[row].append(Room_tile(row, column, 2, 'rightnleft'))
            elif s == 3:
                if fup == 0:
                    maze[row].append(Room_tile(row, column, 3, 'up'))
                elif fdown == 0:
                    maze[row].append(Room_tile(row, column, 3, 'down'))
                elif fleft == 0:
                    maze[row].append(Room_tile(row, column, 3, 'left'))
                else:
                    maze[row].append(Room_tile(row, column, 3, 'right'))
            else:
                if fup == 1:
                    maze[row].append(Room_tile(row, column, 1, 'up'))
                elif fdown == 1:
                    maze[row].append(Room_tile(row, column, 1, 'down'))
                elif fleft == 1:
                    maze[row].append(Room_tile(row, column, 1, 'left'))
                else:
                    maze[row].append(Room_tile(row, column, 1, 'right'))
        else:
            maze[row].append(Wall_tile(row, column))
###########################################################


# Рисуем все: и тайлы и мышей
def draw():
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            maze[row][column].draw()
    if len(stupidcar) > 0:
        for each in stupidcar:
            each.draw()


# Получаем тайл по координатам лабиринта
def get_tile(x, y):
    if 0 <= y < len(maze) and 0 <= x < len(maze[int(y)]):
        tile_column, tile_row = int(x), int(y)
        return maze[tile_row][tile_column]
    else:
        return None


# двигаем, все что движется
# вызов этой функции постоянно в цикле в main.py
def update(delta_time):
    if len(stupidcar) > 0:
        for each in stupidcar:
            each.update(delta_time)
            m1 = each.check(stupidcar)
            if m1 is not None:
                m1.broken = True

def clearbroken():
    eachst, eachsm = 0, 0
    while eachst != len(stupidcar):
        if stupidcar[eachst].broken:
            stupidcar.pop(eachst)
        else:
            eachst += 1
    while eachsm != len(smartcar):
        if smartcar[eachsm].broken:
            smartcar.pop(eachsm)
        else:
            eachsm += 1

def add_stupidcar(x, y, it):
    global stupidcar
    stupidcar.append(StupidCar(x, y, it))

def add_smartcar(x, y, it):
    global smartcar
    stupidcar.append(SmartCar(x, y, it))