originalStr = input()
tempString = ''
for i in range(len(originalStr)):
    if i % 3 != 0:
        tempString += originalStr[i]
print(tempString)
