n = int(input())
sch = 0
k = 1
while k <= n:
    k = str(k)
    if k == k[::-1]:
        sch = sch + 1
    k = int(k)
    k += 1
print(sch)
