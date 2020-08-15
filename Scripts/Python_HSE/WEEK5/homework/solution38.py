n, m = [int(s) for s in input().split()]
keg = ['I'] * n
for i in range(m):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        keg[j] = '.'
print(''.join(keg))
