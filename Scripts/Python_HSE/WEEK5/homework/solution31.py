inputList = list(map(int, input().split(" ")))
resultList = []
temp = []
for i in range(len(inputList)):
    while i < len(inputList) - 1 and len(resultList) < len(inputList):
        resultList.append(inputList[i + 1])
        resultList.append(inputList[i])
        i += 2
    if len(inputList) % 2 != 0:
        temp.append(inputList.pop())
        r = temp[0]
        resultList.append(r)
print(*resultList)
