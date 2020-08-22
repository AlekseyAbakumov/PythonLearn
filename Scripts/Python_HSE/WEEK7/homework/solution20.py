customers = {}

fin = open('input.txt', 'r', encoding='utf-8')
for line in fin:
    name, good, qty = line.strip().split()
    if name not in customers:
        customers[name] = {good: int(qty)}
    elif good not in customers[name]:
        customers[name].update({good: int(qty)})
    else:
        customers[name].update({good: customers[name].get(good) + int(qty)})
fin.close()

for name in sorted(customers):
    print(name + ':')
    for good in sorted(customers[name]):
        print(good, customers[name][good])
