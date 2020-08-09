num = int(input())
i = 0
result = 2

while result < num:
    i += 1
    result *= 2
print(0 if num in (0, 1) else i + 1)
