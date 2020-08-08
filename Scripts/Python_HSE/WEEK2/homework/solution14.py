a, b, c = (int(input()) for _ in range(3))
if any(i % 2 == 0 for i in (a, b, c)) and \
        any(i % 2 for i in (a, b, c)):
    print("YES")
else:
    print("NO")
