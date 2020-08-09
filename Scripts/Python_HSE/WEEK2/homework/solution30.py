per_day, distance = float(input()), float(input())
day = 1
total = per_day + (per_day * 10 / 100)

while total < distance:
    total += total * 10 / 100
    day += 1

print(day + 1 if not per_day >= distance else day)
