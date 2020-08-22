n = int(input())
myDict = dict()
for i in range(n):
    line = input()
    syn1, syn2 = line.split()
    myDict[syn1] = syn2
    myDict[syn2] = syn1
word = input()
print(myDict[word])
