with open('input.txt', 'r', encoding='utf-8') as f:
    first_line = f.readline().split()
    n = int(first_line[0])
    m = int(first_line[1])
    setAnnya = set()
    setBoris = set()
    for i in range(n):
        setAnnya.add(int(f.readline()))
    for i in range(m):
        setBoris.add(int(f.readline()))
    unionSet = setAnnya | setBoris
    print(len(setAnnya & setBoris))
    print(*sorted(setAnnya & setBoris))
    print(len(unionSet - setBoris))
    print(*sorted(unionSet - setBoris))
    print(len(unionSet - setAnnya))
    print(*sorted(unionSet - setAnnya))
