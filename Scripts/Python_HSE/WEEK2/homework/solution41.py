n = int(input())
a, b = 0, 1
counter = 0

while a < n:
    a, b = b, a + b
    counter += 1

print(counter if a == n else -1)
