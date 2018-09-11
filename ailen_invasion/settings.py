class Settings:
    """Класс для хранения настроек игры Alien Invasion."""
    # Q = False

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана.
        self.screen_with = 600
        self.screen_height = 400
        self.bg_color = (222, 111, 88)
        self.game_name = "Alien Invasion"
        self.ship_speed = 1

    # @staticmethod
    # def quit():
    #     global Q
    #     Q = True
