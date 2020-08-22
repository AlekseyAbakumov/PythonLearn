fileInput = open('input.txt', 'r', encoding='utf8')
candidatesDict = dict()
votes = 0
for line in fileInput:
    line = line.strip()
    votes += 1
    candidatesDict[line] = candidatesDict.get(line, 0) + 1
fileInput.close()
i_c = 0
fileOutput = open('output.txt', 'w', encoding='utf8')
for cnd in sorted(candidatesDict,
                  key=lambda cndl: (-candidatesDict[cndl], cndl)):
    if candidatesDict[cnd] * 100 > votes * 50:
        print(cnd, file=fileOutput)
        break
    elif i_c == 0:
        print(cnd, file=fileOutput)
        i_c += 1
    else:
        print(cnd, file=fileOutput)
        break
fileOutput.close()
