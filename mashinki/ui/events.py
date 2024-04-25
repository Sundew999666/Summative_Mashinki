'''
Здесь находиться файл с настройками событий во время цикла. События - кнопки, нажатые во время действия симуляции
Всё, для чего служит этот файл - более удобный доступ к функциям Pygame.event
'''

import pygame.event

Clock = pygame.time.Clock

Event = pygame.event.EventType
get_event_queue = pygame.event.get

QUIT = pygame.QUIT
MOUSEBUTTONDOWN = pygame.MOUSEBUTTONDOWN
MOUSEBUTTONUP = pygame.MOUSEBUTTONUP
MOUSEMOTION = pygame.MOUSEMOTION
MOUSEWHEEL = pygame.MOUSEWHEEL
KEYDOWN = pygame.KEYDOWN
K_SPACE = pygame.K_SPACE
K_RIGHT = pygame.K_RIGHT
K_UP = pygame.K_UP
K_DOWN = pygame.K_DOWN
K_LEFT = pygame.K_LEFT