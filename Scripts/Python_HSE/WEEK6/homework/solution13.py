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

print(listScore9.count(max(listScore9)), listScore10.count(max(listScore10)),
      listScore11.count(max(listScore11)), sep=' ')
