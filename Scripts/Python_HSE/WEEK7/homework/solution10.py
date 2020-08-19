N, K = tuple(map(int, input().split()))
wknds = set(range(6, N + 1, 7)) | set(range(7, N + 1, 7))
strkall = set()
for i in range(K):
    beg, stp = tuple(map(int, input().split()))
    strk = set(range(beg, N + 1, stp))
    strk.difference_update(wknds)
    strkall.update(strk)
print(len(strkall))
