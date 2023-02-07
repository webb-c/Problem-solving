import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
house = []
chick = []
for r in range(N) :
    line = input().split()
    for c, box in enumerate(line) :
        if box == "1" : house.append([r, c])
        elif box == "2" : chick.append([r, c])

# 가능한 모든 조합 확인
result = 999999999
for com in combinations(chick, M) :
    chickDist = 0
    for h in house :
        minDist = 99999
        for ch in com :
            dist = abs(h[0] - ch[0]) + abs(h[1] - ch[1])
            if minDist > dist : minDist = dist
        chickDist += minDist
    if result > chickDist : result = chickDist

print(result)