n = int(input())
SUM = 0
fac = 1
for i in range(n + 1):
    if i != 0:
        SUM += fac
        fac *= (i + 1)
print(SUM)
