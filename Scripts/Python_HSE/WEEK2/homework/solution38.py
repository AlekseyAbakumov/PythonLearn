num = int(input())
max1 = max2 = 0

while num != 0:
    if max1 < num:
        max2 = max1
        max1 = num
    elif max2 < num:
        max2 = num
    num = int(input())

print(max2)
