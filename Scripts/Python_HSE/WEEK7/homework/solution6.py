mySet = set()
fileInput = open('input.txt', 'r', encoding='utf-8')
for line in fileInput:
    myString = line.split()
    for word in myString:
        mySet.add(word)
fileInput.close()
print(len(mySet))
