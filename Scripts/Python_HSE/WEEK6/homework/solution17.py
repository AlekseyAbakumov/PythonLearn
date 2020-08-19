distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
distances.sort(reverse=True)
prices.sort()
SUM = 0
for i in range(len(distances)):
    SUM += distances[i] * prices[i]
print(SUM)
