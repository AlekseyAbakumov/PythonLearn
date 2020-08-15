inputList = list(map(int, input().split()))
for i in range(len(inputList) - 1):
    (inputList[len(inputList) - i - 1], inputList[len(inputList) - i - 2]) = \
        (inputList[len(inputList) - i - 2], inputList[len(inputList) - i - 1])
print(*inputList)
