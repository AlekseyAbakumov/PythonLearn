# Конструкция ветвления
# IF
x = 1
y = 1
z = 2
if x == y:
    print("x равен Y")

if z == x or y < z:
    print("z=x или y<z")

# IF ELSE
if x == z:
    print("x равен z")
else:
    print("x не равен z")

# IF ELIF ELSE
if z == x:
    print("z равен x")
elif z == y:
    print("z равен y")
else:
    print("z ничему не равен")

# Цикл WHILE
i = 0
while i < 100:
    i += 1

print(i)

# Цикл FOR, объект Range
print("Цикл FOR по переменной")
name = "Alex"
for letter in name:
    print(letter)
print("Цикл FOR по объекту")
for i in range(3):  # Будет выполнять от нуля, до 2. Последний элемент
    # не выполняется
    print(i)

# Получим сумму чисел от нуля до 100
print("Сумма чисел от нуля до 100")
x = 0
for i in range(101):  # Т.к. последний элемент не входит в цикл
    x += i

print(x)

# Установление границ объекта RANGE
print("")
for i in range(5, 8):  # последняя не входит в последовательность
    print(i)
# Установление границ объекта RANGE с шагом
print("")
for i in range(1, 10, 2):
    print(i)
# Установление границ объекта RANGE с шагом назад
print("")
for i in range(10, 1, -1):
    print(i)

# Оператор pass выступает как "заглушка"
# делай итерации и ничего в них не выполняй
for i in range(10):
    pass

# Оператор прерывания
print("")
x = 0
for i in range(5):
    x += 1
    print(x)
    if x >= 3:
        break

print("Цикл дошел до конечной остановки. X равен " + str(x))

# CONTINUE - не прерывание, а принудительный перевод к следующей итерации
print("")
x = 0
y = 0
for i in range(10):
    x += 1
    if x > 6:
        continue  # x больше 6, ниже конструкцию цикла не выпонять
    y = x
print(x, y)
