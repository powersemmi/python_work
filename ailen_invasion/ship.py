import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        """Инициализирует карабль и задаёт его начальную позицую."""
        self.moving_right = False
        self.moving_left = False
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения коробдя и его прогрузка.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Каждый новый корабль появляеться в нижнем краю экраеа.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def update(self):
        """Обновляет позицию корабля с учётом флагов."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed

    def blitme(self):
        """Рисует карабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
