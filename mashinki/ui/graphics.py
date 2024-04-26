'''
Файл, в котором собрано удобное управление всей отрисовкой в симуляции
'''

import pygame
import settings
from ui import screen

Image = pygame.Surface
flip = pygame.display.flip
pygame.display.set_caption('Criminal in Country')


def fill(color):
    screen.fill(color)


# отображение картинки и её форматирование
def load_image(path, size=(1, 1)):
    img = pygame.image.load(path)
    return pygame.transform.scale(img, (size[0] * settings.tile_size[0], size[1] * settings.tile_size[1]))


# отрисовка изображения
def draw_image(image, x, y):
    screen.blit(image, (
    x * settings.tile_size[0] + settings.view_left_top[0], y * settings.tile_size[1] + settings.view_left_top[1]))
    pass


# отрисовка машинок
def draw_circle(color, x, y, r):
    pygame.draw.circle(screen, color, (
    x * settings.tile_size[0] + settings.view_left_top[0], y * settings.tile_size[1] + settings.view_left_top[1]),
                       r * settings.tile_size[0])
    pass
