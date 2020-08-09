previous = int(input())
counter = 0

while previous != 0:
    current = int(input())
    if current > previous:
        counter += 1
    previous = current

print(counter)
