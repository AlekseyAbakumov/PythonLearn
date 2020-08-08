a, b, c, d = (int(input()) for _ in range(4))
if a == 0 and b == 0:
    print("INF")
elif a == 0 and b != 0:
    print("NO")
else:
    x = -b / a
    if x == int(x) and c * x + d != 0:
        print(int(x))
    else:
        print("NO")
