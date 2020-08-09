originalString = input()
temps = originalString[originalString.find('h') + 1:originalString.rfind('h')]
temps = temps + temps
first_s = originalString[:originalString.find('h') + 1]
last_s = originalString[originalString.rfind('h'):]
print(first_s + temps + last_s)
