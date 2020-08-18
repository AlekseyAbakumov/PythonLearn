def mergeLists(aList, bList):
    aList.extend(bList)
    aList.sort()
    return aList


aList = list(map(int, input().split()))
bList = list(map(int, input().split()))
print(*mergeLists(aList, bList))
