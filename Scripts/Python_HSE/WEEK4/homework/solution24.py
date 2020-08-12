def sqr(z=0):
    n = int(input())
    if n ** .5 == int(n ** .5) and n:
        z = ''
    if n == 0:
        print(z, end=' ')
    if n:
        sqr(z)
        if n ** .5 == int(n ** .5) and n:
            print(n, end=' ')


sqr()
