fin = open('input.txt', 'r', encoding='utf8')
fin.readline()
parties = []
for party in fin:
    if party == 'VOTES:\n':
        break
    parties.append([party.strip(), 0])
for vote in fin:
    for party in parties:
        if vote.strip() == party[0]:
            party[1] += 1
parties.sort(key=lambda prt: [-prt[-1], prt[0]])
for i in range(len(parties)):
    print(parties[i][0])
