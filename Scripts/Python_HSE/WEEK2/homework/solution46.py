x1 = int(input())
x2 = int(input())
n_max = 1
n = 1
while 0 == 0:
    if x2 == 0 or x1 == 0:
        break
    while x1 > x2:
        if x2 == 0:
            break
        n += 1
        if n > n_max:
            n_max = n
            x1 = x2
            x2 = int(input())
        else:
            x1 = x2
            x2 = int(input())
    n = 1
    while x1 < x2:
        n += 1
        if n > n_max:
            n_max = n
            x1 = x2
            x2 = int(input())
        else:
            x1 = x2
            x2 = int(input())
    n = 1
    while x1 == x2:
        n = 1
        x1 = x2
        x2 = int(input())
print(n_max)
