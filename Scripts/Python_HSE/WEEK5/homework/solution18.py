inputList = list(map(int, input().split()))
temp = 0
for i in range(len(inputList) - 1):
    if inputList[i] >= inputList[i + 1]:
        temp = 1
        break
if temp == 1:
    print('NO')
else:
    print('YES')
