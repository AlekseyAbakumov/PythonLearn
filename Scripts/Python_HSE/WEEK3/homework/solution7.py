from math import floor

p, x, y, k = int(input()), int(input()), int(input()), int(input())
i = 0
kop = x * 100 + y
while i < k:
    kop += kop * p / 100
    i = i + 1
    kop = floor(kop)
rubles = kop // 100
kop = kop % 100
print(rubles, kop)
