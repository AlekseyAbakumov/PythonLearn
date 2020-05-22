# СПИСКИ
empty_list = []
empty_list = list()
none_list = [None] * 10
collections = ['list', 'tuple', 'dict', 'set']
# список списков
user_data = [
    ['Elena', 4.4],
    ['Andrey', 4.2]
]
# длина списка (количество элементов)
x = len(collections)
print(x)

# Индексы и срезы
print(collections)
print(collections[0])  # Первый элемент списка
print(collections[-1])  # Первый с конца элемент списка

print("Замена элемента в списке")
collections[3] = "frozenset"  # Замена элемента списка
print(collections)

print("Есть ли объект в списке?")
y = "tuple"
print(y in collections)  # Есть ли объект в списке

# Срез списка
print("Срез списка")
range_list = list(range(10))  # Создать список от 0 до 9
print(range_list[1:3])  # Вывести второй и третий элемент списка.
print(range_list[3:])  # Вывести с четвертого элемента до конца
print(range_list[:5])  # Вывести ДО пятого элемента
print(range_list[::2])  # Вывести каждый второй элемент списка
print(range_list[::-1])  # Вывести с последнего до первого элемента

# Можно итерироваться по списку
print("Можно итерироваться по списку")
collections = ['list', 'tuple', 'dict', 'set']
for i in collections:
    print(i)

# Добавить элемент в список
print("Добавить элемент в список")
collections.append("OrdereDict")  # Добавить элемент в список
print(collections)
collections.extend(
    ['ponyset', 'unicorndict'])  # Добавляем список в конец другого списка
print(collections)
collections+=["1"] # Добавить в список простым добавлением
print(collections)

# Удалить элемент списка
print("Удалить элемент списка")
del collections[1] # Удалить второй элемент списка
print(collections)

# Списки поддерживают агрегатные функции
print("Списки поддерживают агрегатные функции")
numbers=[4,17,19,9,2,6,10,13]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Вывести значения списка в строку
print("Вывести значения списка в строку")
tag_list=(' - '.join(collections))
print(collections)
print(tag_list)

# Сортировка списка
print("Сортировка списка")
print(sorted(numbers)) # SORTED - только выводит, не сохраняя значение
numbers.sort() # SORT - сортирует и сохраняет
print(numbers)
print(sorted(numbers,reverse=True)) # Сортировка в обратном порядке
numbers.sort(reverse=True)
print(numbers)

# КОРТЕЖИ
print("КОРТЕЖИ - это неизменяемые списки")
empty_tuple=()
empty_tuple=tuple()
immutables=(int,str,tuple)

print("Хоть кортеж не изменяем, но его элементы МОГУТ БЫТЬ изменяемыми")
print("Если кортеж в качестве элементов содержит списки")
x=[1,1,1]
y=[2,2,2]
z=(x,y)
print(z)
y[0]=100
print(z)

# Кортежи - это хэшируемый объект, и может использоваться в качестве ключей
x="""
Если кортеж состоит из одного элемента, то обязательно нужно ставить запятую. 
Потому что иначе PYthon преобразует его в переменную
"""
print(x)

x=(1,)
print(type(x))
x=(1)
print(type(x))
x=("one")
print(type(x))