def power(a, n):
    if n == 0:
        return 1
    elif n > 0:
        SUM = 1
        while n > 0:
            SUM *= a
            n -= 1
        return SUM
    else:
        SUM = 1
        while n < 0:
            SUM *= 1 / a
            n += 1
        return SUM


a, n = float(input()), int(input())
print(power(a, n))
