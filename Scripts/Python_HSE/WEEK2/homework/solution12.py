x1, y1, x2, y2 = (int(input()) for _ in range(4))
first_condition = y1 < y2
second_condition = (x1 + x2 + y1 + y2) % 2 == 0
third_condition = y2 - y1 >= abs(x2 - x1)
print("YES" if first_condition and second_condition and
               third_condition else "NO")
