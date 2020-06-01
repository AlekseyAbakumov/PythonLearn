# СТАТИЧЕСКИЙ МЕТОД


class Human:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    @staticmethod
    def is_age_valid(age):  # Статический метод принимает только те аргументы
        # которые ему передадут. Здесь нет cls или self
        return 0 < age < 150


# Обращаться к методу можно относительно имени класса
x = Human.is_age_valid(35)
print(x)
# или имени экземпляра
bob = Human("Bob")
x = bob.is_age_valid(234)
print(x)
