inputList = list(map(int, input().split()))
uniqueElements = []
for i in inputList:
    if inputList.count(i) == 1:
        uniqueElements.append(inputList[inputList.index(i)])
print(*uniqueElements)
