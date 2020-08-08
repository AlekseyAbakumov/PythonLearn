capacity, minutes, cutlets = (int(input()) for _ in range(3))
if cutlets <= capacity:
    print(minutes * 2)
elif cutlets > capacity and cutlets % capacity == 0:
    print(cutlets // capacity * minutes * 2)
elif cutlets / capacity % 1 <= 0.5:
    print(int((cutlets // capacity * 2 + 1) * minutes))
else:
    print((cutlets // capacity + 1) * minutes * 2)
