def cutAndMakeTuple(*args):
    return int(args[0][2]), int(args[0][3])


studentList = []
fileInput = open('input.txt', 'r', encoding='utf-8')
for line in fileInput:
    studentList.append(cutAndMakeTuple(line.strip().split(' ')))

score9 = 0
count9 = 0
score10 = 0
count10 = 0
score11 = 0
count11 = 0
for s in studentList:
    if s[0] == 9:
        score9 += s[1]
        count9 += 1
    elif s[0] == 10:
        score10 += s[1]
        count10 += 1
    elif s[0] == 11:
        score11 += s[1]
        count11 += 1
fileInput.close()
print(score9 / count9, score10 / count10, score11 / count11, sep=' ')
