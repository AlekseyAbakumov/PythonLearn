inputList = list(map(int, input().split()))
for i in range(len(inputList) - 1):
    if inputList[i] < inputList[i + 1]:
        print(inputList[i + 1], end=' ')
