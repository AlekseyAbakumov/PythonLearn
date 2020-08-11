a, b, c, d = int(input()), int(input()), int(input()), int(input())


def minvalue(i, j, k, m):
    return min(min(i, j), min(k, m))


print(minvalue(a, b, c, d))
