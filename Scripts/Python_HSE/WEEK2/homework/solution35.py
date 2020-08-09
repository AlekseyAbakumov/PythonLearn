num = int(input())
counter = 0
total = 0

while num != 0:
    counter += 1
    total += num
    num = int(input())

print(total / counter)
