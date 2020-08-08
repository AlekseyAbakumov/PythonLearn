a1, b1, a2, b2 = (int(input()) for _ in range(4))
if a1 - a2 in (-1, 0, 1) and b1 - b2 in (-1, 0, 1):
    print("YES")
else:
    print("NO")
