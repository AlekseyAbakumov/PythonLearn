myList = list(map(int, input().split()))
mySet = set()
for element in myList:
    if element in mySet:
        print('YES')
    else:
        print('NO')
        mySet.add(element)
