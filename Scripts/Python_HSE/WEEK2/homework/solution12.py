startRow = int(input())
startLine = int(input())
endRow = int(input())
endLine = int(input())
if endLine - startLine < 1 \
        or endLine > 8 or startLine > 8 or startRow > 8 or endRow > 8 \
        or startLine < 1 or startRow < 1:
    print('NO')
else:
    if (startRow + startLine) % 2 == 0:
        cell1IsBlack = True
    else:
        cell1IsBlack = False
    if (endRow + endLine) % 2 == 0:
        cell2IsBlack = True
    else:
        cell2IsBlack = False
    if cell1IsBlack == cell2IsBlack:
        print('YES')
    else:
        print('NO')
