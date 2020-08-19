def cutAndMakeTuple(*args):
    return int(args[0][2]), int(args[0][3])


studentList = []
fileInput = open('input.txt', 'r', encoding='utf-8')
for line in fileInput:
    studentList.append(cutAndMakeTuple(line.strip().split(' ')))
fileInput.close()

listScore9 = []
listScore10 = []
listScore11 = []
for s in studentList:
    if s[0] == 9:
        listScore9.append(s[1])
    elif s[0] == 10:
        listScore10.append(s[1])
    elif s[0] == 11:
        listScore11.append(s[1])

max9 = max(listScore9)
max10 = max(listScore10)
max11 = max(listScore11)
maximum9 = -1
maximum10 = -1
maximum11 = -1

for now in listScore9:
    if maximum9 < now != max9:
        maximum9 = now
for now in listScore10:
    if maximum10 < now != max10:
        maximum10 = now
for now in listScore11:
    if maximum11 < now != max11:
        maximum11 = now
print(maximum9, maximum10, maximum11, sep=' ')
