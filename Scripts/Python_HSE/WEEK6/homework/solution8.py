inputFile = open('input.txt', 'r', encoding='utf8')
outputFile = open('output.txt', 'w', encoding='utf8')
lines = inputFile.readlines()
lines.sort()
for i in lines:
    print(*i.split()[:2] + i.split()[3:], file=outputFile)
inputFile.close()
outputFile.close()
