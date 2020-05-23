# ЧЕРЕЗ СКОЛЬКО ОПЕРАЦИЙ RANDOM ВЕРНЕТ ПОВТОР?
import random

random_set = set()
i = 0
while True:
    x = random.randint(1, 10)
    if x in random_set:
        break
    else:
        random_set.add(x)
        i += 1
print(random_set)
print(x)
print(i)

x=[1,'1']
print(x)
