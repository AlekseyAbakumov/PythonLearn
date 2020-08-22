myDict = {}
n = int(input())
for i in range(n):
    line = input().split()
    for j in range(1, len(line)):
        myDict[line[j]] = line[0]
m = int(input())
for k in range(m):
    capital = input()
    print(myDict[capital])
