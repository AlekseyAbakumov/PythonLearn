# Комментарий
print("Комментарии")
print("Hello")  # Комментарий
"""
Многострочный
комментарий
"""

# Переменные
print("Переменные")
num = 13
print(num)
num = 0
print(num)
num = -10
print(num)
num = 100_000_000  # Можно поставить как разделитель
print(num)
print(type(num))  # Узнать тип переменной
num = 13.2
print(num)
num = 100_000.000_001
print(num)
print(type(num))
num = "ADB"
print(num)
print(type(num))

x1, y1 = 10, 20  # Можно назначать сразу несколько переменные в одной строке
print(x1, y1)
x1, y1 = y1, x1  # Можно переназначать значения переменных в одной строке
print(x1, y1)
x1 = y1 = 30  # Можно назначать одно значение двум переменных в одной строке
print(x1, y1)

# Сокращенная запись суммы прибавления к переменной к самой себе
z1 = 1
z1 += 1  # Вместо z1 = z1 + 1
print(z1)
# Но тут нужно опасаться если используем изменяемый объект. Например список
x2 = y2 = []
print(y2)
x2.append(1)  # изменяем только X2
print(y2)  # Y2 тоже изменил свое значение

# Конвертация типов
print("Конвертация типов")
num = 150.2
print(type(num))
num = int(num)
print(num)
print(type(num))
