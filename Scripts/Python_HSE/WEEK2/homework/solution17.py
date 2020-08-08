a, b, c, d, e = (int(input()) for _ in range(5))
if (d >= a and e >= b or d >= a and e >= c or
        d >= b and e >= a or d >= b and e >= c or
        d >= c and e >= a or d >= c and e >= b):
    print("YES")
else:
    print("NO")
