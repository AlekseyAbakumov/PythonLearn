s, b = [], []
n, sel = int(input()), list(map(int, input().split()))
m, bom = int(input()), list(map(int, input().split()))
for i in range(1, n + 1):
    s.append((sel[i - 1], i))
s.sort()
for j in range(1, m + 1):
    b.append((bom[j - 1], j))
b.sort()
c = 0
for i in range(len(s)):
    if c + 1 < m and abs(s[i][0] - b[c][0]) < abs(s[i][0] - b[c + 1][0]):
        sel[s[i][1] - 1] = b[c][1]
    else:
        while c + 1 < m and \
                abs(s[i][0] - b[c][0]) > abs(s[i][0] - b[c + 1][0]):
            c += 1
        sel[s[i][1] - 1] = b[c][1]
print(*sel)
