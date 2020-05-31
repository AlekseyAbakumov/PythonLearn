# классы


class Human:
    pass


class Robot:
    """Данный класс позволяет создавать роботов"""


class Planet:
    """Классы Планета"""

    def __init__(self, name):
        self.name = name

    # этот метод не обязательный. Он говорит о том, что если идет обращение
    # к экземпляру класса, без указания атрибу, то, чтобы возвращал указанны
    # атрибут. В данном случае имя класса
    def __str__(self):
        return self.name


earth = Planet("Earth")
print(earth.name)
print(earth)
