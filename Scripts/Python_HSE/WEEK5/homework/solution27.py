inputList = list(map(int, input().split()))
b = list(map(int, input().split()))
k = b[0]
C = b[1]
inputList.insert(k, C)
print(' '.join(map(str, inputList)))
