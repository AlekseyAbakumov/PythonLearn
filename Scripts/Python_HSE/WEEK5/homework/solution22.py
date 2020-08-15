inputList = list(map(int, input().split()))
tempList = []
for i in range(len(inputList)):
    if inputList[i] > 0:
        tempList.append(inputList[i])
print(min(tempList))
