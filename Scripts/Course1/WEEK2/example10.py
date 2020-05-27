# Написать фукнцию, которая превращает список чисел в список строк
def get_retype(*args):
    list_retype = []
    for i in args:
        list_retype.append(str(i))
    return list_retype


x = get_retype(1, 2, 3)
print(x)

# библиотека functools - позволяет запоминать retain значения через reduce
from functools import reduce


def get_multiply(a, b):
    return a + b


# Происходит следующая итерация (((1+2)+3)+4)
x = reduce(get_multiply, [1, 2, 3, 4])
print(x)

print("Списочные выражения")
# СПИСОЧНОЕ ВЫРАЖЕНИЕ - позволяет кое что записать короче
# Длинный, подробный путь
squre_list = []
for number in range(10):
    squre_list.append(number * 10)
print(squre_list)

# короткий способ. Плюс работает быстрее
squre_list = [number * 10 for number in range(10)]
print(squre_list)

# точно также в списочное выражение можно добавлять условие
# длинный метод
even_list = []
for i in range(10):
    if i > 5:
        even_list.append(i)

print(even_list)

# короткий, через списочное выражение
even_list = [i for i in range(10) if i > 5]
print(even_list)

# через списочное выражение можно определять DICT
# До двоеточия КЛЮЧ, после ЗНАЧЕНИЕ. key : value
squre_map = {number: number * 10 for number in range(10)}
print(squre_map)

# через списочное выражение можно определять tuple
reminders_set={num for num in range(10)}
print(reminders_set)
