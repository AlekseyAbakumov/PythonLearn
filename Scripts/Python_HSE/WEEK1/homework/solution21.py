a, b, c = (int(input()) for _ in range(3))
dist = b - c
print((a - b + dist - 1) // dist + 1)
