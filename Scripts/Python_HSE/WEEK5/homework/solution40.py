inputList = list(map(int, input().split()))
tempNotNullElements = []
tempNullElements = []
for i in inputList:
    if i == 0:
        tempNullElements.append(inputList[inputList.index(i)])
    else:
        tempNotNullElements.append(inputList[inputList.index(i)])
print(*(tempNotNullElements + tempNullElements))
