a, b, c = (int(input()) for _ in range(3))
hyp = max(a, b, c)
side1 = min(a, b, c)
side2 = a + b + c - hyp - side1
condition = a < b + c and b < a + c and c < a + b
if hyp ** 2 == side1 ** 2 + side2 ** 2 and condition:
    print("rectangular")
elif hyp ** 2 < side1 ** 2 + side2 ** 2 and condition:
    print("acute")
elif condition:
    print("obtuse")
else:
    print("impossible")
