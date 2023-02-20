import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
groundList = []
minTime = 999999999
maxHeight = 0
for _ in range(N):
    groundList.append(list(map(int, input().split())))

for h in range(257):
    block = B
    time = 0
    for i in range(N):
        for j in range(M):
            gap = abs(h - groundList[i][j])
            if groundList[i][j] < h :
                block -= gap
                time += gap
            elif groundList[i][j] > h :
                block += gap
                time += 2*gap
    if block < 0: break
    if time <= minTime :
        minTime = time
        maxHeight = h

print(minTime, maxHeight)