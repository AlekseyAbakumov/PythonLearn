def IsPointInSquare(x, y):
    a = y - x - 1 <= 0
    b = y + x - 1 <= 0
    c = y + x + 1 >= 0
    d = y - x + 1 >= 0
    return a and b and c and d


x, y = float(input()), float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
