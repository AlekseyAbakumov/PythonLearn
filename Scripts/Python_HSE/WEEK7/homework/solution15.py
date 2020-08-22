fileInput = open('input.txt', 'r', encoding='utf-8')
votes = dict()
for line in fileInput:
    state = line.split()
    votes[state[0]] = votes.get(state[0], 0) + int(state[1])
fileInput.close()
for candidate in sorted(votes):
    print(candidate, votes[candidate])
