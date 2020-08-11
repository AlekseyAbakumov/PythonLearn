def perimeter(x1, y1, x2, y2, x3, y3):
    a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
    b = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** (1 / 2)
    c = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** (1 / 2)
    return a + b + c


x1, y1, x2, y2, x3, y3 = float(input()), float(input()), float(input()), \
                         float(input()), float(input()), float(input())
print(perimeter(x1, y1, x2, y2, x3, y3))
