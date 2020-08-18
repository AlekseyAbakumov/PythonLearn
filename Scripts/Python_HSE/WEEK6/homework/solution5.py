mem, n = map(int, input().split())
volume = sorted([int(input()) for i in range(n)])
amount = sum(volume)
while amount > mem and n:
    amount -= volume.pop()
    n -= 1
print(n)
