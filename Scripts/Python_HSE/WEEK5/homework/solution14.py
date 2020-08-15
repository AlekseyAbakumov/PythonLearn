inputList = list(map(int, input().split()))
for i in range(len(inputList)):
    if inputList[i] % 2 == 0:
        print(inputList[i], end=' ')
