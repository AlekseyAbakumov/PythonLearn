# ООП, с ютуба
# Это класс


class Person:  # Имя класса
    # Это характеристики класса
    name = "Ivan"
    age = 10

    # Это методы класса
    def set(self, name, age):
        self.name = name
        self.age = age


# Это объект класса
# В первом случае я назначаю характеристики напрямую, без использования методов
vlad = Person()
print(vlad.name)
vlad.name = 'Vlad'
print(vlad.name)

ivan = Person()
ivan.age = 45
print(ivan.age)

# Создаем объект класса и присваивает характеристики через методы
Alex = Person()
Alex.set("Alex", 25)
print(Alex.name + "  " + str(Alex.age))
