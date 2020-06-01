# Вычисляемые свойства класса. PROPERTY


class Robot:

    # при инициализации задаем атрибут. Мощность робота
    def __init__(self, power):
        self.power = power


# Создаем экземпляр класса
Topic = Robot(100)
# Изменяем мощность робота
Topic.power = 200


# Предположим, что кто то пользуется нашим классом. И иногда ставит не валидное
# значение. Например мощность не может быть отрицательной. В этом случае
# мы хотим, чтобы она ОБНУЛЯЛАСЬ

# Создадим новый


class Robot2:

    def __init__(self, power):
        self._power = power

    # power является объектом property. Это встроенный объект. Импорт не нужен
    power = property()

    @power.setter  # Метод для изменения атрибуты
    def power(self, value):
        if value < 0:
            self._power = 0
        else:
            self._power = value

    @power.getter  # Метод для чтения атрибута
    def power(self):
        return self._power

    @power.deleter  # Метод для удаления атрибута
    def power(self):
        print("make robot useless")
        del self._power


# Объявляем. Все ОК
Topic = Robot2(100)
print(Topic.power)

# Изменяем на др положительное значение. Все ОК
Topic.power = 50
print(Topic.power)

# Изменяем на отрицательное значение. WARNING. Значение обнулится
Topic.power = -10
print(Topic.power)


# Если же нам просто нужно, чтобы выполнялись какие то действия, при ЧТЕНИИ
# этого атрибута, то можно записать еще короче


class Robot3:

    def __init__(self, power):
        self._power = power

    @property
    def power(self):
        # Здесь может быть что угодно. Например
        print("Вы обратились к атрибуту МОЩНОСТЬ")
        return self._power


Toric = Robot3(100)
x = Toric.power
Y = Toric.power
