# ИТЕРАТОРЫ

for i in range(3):
    print(i)

# как это работает внутри

i = iter([0, 1, 2])

print(next(i))
print(next(i))
print(next(i))
# Тут выбрасывается исключние StopIteration
# print(next(i))

print("Мой итератор")
# Можно написать свой итератор, используя магические методы
class MyIterator:
    """Класс итератора. Аналог Range"""
    def __init__(self, start, end):
        self.current=start
        self.end=end

    # Подразумеваем, что работает с итератором
    def __iter__(self):
        return self

    # определяем, что происходит при итерации
    def __next__(self):
        # если следующая итерация больше или равна последнему значение, нужно
        # выбрасывать исключение
        if self.current>=self.end:
            raise StopIteration

        # в противном случае возвращать результат
        result=self.current
        self.current+=1
        return  result

for i in MyIterator(0,3):
    print(i)