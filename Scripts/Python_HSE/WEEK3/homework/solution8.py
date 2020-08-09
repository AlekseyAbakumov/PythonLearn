n = int(input())
x = float(input())
i = 0
SUM = 0
while i <= n:
    temp = float(input())
    SUM = SUM * x + temp
    i += 1
print(SUM)
