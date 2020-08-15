inputList = list(map(int, input().split()))
minOdd = 0
for i in range(len(inputList)):
    if inputList[i] % 2 != 0:
        minOdd = inputList[i]
for i in range(len(inputList)):
    if inputList[i] % 2 != 0 and minOdd > inputList[i]:
        minOdd = inputList[i]
print(minOdd)
