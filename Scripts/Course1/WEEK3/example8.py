# Вызов методов из методов


class Human:
    def __init__(self, name, age=0):
        # Общепринятое соглашение. Если атрибут начинается с нижнего
        # подчеркивания, значит пользоваться им не рекомендуется. Программист
        # написал их для себя
        self._name = name
        self._age = age

    def _say(self, text):
        print(text)

    def say_name(self):
        self._say(f"Hello, I am {self._name}")

    def say_how_old(self):
        self._say(f"I am {self._age} years old")


bob = Human("Bob", age=29)
bob.say_name()
bob.say_how_old()
