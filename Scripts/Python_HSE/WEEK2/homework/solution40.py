n = int(input())
a, b = 0, 1
i = 0

while i < n:
    a, b = b, a + b
    i += 1

print(a)
