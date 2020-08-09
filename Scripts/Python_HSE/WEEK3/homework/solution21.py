origStr = input()
if len(origStr) == origStr.count(' '):
    print(0)
if origStr.count(' ') == 1 and len(origStr) == 2:
    print(1)
else:
    print(origStr.count(' ') + 1)
