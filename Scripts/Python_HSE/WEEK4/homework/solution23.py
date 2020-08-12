def cubeSum(n, q1=0, q2=0, q3=0, q4=0, q5=0, q6=0, q7=0):
    n1 = int((n ** (1 / 3)) - q1) ** 3
    n2 = int(((n - n1) ** (1 / 3)) - q2) ** 3
    n3 = int(((n - n1 - n2) ** (1 / 3)) - q3) ** 3
    n4 = int(((n - n1 - n2 - n3) ** (1 / 3)) - q4) ** 3
    n5 = int(((n - n1 - n2 - n3 - n4) ** (1 / 3)) - q5) ** 3
    n6 = int(((n - n1 - n2 - n3 - n4 - n5) ** (1 / 3)) - q6) ** 3
    n7 = int(((n - n1 - n2 - n3 - n4 - n5 - n6) ** (1 / 3)) - q7) ** 3

    if not n - n1 - n2 - n3 - n4 - n5 - n6 - n7:
        return n1, n2, n3, n4, n5, n6, n7

    if n1 > 8:
        return cubeSum(n, q1 + 1, q2, q3, q4, q5, q6, q7)
    if n2 > 8:
        return cubeSum(n, q1, q2 + 1, q3, q4, q5, q6, q7)
    if n3 > 8:
        return cubeSum(n, q1, q2, q3 + 1, q4, q5, q6, q7)
    if n4 > 8:
        return cubeSum(n, q1, q2, q3, q4 + 1, q5, q6, q7)
    if n5 > 8:
        return cubeSum(n, q1, q2, q3, q4, q5 + 1, q6, q7)
    if n6 > 8:
        return cubeSum(n, q1, q2, q3, q4, q5, q6 + 1, q7)
    if n7 > 8:
        return cubeSum(n, q1, q2, q3, q4, q5, q6, q7 + 1)
    return 0,


print(*cubeSum(int(input())))
