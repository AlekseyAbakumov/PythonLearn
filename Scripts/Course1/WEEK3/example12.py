# НАСЛЕДОВАНИЕ


class Pet:
    """Основной класс Питомец. РОДИТЕЛЬСКИЙ класс"""

    def __init__(self, name=None):
        self.name = name


class Dog(Pet):
    """Класс Собака. НАСЛЕДУЮЕМЫЙ класс"""

    def __init__(self, name, breed=None):
        super().__init__(name)
        # Порода
        self.breed = breed

    # Метод подачи голоса
    def say(self):
        return "{0}: waw".format(self.name)

Topic=Dog("Топик","Доберман")
print(Topic.name, Topic.breed)
print(Topic.say())
