from math import sqrt


def MinDivisor(n):
    divider, i = 1, 2
    while i <= sqrt(n):
        if n % i == 0:
            divider = i
            break
        i = i + 1
    return divider


n = int(input())
if MinDivisor(n) == 1:
    print(n)
else:
    print(MinDivisor(n))
