# создание абстрактного класса
# мы хотим создать абстрактный класс. В котором есть описание, но нет
# реализации метода

from abc import ABC, abstractmethod


# Как бы мы делали наследуюемый класс по умолчанию

class A:

    def do_something(self):
        print("Hi")


# в этом случае метод do_something будет унаследован и его можно использовать
a = A()
a.do_something()


# создадим абстрактный класс
# мы определяем класса наследуемым от стандартной библиотеки ABC
class B(ABC):
    @abstractmethod
    def do_something(self):
        print("Hi")


# b = B()  # при попытке создать объект абстрактного класса, выдасться ошибка

# пишем реализацию метода абстрактного класса

class C(B):
    def do_something(self):
        print("Hello")


b = C()
b.do_something()
