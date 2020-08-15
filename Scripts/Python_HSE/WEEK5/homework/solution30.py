inputList = list(map(int, input().split()))
uniqueValues = []
for i in inputList:
    if uniqueValues.count(i) == 0:
        uniqueValues.append(i)
print(uniqueValues.__len__())
