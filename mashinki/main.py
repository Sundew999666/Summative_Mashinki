'''
Основной файл симуляции. Именно его надо запускать и он отвечает за работу всего кода.
'''

import settings
from maze import Maze
from ui import events
from ui import graphics

running = True
clock = events.Clock()
num = 0
dir = 0
while running:
    for event in events.get_event_queue():
        if event.type == events.QUIT:
            running = False
        if event.type == events.MOUSEBUTTONDOWN:
            if event.button == 1:
                Maze.add_stupidcar(
                    event.pos[0] / settings.tile_size[0] - settings.view_left_top[0] / settings.tile_size[0],
                    event.pos[1] / settings.tile_size[1] - settings.view_left_top[1] / settings.tile_size[1], num, dir)
                num += 1
            if event.button == 3:
                Maze.add_smartcar(
                    event.pos[0] / settings.tile_size[0] - settings.view_left_top[0] / settings.tile_size[0],
                    event.pos[1] / settings.tile_size[1] - settings.view_left_top[1] / settings.tile_size[1], num, dir)
                num += 1
        if event.type == events.KEYDOWN:
            if event.key == events.K_SPACE:
                Maze.clearbroken()
            if event.key == events.K_RIGHT:
                dir = 0
            if event.key == events.K_LEFT:
                dir = 2
            if event.key == events.K_DOWN:
                dir = 3
            if event.key == events.K_UP:
                dir = 1
    # отрисовка
    graphics.fill("black")
    Maze.draw()
    graphics.flip()
    clock.tick(settings.FPS)
    # обновление
    Maze.update(1 / settings.FPS)
