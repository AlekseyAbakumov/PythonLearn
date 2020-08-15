N = int(input())
s = list(map(int, input().split()))
x = int(input())
temp = []
for i in range(N):
    s[i] = int(s[i])
    temp.append(abs(s[i] - x))
print(s[temp.index(min(temp))])
