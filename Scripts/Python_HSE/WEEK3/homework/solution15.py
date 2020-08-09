originalString = input()
reverseString = originalString[::-1]
headPos = len(originalString) - reverseString.find('f') - 1
if originalString.find('f') != -1:
    if headPos == originalString.find('f'):
        print(originalString.find('f'))
    elif headPos != originalString.find('f'):
        print(originalString.find('f'), headPos)
