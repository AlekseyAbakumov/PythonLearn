fin = open('input.txt', 'r', encoding='utf-8')
party_votes = {}
total_votes = 0
seats = 450
for line in fin:
    party = line.rsplit(maxsplit=1)[0]
    votes = int(line.rsplit(maxsplit=1)[1])
    total_votes += votes
    party_votes[party] = party_votes.get(party, 0) + votes
fin.close()

fsp = total_votes / 450

for i in party_votes:
    i_seats = int(party_votes.get(i) // fsp)
    i_fraction = party_votes.get(i) / fsp - i_seats
    party_votes[i] = [(i_fraction, party_votes.get(i)), i_seats]
    seats -= i_seats

for i in sorted(party_votes, reverse=True, key=party_votes.get):
    if seats:
        party_votes[i] = party_votes.get(i)[1] + 1
        seats -= 1
    else:
        party_votes[i] = party_votes.get(i)[1]

for i in party_votes:
    print(i, party_votes[i])
