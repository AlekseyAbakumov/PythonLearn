# МЕТОДЫ ЭКЗЕМПЛЯРА


class Human:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age


class Planet:

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []

    # метод, который добавляем на планету людей
    def add_human(self, human):
        print(f"Welcome to {self.name},{human.name}")
        self.population.append(human)


mars = Planet("Mars")
print(mars.population)
bob = Human("Bob")
mars.add_human(bob)
print(mars.population)