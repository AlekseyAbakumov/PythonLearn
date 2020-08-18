def IntersectionLists(A, B):
    out_list = []
    i_a = 0
    i_b = 0
    lA = len(A)
    lB = len(B)
    while i_a < lA and i_b < lB:
        if A[i_a] < B[i_b]:
            i_a += 1
        elif A[i_a] == B[i_b]:
            out_list.append(A[i_a])
            i_a += 1
            i_b += 1
        else:
            i_b += 1
    return out_list


listA = list(map(int, input().split()))
listB = list(map(int, input().split()))
print(*IntersectionLists(listA, listB))
