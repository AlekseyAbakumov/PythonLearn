# ОБРАБОТКА ИСКЛЮЧЕНИЙ КЛАССОВ

try:
    1 / 0  # Если этот блок отработает с ошибкой
except:
    print("Ошибка")  # То управление будет передано сюда

try:
    1 / 0
except Exception:  # Сюда будет передано управление, при любой ошибке данного
    # типа
    print("Ошибка")

# Полный блок
print("Данная программа разделит одно число на другое")
try:
    x = int(input("Введите число Х:"))
    y = int(input("Введите число Y:"))
    z = x / y
except ValueError:  # Обрабатываем ошибку, если не введено число
    print("Вы ввели не число")
except ZeroDivisionError:  # Обрабатываем ошибку, если деление на ноль
    print("Вы попытались поделить на ноль")
else:  # обрабатываем, если никаких ошибок нет
    print(z)
finally:  # Обрабатываем всегда. Без разницы на ошибки
    print("End Program")
