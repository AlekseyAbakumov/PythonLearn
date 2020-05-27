# ФУНКЦИИ

from datetime import datetime


def get_second():  # Начало функции
    """Return current second"""  # Строка документации
    return datetime.now().second  # Что функция будет возвращать


x = get_second()  # Вызов функции
y = get_second.__doc__  # Вызов документации функции
z = get_second.__name__  # Вызов имени функции
print(x)
print(y)
print(z)

# Вызов функции с параметрами
print("Функция суммирования")


def get_mySum(x, y, z):
    """Суммируем переданные значения"""
    return x + y + z


perem = get_mySum(1, 1, 1)
print(perem)

print("Преобразует текстовую переменную в список")


def get_split_tags(tag_string):
    """Преобразует текстовую переменную в список"""
    tag_list = []
    for tag in tag_string.split(','):
        tag_list.append(tag.strip())

    return tag_list


x = get_split_tags('python, coursera, mooc')
print(x)


# Аннотация типов
def get_add(x: int, y: int) -> int:  # Можно конкретно указать, какой тип
    # будет подаваться и возвращаться
    return x + y


print(get_add(10, 11))
# Но Python - это динамический язык, поэтому будет работать и с др. типов
print(get_add('I ', 'am'))

# ИМЕНОВАННЫЕ АРГУМЕНТЫ
print("Именованные аргументы")


def get_say(greeting, name):
    print('{} {}!'.format(greeting, name))


print(get_say('Hello', 'Kitty'))
print(get_say(name='Kitty', greeting='Hello'))


# Дефолтное значение
def get_mySum2(x=2):
    return x * 10


print(get_mySum2())  # Аргумент мы не указали, но функция вернула результат

# Можно передавать неизвестное количество аргументов
print("Можно передавать неизвестное количество аргументов")


def get_printer(*args): # ARGS - это tuple
    th = []
    for i in args:
        print(i)
        th.append(i)
    return th


result = get_printer(1, 2, 3, 4, 5)
print(result)


def get_printer2(**kwargs): # KWARGS - это Dict
    th={}
    for key, value in kwargs.items():
        th[key]=value

    return th

result=get_printer2(pil567='Approve', pil876='Decline')
print(result)
