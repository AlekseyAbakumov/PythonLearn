def stressed(string):
    x = set()
    for s in range(len(string)):
        if string[s].isupper():
            x.add(int(s) + 1)
    return x


words = {}
errors = 0
fin = open('input.txt', 'r', encoding='utf-8')
for i in range(int(fin.readline())):
    word = fin.readline().strip()
    k = word.lower()
    words[k] = words.get(k, stressed(word)) | stressed(word)
text = fin.read().strip().split()
fin.close()

for word in text:
    k = word.lower()
    accents = stressed(word)
    if len(accents) != 1 or not accents & words.get(k, accents):
        errors += 1

print(errors)
