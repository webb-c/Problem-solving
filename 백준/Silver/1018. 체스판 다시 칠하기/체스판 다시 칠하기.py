import sys
input = sys.stdin.readline

minSquare = 100
board = []
black = []
N, M = map(int, input().split())
for _ in range(N) :
    board.append(list(input()))
for i in range(N) :
    black.append([])
    for j in range(M) :
        if (i+j)%2==0 :
            if board[i][j] == 'W': black[i].append(1)
            else : black[i].append(0)
        else :
            if board[i][j] == 'W': black[i].append(0)
            else : black[i].append(1)

for iLeft in range(N-7):
    iRight = iLeft+8
    for jUp in range(M-7):
        jDown = jUp+8
        temp1 = 0
        for row in black[iLeft:iRight] :
            for value in row[jUp:jDown] :
                temp1 += value
        temp2 = 64 - temp1
        minSquare = min(minSquare, temp1, temp2)

print(minSquare)