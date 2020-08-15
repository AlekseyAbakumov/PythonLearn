listA = list(map(int, input().split()))
if len(listA) < 4:
    resultElements = listA[::]
else:
    maxElements = []
    minElements = []
    resultElements = []
    maxElements.append(listA.pop(listA.index(max(listA))))
    if maxElements[0] == 0:
        resultElements.extend(listA[:2:])
        resultElements.append(maxElements[0])
    elif maxElements[0] < 0:
        resultElements.append(maxElements[0])
        for i in range(2):
            resultElements.append(listA.pop(listA.index(max(listA))))
    else:
        resultElements.append(maxElements[0])
        maxElements.append(listA.pop(listA.index(max(listA))))
        if maxElements[1] <= 0:
            for i in range(2):
                resultElements.append(listA.pop(listA.index(min(listA))))
        else:
            resultElements.append(maxElements[1])
            resultElements.append(listA.pop(listA.index(max(listA))))
            if len(listA) > 1:
                for i in range(2):
                    minElements.append(listA.pop(listA.index(min(listA))))
                if minElements[0] * minElements[1] > \
                        resultElements[1] * resultElements[2]:
                    resultElements[1::] = minElements[::]
print(*resultElements)
