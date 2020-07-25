# применяем паттерн ДЕКОРАТОР

# описываем животных, которые живут в нашей игре
# чтобы не описывать каждый вид, применим паттерн декоратор
from abc import ABC, abstractmethod


class Creature(ABC):

    # принимать пищу
    @abstractmethod
    def feed(self):
        pass

    # двигаться
    @abstractmethod
    def move(self):
        pass

    # издавать звук
    @abstractmethod
    def make_noise(self):
        pass


class Animal(Creature):

    def feed(self):
        print("Я ем траву")

    def move(self):
        print("Я гуляю")

    def make_noise(self):
        print("Ууууууу!")


# создаем абстрактный декоратор
class AbstractDecorator(Creature):

    def __init__(self, base):
        self.base = base

    def move(self):
        self.base.move()

    def feed(self):
        self.base.feed()

    def make_noise(self):
        self.base.make_noise()


# создаем класс водоплавающих
class Swimming(AbstractDecorator):

    # переопределяем метод, т.к. животное не ходит а плавает
    def move(self):
        print("Я плаваю")

    # переопределяем метод, т.к. водоплавающие не издают звуков
    def make_noise(self):
        print("Я не разговариваю")


# создаем класс Хищников
class Predator(AbstractDecorator):

    # переопределяем метод приема пищи. Хищник не др. животных, а не траву
    def feed(self):
        print("Я ем других животных")


# Создаем класс "быстрых" животных
class Fast(AbstractDecorator):

    def move(self):
        self.base.move()
        print("Быстро")


print("ПРОСТО ЖИВОТНОЕ")
# Создаем объект животное. Просто ЖИВОТНОЕ
animal = Animal()
animal.move()
animal.feed()
animal.make_noise()

print("")
# Создаем рыбу,
# Она принадлежит классу водоплавающее, и наследуюется от объекта животное
print("РЫБА")

fish = Swimming(animal)
fish.move()
fish.feed()
fish.make_noise()

print("")

# Создаем Акулу
# Она принадлежит классу хищник и наследуется от объекта Рыба
print("АКУЛА")

shark = Predator(fish)
shark.move()
shark.feed()
shark.make_noise()

print("")

# Создаем Гепарда, который принадлежит классу "Быстрых" и наследуется от
# объекта акула
print("ГЕПАРД")
gepard = Fast(shark)
gepard.move()  # в данном случае он приобретет и метод от акулы + свой декоратор
gepard.feed()
gepard.make_noise()

print("")

# создаем супер Гепарда
print("СУПЕР ГЕПАРД")
superGepard = Fast(gepard)
superGepard.move()
superGepard.feed()
superGepard.make_noise()

print("")
# отнимем статус хищника у Гепарда
# Уберем у него декоратор
# На этапе, когда мы делали Водоплавающих, мы еще не обзывали их хищниками
# Эти свойства можно увидеть
print(superGepard.base)
print(superGepard.base.base)
print(superGepard.base.base.base)

print("")

# отнимаем статус хищника
print("Супер гепард теперь супер быстрый, но больше не хищник и ест траву")
superGepard.base.base = superGepard.base.base.base
superGepard.move()
superGepard.feed()
superGepard.make_noise()
