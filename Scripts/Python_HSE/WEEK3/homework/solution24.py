originalStr = input()
first_pos = originalStr.find('h')
last_pos = originalStr.rfind('h')
first_s = originalStr[:first_pos + 1]
last_s = originalStr[last_pos:]
temps = originalStr[first_pos + 1:last_pos].replace('h', 'H')
print(first_s + temps + last_s)
