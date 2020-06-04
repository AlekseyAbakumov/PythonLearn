# НАСЛЕДОВАНИЕ ОТ НЕСКОЛЬКИХ КЛАССОВ ПРЕДКОВ

import json


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


class ExportJSON:

    def to_json(self):
        return json.dumps({
            "name": self.name,
            "breed": self.breed
        })


# Данный класс наследует от двух классов
class ExDog(Dog, ExportJSON):
    pass


dog = ExDog("Белка", breed="Дворняжка")

print(dog.to_json())

# ЛЮБОЙ КЛАСС ЯВЛЯЕТСЯ ПОТОМКОМ object
# Проверить, является ли тот или иной объект экземпляром класса также можно
x = isinstance(dog, Pet)
print(x)

# Чтобы понять в каком порядке производится поиск атрибута в родительских
# классах, можно запросить линеаризацию класса

x = ExDog.__mro__
print(x)
