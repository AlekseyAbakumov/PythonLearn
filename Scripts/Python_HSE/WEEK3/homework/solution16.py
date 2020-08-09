originalString = input()
reverseString = originalString[::-1]
pos1 = originalString.find('h')
pos2 = reverseString.find('h')
headPos = len(originalString) - pos2 - 1
print(originalString[0:pos1], originalString[headPos + 1:], sep='')
