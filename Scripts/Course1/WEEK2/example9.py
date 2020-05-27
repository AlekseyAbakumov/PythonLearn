# ФУНКЦИОНАЛЬНОЕ ПРОГРАММИРОВАНИЕ
# В функцию можно передавать другую функцию

def caller(func, params):
    return func(*params)


def printer(name, origin):
    print('I\'m {} of {} !'.format(name, origin))


x = caller(printer, ['Moana', 'Motunui'])


# В функции можно создавать другую функцию

def get_multiplier(number):
    def get_inner(a):
        return a * number

    return get_inner


# В этот момент получаем фукнцию, которая любой аргумент будет умножать на 2
x = get_multiplier(2)
y = x(10)  # Х в этот момент хранит в себе уже функцию
print(y)
# Этоже можно увидеть, если обратиться к имени Х
print(x.__name__)

# АНОНИМНАЯ ФУНКЦИЯ
# Применяется, когда функцию не надо делать постоянно рабочей
# Анонимные фукнции могут содержать только одно выражение, но выполняются они
# быстрее
print("Анонимная функция")
myFunc = lambda x, y: x + y
x = myFunc(1, 1)
print(x)

myFunc2 = lambda *args: args + args
x = myFunc2(1, 2, 3, 4, 5)
print(x)
