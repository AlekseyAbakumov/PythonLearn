from math import sqrt

x = []
now = int(input())
x.append(now)
while now != 0:
    now = int(input())
    x.append(now)
x = x[:-1]
SUMx = sum(x) / len(x)
SUM = 0
for i in range(len(x)):
    SUM += (x[i] - SUMx) ** 2
print(sqrt(SUM / (len(x) - 1)))
