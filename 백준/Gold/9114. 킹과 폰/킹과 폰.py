# [Gold 3] 킹과 폰 - 9114
import sys
input = sys.stdin.readline

def getddPos(x, y, fPos):
    ddPos = []
    if 0 < y-1 :
        if (0 < x-1) and ((x-1, y-1) not in fPos) :
            ddPos.append((x-1, y-1))
        if (x+1 < 9) and ((x+1, y-1) not in fPos) :
            ddPos.append((x+1, y-1))
    return ddPos

def simulate(xk, yk, xp, yp, dPos, fPos):
    white = False
    # *킹*
    # 킹의 후보 포지션 확인
    canList = []
    ddPos = getddPos(xp, yp, fPos)
    banList = fPos + dPos + ddPos
    for y in range(yk - 1, yk + 2):
        if y < 1 or y > 8: continue
        for x in range(xk - 1, xk + 2):
            if x < 1 or x > 8: continue
            if x == xk and y == yk: continue
            if (x, y) not in banList: canList.append((x, y))
    # 종료조건
    if len(canList) == 0 : return white
    # 킹의 움직임 (완전 탐색)
    for (x, y) in canList:
        xk_ = x
        yk_ = y
        # 킹의 승리조건 1
        if xk_ == xp and yk_ == yp : white = True
        # *폰*
        # 킹의 승리조건 2
        if ((xp, yp - 1) in fPos) or (xp == xk_ and yp - 1 == yk_) : white = True
        if white: break
        else :
            if yp - 1 == 0 :
                continue
            white = simulate(xk_, yk_, xp, yp-1, dPos, fPos)
    return white

n = int(input())
winnerList = []
for _ in range(n):
    # 입력 받기
    dPos = []
    fPos = []
    for i in range(8):
        line = input()
        for j, ch in enumerate(line) :
            if ch == 'D' :
                dPos.append((j+1, 8-i))
            elif ch == 'F' :
                fPos.append((j+1, 8-i))
    xk, yk = map(int, input().split()) # white
    xp, yp = map(int, input().split()) # black
    ddPos = getddPos(xp, yp, fPos)
    # 테스트 수행
    ret = simulate(xk, yk, xp, yp, dPos, fPos)
    if ret : winnerList.append("White")
    else : winnerList.append("Black")

# 승자 출력
for winner in winnerList :
    print(winner)