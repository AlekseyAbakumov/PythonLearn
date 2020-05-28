# декораторы
# Это функция, которая принимает функцию и возвращает функцию

def decorator(func):
    def wrapper():
        print("Код до выполнения функции")
        func()
        print("Код который сработал после выполнения функции")
    return wrapper

def show():
    print("Я обычная функция")

# Можно создать декоратор так
show=decorator(show)
show()


print()
# Либо общепринятый способ
def decorator2(func):
    def wrapper2():
        print("Код до выполнения функции")
        func()
        print("Код, после выполнения функции")
    return wrapper2

@decorator2
def show2():
    print("Сам код функции")

show2()