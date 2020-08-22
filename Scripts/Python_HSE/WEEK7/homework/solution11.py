with open('input.txt', 'r', encoding='utf8') as fin:
    a = fin.readlines()
    a[0] = a[0].strip().replace("(", "")
    a[0] = a[0].strip().replace(")", "")
    a[0] = a[0].strip().replace("-", "")
    if len(a[0]) == 7:
        a[0] = '495' + a[0]
    num = {}
    for n in range(1, len(a)):
        num[n] = a[n].strip().replace("-", "")
        num[n] = num[n].strip().replace(")", "")
        num[n] = num[n].replace("(", "").strip()
        if len(num[n]) == 7:
            num[n] = '495' + num[n]
        if len(a[0]) >= 10 and len(num[n]) >= 10:
            if a[0][-10:] == num[n][-10:]:
                print("YES")
            else:
                print("NO")
