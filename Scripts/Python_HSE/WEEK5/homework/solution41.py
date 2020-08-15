inputList = list(map(int, input().split()))
maxCount = 0
maxElement = 0
for i in inputList:
    if inputList.count(i) >= maxCount:
        maxCount = inputList.count(i)
        maxElement = inputList[inputList.index(i)]
print(maxElement)
