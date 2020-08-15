inputList = list(map(int, input().split()))
for i in range(len(inputList) - 1):
    if inputList[i] > 0 and inputList[i + 1] > 0 \
            or inputList[i] < 0 and inputList[i + 1] < 0:
        print(inputList[i], inputList[i + 1])
        break
