inputList = list(map(int, input().split()))
maxElement = inputList[0]
indexOfMaxElement = 0
for i in range(len(inputList)):
    if inputList[i] > maxElement:
        maxElement = inputList[i]
        indexOfMaxElement = i
print(maxElement, indexOfMaxElement)
