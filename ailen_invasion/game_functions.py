# game_functions.py

from sys import exit
from os import system
import settings

import pygame


def check_keydown_event(event, ship):
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_q:
        exit()
        settings.Q = True


def check_keyup_event(event, ship):
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False


def check_events(ship):
    """Обрабатывает нажатия и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            system('python start.py')
            exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def update_screen(ai_settings, screen, ship):
    # При каждом проходе цикла перерисовывается экран
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Отображение последнего прорисованного экрана
    pygame.display.flip()
