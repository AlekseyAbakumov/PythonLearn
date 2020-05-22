import random

x = random.randint(0, 1000)
y = None
z = 0
while x != y:
    z += 1
    y = int(input("Введите число:"))
    if y > x:
        print("Введенное число больше загаданого")
    elif y < x:
        print("Введенное число меньше загаданного")
    else:
        print("Вы ввели правильное число. Вам понадобилось " + str(z) + " " +
              "попыток.")