marks = map(int, input().split())
countMarks = [0] * 101
for mark in marks:
    countMarks[mark] += 1
for nowMark in range(101):
    print((str(nowMark) + ' ') * countMarks[nowMark], end='')
