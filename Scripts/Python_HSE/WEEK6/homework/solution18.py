fin = open('input.txt', 'r', encoding='utf8')
fin.readline()
parties = []
votes = []
sumvot = 0
for party in fin:
    if party == 'VOTES:\n':
        break
    parties.append(party.strip())
    votes.append(0)
for vote in fin:
    sumvot += 1
    votes[parties.index(vote.strip())] += 1
for i in range(len(votes)):
    if votes[i] * 100 / sumvot >= 7:
        print(parties[i])
