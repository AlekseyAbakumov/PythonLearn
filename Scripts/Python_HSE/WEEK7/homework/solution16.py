fileInput = open('input.txt', 'r', encoding='utf8')
wordDict = dict()
for line in fileInput:
    words = line.split()
    for word in words:
        wordDict[word] = wordDict.get(word, 0) + 1
fileInput.close()
newWordsDict = dict()
for wrd in sorted(wordDict, reverse=True):
    newWordsDict[wordDict[wrd]] = wrd
for wrd in sorted(newWordsDict, reverse=True):
    print(newWordsDict[wrd])
    break
