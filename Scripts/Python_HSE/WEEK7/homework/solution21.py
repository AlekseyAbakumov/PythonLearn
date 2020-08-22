def deposit(lst, dct):
    name = lst[1]
    amount = int(lst[-1])
    dct[name] = dct.get(name, 0) + amount


def withdraw(lst, dct):
    name = lst[1]
    amount = int(lst[-1])
    dct[name] = dct.get(name, 0) - amount


def balance(lst, dct):
    name = lst[1]
    print(dct.get(name, 'ERROR'))


def transfer(lst, dct):
    name1, name2 = lst[1], lst[2]
    amount = int(lst[-1])
    dct[name1] = dct.get(name1, 0) - amount
    dct[name2] = dct.get(name2, 0) + amount


def income(lst, dct):
    p = 1 + float(lst[-1]) / 100
    for name in dct:
        if dct.get(name) > 0:
            dct[name] = int(dct.get(name) * p)


accounts = {}

fin = open('input.txt', 'r', encoding='utf-8')
for line in fin:
    operation = line.split()[0].lower()
    eval(operation)(line.split(), accounts)
fin.close()
