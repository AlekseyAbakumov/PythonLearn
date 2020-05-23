# МНОЖЕСТВА - позволяют хранить в неупорядоченном виде
# набор уникальных объектов

empty_set = set()
number_set = {1, 2, 3, 3, 4, 5}  # Две Тройки
print(number_set)  # Одна Тройка

# Проверка, есть ли объект в Множестве, происходит за константное время
print(2 in number_set)

odd_set = set()
even_set = set()

# Итерируемся 10-раз, четные числа в один Set, нечетные в другой
for number in range(10):
    if number % 2:
        odd_set.add(number)  # Добавить элемент в SET
    else:
        even_set.add(number)

print(odd_set)
print(even_set)

# SET - поддерживает математические операции
# Объединить множества

union_set = odd_set | even_set
union_set = odd_set.union(even_set)
print(union_set)

# Пересечение множеств
intersection_set = odd_set & even_set
intersection_set = odd_set.intersection(even_set)
print(intersection_set)

# РАЗНОСТЬ. Данные есть в одном SET, но нет в другом
difference_set = odd_set - even_set
difference_set = odd_set.difference(even_set)
print(difference_set)

# Удалить элементы из SET
even_set.remove(2)
print(even_set)

# FROZENSET - это неизменяемое множество. Добалять/изменять его нельзя
frozen = frozenset([1, 2, 3])
frozen.add(0)  # Ошибка - добавлять элементы нельзя
