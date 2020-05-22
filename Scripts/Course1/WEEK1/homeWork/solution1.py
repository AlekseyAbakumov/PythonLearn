# Сумма всех цифр в строке
import sys

digit_string = sys.argv[1]
# digit_string = "111"
mySum = 0
for i in digit_string:
    mySum += int(i)
print(mySum)
