inputList = list(map(int, input().split()))
count = 0
for i in range(len(inputList)):
    if inputList[i] > 0:
        count += 1
print(count)
