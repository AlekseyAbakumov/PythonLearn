originalString = input()
if originalString.find('f') == -1:
    print(-2)
else:
    temp = 1
    pos = originalString.find('f')
    while pos != -1:
        pos = originalString.find('f', pos + 1)
        temp += 1
    if temp - 1 == 1:
        print(-1)
    else:
        print(originalString.find('f', originalString.find('f') + 1))
