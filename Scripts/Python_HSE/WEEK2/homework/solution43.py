n = int(input())
b = n
k = 0
SUM = 0
while b != 0:
    b = b // 10
    k = k + 1
while n != 0:
    a = n % 10
    n = n // 10
    SUM = SUM + a * 10 ** (k - 1)
    k = k - 1
print(SUM)
