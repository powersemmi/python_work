# Alien Invasion
import pygame

from game_functions import check_events, update_screen

from settings import Settings
from ship import Ship


def run_game():
    # Инициализирует pygame, settings и объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_with, ai_settings.screen_height))
    pygame.display.set_caption(
        ai_settings.game_name
    )

    # Создание коробля
    ship = Ship(ai_settings, screen)

    # Запуск основнго цикла игры
    while True:
        check_events(ship)
        ship.update()
        update_screen(ai_settings, screen, ship)


run_game()
