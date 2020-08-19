num = int(input())
members = [input().split() for i in range(num)]
for i in sorted(members, key=lambda x: int(x[1]), reverse=True):
    print(i[0])
