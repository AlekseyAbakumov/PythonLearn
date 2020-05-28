# декораторы
# Это функция, которая принимает функцию и возвращает функцию

def decorator(func):
    return func


@decorator
def decorated():
    print("Hello")


# По сути
# decorated=decorator(decorated)

def decorator(func):
    def new_func():
        print("Истинный Hello")

    return new_func


@decorator
def decorated():
    print('Hello')


decorated()
print(decorated.__name__)


# ОБЪЯСНЕНИЕ. Я вызываю функцию decorated. Ожидается, что она вернет Hello
# Но данная функция обернута в декоратор. Напомним, что декоратор - это
# функция, которая принимает функцию и возвращает функцию. Т.е. можно увидеть,
# что функция decorated - это уже функция New_func. Которая возвращает
# Истинный Hello


# ЗАДАЧА, написать декоратор, который записывает в лог результат
# декорируемой функции

def logger(func):
    def wrapped(num_list):
        result = func(num_list)
        with open('log.txt', 'w') as f:
            f.write(str(result))

        return result

    return wrapped


@logger
def summator(num_list):
    return sum(num_list)


summator([1, 2, 3, 4, 5])
