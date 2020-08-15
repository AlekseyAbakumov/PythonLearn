inputList = list(map(int, input().split()))
x = int(input())
position = 1
for i in inputList:
    if i >= x:
        position += 1
print(position)
