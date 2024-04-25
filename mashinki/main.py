import settings
from maze import Maze
from ui import events
from ui import graphics

FPS = 60
running = True
clock = events.Clock()
it = 0
while running:
    for event in events.get_event_queue():
        if event.type == events.QUIT:
           running = False
        if event.type == events.MOUSEBUTTONDOWN:
            if event.button == 1:
                Maze.add_stupidcar(event.pos[0]/settings.tile_size[0]-settings.view_left_top[0]/settings.tile_size[0], event.pos[1]/settings.tile_size[1]-settings.view_left_top[1]/settings.tile_size[1], it)
                it += 1
            if event.button == 3:
                Maze.add_smartcar(event.pos[0]/settings.tile_size[0]-settings.view_left_top[0]/settings.tile_size[0], event.pos[1]/settings.tile_size[1]-settings.view_left_top[1]/settings.tile_size[1], it)
                it += 1
        if event.type == events.KEYDOWN:
            if event.key == events.K_SPACE:
                Maze.clearbroken()

    graphics.fill("black")
    # рисуем лабиринт
    Maze.draw()
    graphics.flip()
    clock.tick(FPS)
    # обновляем весь лабиринт
    Maze.update(1 / FPS)
