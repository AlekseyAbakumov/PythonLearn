inputList = list(map(int, input().split()))
k = int(input())
for i in range(k, len(inputList) - 1):
    inputList[i] = inputList[i + 1]
else:
    inputList.pop()
print(*inputList)
