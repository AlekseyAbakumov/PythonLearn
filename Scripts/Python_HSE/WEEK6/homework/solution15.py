with open('input.txt', 'r', encoding='utf-8') as f:
    MAX = 1
    temp = {}
    for line in f:
        list_line = line.split()
        temp[int(list_line[2])] = temp.get(int(list_line[2]), 0) + 1
    dictList = sorted(temp.items(), key=lambda x: (x[1], x[0]))
    maxClass = dictList[-1][1]
    for key, value in dictList:
        if value == maxClass:
            print(key, end=' ')
