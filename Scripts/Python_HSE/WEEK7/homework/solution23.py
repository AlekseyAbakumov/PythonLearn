generation = {}
tree = {}
filein = open('input.txt', 'r', encoding='utf-8')
for N in range(int(filein.readline()) - 1):
    child, parent = filein.readline().split()
    generation[child] = generation.get(child, parent)
filein.close()

parents = set(generation.values())
children = set(generation.keys())
root = (parents - children).pop()

level = 0
tree[level] = [root]

while children:
    children = {x for x in generation if generation[x] in tree[level]}
    level += 1
    for name in children:
        if tree.get(level):
            tree[level].append(name)
        else:
            tree[level] = [name]

for i in tree:
    for v in tree[i]:
        generation[v] = i

for name in sorted(generation):
    print(name, generation[name])
