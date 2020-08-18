shoeSize = int(input())
availableShoeSize = list(map(int, input().split()))
availableShoeSize.sort()
shoesNum = 0
for shoe in availableShoeSize:
    if shoesNum == 0:
        if shoe >= shoeSize:
            shoeSize = shoe
            shoesNum += 1
    else:
        if shoe - shoeSize >= 3:
            shoeSize = shoe
            shoesNum += 1
print(shoesNum)
