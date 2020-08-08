n, m, k = (int(input()) for _ in range(3))
if (k % m == 0 or k % n == 0) and k < m * n:
    print('YES')
else:
    print('NO')
