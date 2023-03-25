import sys
input = sys.stdin.readline

N = int(input())
starList = [[' ']*2*N for _ in range(N)]

def drawStar(N, i, j) :
    if N == 3:
        starList[i][j] = '*'
        for di in range(1, 3) :
            for dj in range(-di, di+1) :
                starList[i+di][j+dj] = '*'
        starList[i+1][j] = ' '
    else :
        newN = N//2
        drawStar(newN, i, j)
        drawStar(newN, i+newN, j-newN) #왼쪽
        drawStar(newN, i+newN, j+newN) #오른쪽

drawStar(N, 0, N-1)
for star in starList :
    print("".join(star))