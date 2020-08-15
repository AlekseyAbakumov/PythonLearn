inputList = list(map(int, input().split()))
index_of_min = 0
index_of_max = 0
for i in range(1, len(inputList)):
    if inputList[i] > inputList[index_of_max]:
        index_of_max = i
    if inputList[i] < inputList[index_of_min]:
        index_of_min = i
inputList[index_of_min], inputList[index_of_max] = \
    inputList[index_of_max], inputList[index_of_min]
print(' '.join(map(str, inputList)))
