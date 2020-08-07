n = int(input())
m = int(input())
print((1 - 0 ** (n % m)) * 'NO', (0 ** (n % m)) * 'YES', sep='')
