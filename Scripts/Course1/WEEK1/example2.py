# Логические типы
print("Логические типы")
result = True
print(type(result))
print(13 == 13)  # Знак двух равенств означает не присвоить, а сравнить
print(1 != 2)  # Неравенство записывается последовательностью Воскл.знак+равно
print(3 > 4)
print(3 <= 3)
print(6 >= 10)
print(6 < 5)
# Разрешено множественное сравнение
print("Множественное сравнение")
x = 2
print(0 < x < 3)
print(0 < x < 2)
# Логические операторы
print("Логичесткие операторы")
x, y = 1, 2
print((x and y) == 1)
print((x or y) == 1)
print("Логическое отрицание")
y = True
print(not y)  # Превращает Правду в Ложь, а Ложь в Правду
# Задача определить високосный год или нет?
print("Задача определить високосный год или нет?")
# Подсказка, год високосный, если кратен 4, но не кратен 100, либо кратен 400
year = 2019  # Високосный год 2020
y = (year % 4) == 0
y1 = (year % 100) != 0
y2 = (year % 400) == 0
y3 = (y and (y1 or y2))
print(y, y1, y2, y3)
z = "Год " + str(year) + " = " + str(y3)
print(z)
