a, b, c = (int(input()) for _ in range(3))
print(min(a, b, c), a + b + c - max(a, b, c) -
      min(a, b, c), max(a, b, c))
