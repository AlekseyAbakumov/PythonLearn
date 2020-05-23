# получим медиану случайного списка
import random
import statistics

x = random.randint(1, 10)  # Добавь N-ое количество элементов
numbers = []
for _ in range(x):  # Нижнее подчеркивание говорит о том, что нам не интересно
    # что содержит переменная. Только важно, чтобы цикл отработал
    # N-ое количество раз
    numbers.append(random.randint(1, 10))  # Добавь N-е значение

print(numbers)
numbers.sort()
print(numbers)
y = statistics.median(numbers)
print(y)
