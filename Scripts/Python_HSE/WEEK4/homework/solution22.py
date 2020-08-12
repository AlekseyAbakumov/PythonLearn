def lagrange(n, aq=0, bq=0, cq=0, q=1):
    a = int((n ** .5) - aq) ** 2
    b = int(((n - a) ** .5) - bq) ** 2
    c = int(((n - a - b) ** .5) - cq) ** 2
    d = int((n - a - b - c) ** .5) ** 2
    if n == a + b + c + d:
        return int(a ** .5), int(b ** .5), int(c ** .5), int(d ** .5)

    if q == 1:
        if a > 0:
            return lagrange(n, aq + 1, 0, 0, 1)
        else:
            return lagrange(n, 1, 1, 0, 2)
    elif q == 2:
        if a > 0 or b > 0:
            if b > 0:
                return lagrange(n, aq, bq + 1, 0, 2)
            return lagrange(n, aq + 1, 0, 0, 2)
        else:
            return lagrange(n, 1, 1, 1, 3)

    elif q == 3:
        if a > 0 or b > 0 or c > 0:
            if b > 0 or c > 0:
                if c > 0:
                    return lagrange(n, aq, bq, cq + 1, 3)
                return lagrange(n, aq, bq + 1, 0, 3)
            return lagrange(n, aq + 1, 0, 0, 3)


print(*lagrange(int(input())))
