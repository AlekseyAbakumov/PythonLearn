a, b = int(input()), int(input())
for i in range(a, b + 1):
    if i // 100 == (i % 10) * 10 + (i % 100) // 10:
        print(i)
