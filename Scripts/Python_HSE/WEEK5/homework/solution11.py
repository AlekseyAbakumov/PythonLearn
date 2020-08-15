n = int(input())
SUM = n * (n + 1) // 2
for i in range(n - 1):
    temp = int(input())
    SUM -= temp
print(SUM)
