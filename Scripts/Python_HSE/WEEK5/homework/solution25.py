inputList = list(map(int, input().split()))
if len(inputList) % 2 == 0:
    for i in range(len(inputList) // 2):
        (inputList[i], inputList[len(inputList) - i - 1]) = \
            (inputList[len(inputList) - i - 1], inputList[i])
else:
    for i in range((len(inputList) - 1) // 2):
        (inputList[i], inputList[len(inputList) - i - 1]) = \
            (inputList[len(inputList) - i - 1], inputList[i])
print(*inputList)
