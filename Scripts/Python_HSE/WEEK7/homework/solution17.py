fileInput = open('input.txt', 'r', encoding='utf-8')
wordDict = dict()
for line in fileInput:
    words = line.split()
    for word in words:
        wordDict[word] = wordDict.get(word, 0) + 1
fileInput.close()
for word in sorted(wordDict, key=lambda wrd: (-wordDict[wrd], wrd)):
    print(word)
