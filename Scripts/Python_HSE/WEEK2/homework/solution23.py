l1, r1 = int(input()), int(input())
l2, r2 = int(input()), int(input())
l3, r3 = int(input()), int(input())
answer = ''
flag = 1
L12, R12, L23, R23, L123, R123 = 0, 0, 0, 0, 0, 0
if l1 <= l2 <= l3:
    L1, L2, L3 = l1, l2, l3
    R1, R2, R3 = r1, r2, r3
elif l1 <= l3 <= l2:
    L1, L2, L3 = l1, l3, l2
    R1, R2, R3 = r1, r3, r2
elif l2 <= l1 <= l3:
    L1, L2, L3 = l2, l1, l3
    R1, R2, R3 = r2, r1, r3
elif l2 <= l3 <= l1:
    L1, L2, L3 = l2, l3, l1
    R1, R2, R3 = r2, r3, r1
elif l3 <= l1 <= l2:
    L1, L2, L3 = l3, l1, l2
    R1, R2, R3 = r3, r1, r2
else:
    L1, L2, L3 = l3, l2, l1
    R1, R2, R3 = r3, r2, r1

if L2 > R1 and L3 > R2:
    if R3 - L3 < L2 - R1 and R1 - L1 < L3 - R2:
        answer = -1
        flag = 0

a = (L2 <= L1 <= R2) + (L2 <= R1 <= R2)
b = (L1 <= L2 <= R1) + (L1 <= R2 <= R1)
if a or b:
    if L1 <= L2:
        L12 = L1
    else:
        L12 = L2
    if R1 >= R2:
        R12 = R1
    else:
        R12 = R2

a = (L3 <= L2 <= R3) + (L3 <= R2 <= R3)
b = (L2 <= L3 <= R2) + (L2 <= R3 <= R2)
if a or b:
    if L2 <= L3:
        L23 = L2
    else:
        L23 = L3
    if R2 >= R3:
        R23 = R2
    else:
        R23 = R3

a = (L12 <= L3 <= R12) + (L12 <= R3 <= R12)
b = (L3 <= L12 <= R3) + (L3 <= R12 <= R3)
if a or b:
    if L12 <= L3:
        L123 = L12
    else:
        L123 = L3
    if R12 >= R3:
        R123 = R12
    else:
        R123 = R3
    if R123:
        answer = 0
        flag = 0

a = (l3 <= l2 <= r3) + (l3 <= r2 <= r3)
b = (l2 <= l3 <= r2) + (l2 <= r3 <= r2)
r23 = 0
if a or b:
    if l2 <= l3:
        l23 = l2
    else:
        l23 = l3
    if r2 >= r3:
        r23 = r2
    else:
        r23 = r3

a = (l3 <= l1 <= r3) + (l3 <= r1 <= r3)
b = (l1 <= l3 <= r1) + (l1 <= r3 <= r1)
r13 = 0
if a or b:
    if l1 <= l3:
        l13 = l1
    else:
        l13 = l3
    if r1 >= r3:
        r13 = r1
    else:
        r13 = r3

if flag:
    if r23:
        answer = 1
    elif r2 <= l3 and r1 - l1 >= l3 - r2:
        answer = 1
    elif r3 <= l2 and r1 - l1 >= l2 - r3:
        answer = 1
    elif r13:
        answer = 2
    elif r1 <= l3 and r2 - l2 >= l3 - r1:
        answer = 2
    elif r3 <= l1 and r2 - l2 >= l2 - r1:
        answer = 2
    else:
        answer = 3
print(answer)
