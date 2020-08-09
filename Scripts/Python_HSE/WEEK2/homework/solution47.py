tail = 0
last_range = 0
min_range = 0
a = int(input())
b = int(input())
if b:
    c = int(input())
else:
    c = 0
while c:
    if a < b > c:
        last_range = tail
        if min_range == 0:
            min_range = last_range
        elif min_range > last_range:
            min_range = last_range
        tail = 1
    elif tail:
        tail += 1
    a, b = b, c
    c = int(input())
print(min_range)
