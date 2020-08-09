num = int(input())
max_num = num
counter = 0

while num != 0:
    if num == max_num:
        counter += 1
    elif num > max_num:
        max_num = num
        counter = 1
    num = int(input())

print(counter)
