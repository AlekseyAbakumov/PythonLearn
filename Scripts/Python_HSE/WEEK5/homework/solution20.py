inputList = list(map(int, input().split()))
count = 0
for i in range(len(inputList) - 1):
    if i != 0:
        if inputList[i - 1] < inputList[i] > inputList[i + 1]:
            count += 1
print(count)
