price = float(input())
print(int(price // 1), ' ', int(('{0:.0f}'.format(price * 100 % 100))), sep='')
