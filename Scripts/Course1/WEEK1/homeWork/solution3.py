# Скрипт решения квадратных уравнений
import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

# a = "1"
# b = "-3"
# c = "2"

int_a, int_b, int_c = int(a), int(b), int(c)
d = int_b ** 2 - 4 * int_a * int_c
if d > 0:
    x1 = ((-1) * int_b + math.sqrt(d)) / (2 * int_a)
    x2 = ((-1) * int_b - math.sqrt(d)) / (2 * int_a)
    print(int(x1))
    print(int(x2))
elif d == 0:
    x = -1 * int_b / 2 * int_a
    print(int(x))
else:
    print("Решения нету")
