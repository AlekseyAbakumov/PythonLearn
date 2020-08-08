a1, b1, a2, b2 = (int(input()) for _ in range(4))
if (a1 + b1 + a2 + b2) % 2 == 0:
    print("YES")
else:
    print("NO")
