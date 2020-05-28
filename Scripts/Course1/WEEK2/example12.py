# ГЕНЕРАТОРЫ

def even_range(start, end):
    current = start
    while current < end:
        yield current  # yield - это временный return. Но он не прекращает
        # выполнение функции
        current += 2
    print("Конец")


for number in even_range(0, 10):
    print(number)

print()


# Это можно использовать для оптимизации
# Пример. Хотим создать список фибоначи
# Обычно
def fibonacci(number):
    result = []
    a = b = 1
    for i in range(number):
        result.append(a)
        a, b = b, a + b
    return result


print(fibonacci(10))


# Все работает, но в этом случае наша функция вынуждена хранить в себе
#  result, который выполняет роль аккомулятора. Промежуточное хранение

# Применим генераторы
def fibonacci2(number):
    a = b = 1
    for _ in range(number):
        yield a
        a, b = b, a + b


for i in fibonacci2(10):
    print(i)

result = []
for i in fibonacci2(10):
    result.append(i)

print(result)

# В этом случае он выполняет функцию только одним обращением. И запоминает
# последний результат. Т.е. если мы вызовем функцию еще раз, то он вернет
# уже следующее значение.
# Мы экономим память