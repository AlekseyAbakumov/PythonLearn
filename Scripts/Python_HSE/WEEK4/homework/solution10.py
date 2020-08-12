def IsPrime(n):
    i = 1
    while i != n:
        i += 1
        if n % i == 0:
            if i != n:
                return 1
        if i >= n ** (1 / 2):
            return 0


n = int(input())
if IsPrime(n):
    print('NO')
else:
    print('YES')
