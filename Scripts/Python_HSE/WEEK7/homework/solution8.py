N = int(input())
poss = set(range(1, N + 1))
ans = []
while True:
    nums = input()
    if 'HELP' in nums:
        break
    else:
        nums = set(map(int, nums.split()))
    if len(nums & poss) * 2 > len(poss):
        ans.append('YES')
        poss.intersection_update(nums)
    else:
        ans.append('NO')
        poss.difference_update(nums)
print(*ans, sep='\n')
print(*sorted(list(poss)))
