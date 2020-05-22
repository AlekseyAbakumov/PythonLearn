# Рисуем лестницу из решеток
import sys

digit_string = sys.argv[1]
# digit_string = "3"
digit = int(digit_string)
i = 1
while i <= digit:
    mySpace = digit - i
    print(mySpace * " " + "#" * i)
    i += 1
