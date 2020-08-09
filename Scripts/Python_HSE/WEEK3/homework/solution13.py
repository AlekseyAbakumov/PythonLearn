a, b, c, d, e, f = float(input()), float(input()), float(input()), \
                   float(input()), float(input()), float(input())

delta = a * d - c * b
delta_x = e * d - f * b
delta_y = a * f - c * e
x, y, p, q = 0, 0, 0, 0

if not a and not b and not c and not d and not e and not f:
    print('5')
elif (not a and not b and e) or (not c and not d and f):
    print('0')
elif a and c and not b and not d and e / a != f / c:
    print('0')
elif not a and not c and b and d and e / b != f / d:
    print('0')
elif not b and not d and (a or c):
    if a:
        x = int((e / a) * 1000000) / 1000000
    if c:
        x = int((f / c) * 1000000) / 1000000
    print('3', x)
elif not a and not c and (b or d):
    if b:
        y = int((e / b) * 1000000) / 1000000
    elif d:
        y = int((f / d) * 1000000) / 1000000
    print('4', y)
elif delta:
    x = int((delta_x / delta) * 1000000) / 1000000
    y = int((delta_y / delta) * 1000000) / 1000000
    print('2', x, y)
elif a * d == c * b and e * d == f * b and (b or d):
    if b:
        p = int((-a / b) * 1000000) / 1000000
        q = int((e / b) * 1000000) / 1000000
    elif d:
        p = int((-c / d) * 1000000) / 1000000
        q = int((f / d) * 1000000) / 1000000
    print('1', p, q)
else:
    print('0')
