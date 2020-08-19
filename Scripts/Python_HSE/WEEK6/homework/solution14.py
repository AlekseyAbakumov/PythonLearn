inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
myList = [list(line.strip().split()) for line in inFile]
new_l = []
N = int(*myList[0])
for line in myList[1:]:
    a = sorted(list(map(int, line[-1:-4:-1])))
    if a[0] >= 40:
        new_l.append(a)
if len(new_l):
    new_l.sort(key=lambda a: a[0] + a[1] + a[2], reverse=True)
    if N >= len(new_l):
        print(0, file=outFile)
    elif sum(new_l[N - 1]) == sum(new_l[N]):
        c = N - 1
        while c != 0 and sum(new_l[c - 1]) == sum(new_l[c]):
            c -= 1
        if c == 0:
            print(1, file=outFile)
        else:
            print(sum(new_l[c - 1]), file=outFile)
    else:
        print(sum(new_l[N - 1]), file=outFile)

inFile.close()
outFile.close()
