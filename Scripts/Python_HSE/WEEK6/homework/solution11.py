def cutAndMakeTuple(*args):
    return int(args[0][2]), int(args[0][3])


studentList = []
fileInput = open('input.txt', 'r', encoding='utf-8')
for line in fileInput:
    studentList.append(cutAndMakeTuple(line.strip().split(' ')))

maxScore9 = 0
maxScore10 = 0
maxScore11 = 0
for s in studentList:
    if s[0] == 9 and s[1] >= maxScore9:
        maxScore9 = s[1]
    elif s[0] == 10 and s[1] >= maxScore10:
        maxScore10 = s[1]
    elif s[0] == 11 and s[1] >= maxScore11:
        maxScore11 = s[1]
fileInput.close()
print(maxScore9, maxScore10, maxScore11, sep=' ')
