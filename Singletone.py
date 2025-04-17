class GameSettings:
    """
    Класс игрового синглтона, хранящий общие игровые настройки.
    """
    __instance = None  # Хранит ссылку на единственный экземпляр класса

    def __new__(cls):
        """
        Переопределенный конструктор, обеспечивающий существование только одного экземпляра.
        """
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            # Можно сразу инициализировать некоторые базовые настройки
            cls.__instance.volume = 50
            cls.__instance.difficulty = "Medium"
        return cls.__instance

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, new_volume):
        self._volume = new_volume

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, new_difficulty):
        self._difficulty = new_difficulty


# Тестируем нашу реализацию
if __name__ == "__main__":
    # Обращаемся к игровому Singleton дважды
    settings1 = GameSettings()
    settings2 = GameSettings()

    # Проверяем, что оба экземпляра ссылаются на один и тот же объект
    print(settings1 is settings2)  # Вернет True

    # Устанавливаем громкость и сложность в одном месте
    settings1.volume = 70
    settings1.difficulty = "Hard"

    # Эти изменения видны также и в другом обращении к объекту
    print(settings2.volume)       # Выведет 70
    print(settings2.difficulty)  # Выведет Hard