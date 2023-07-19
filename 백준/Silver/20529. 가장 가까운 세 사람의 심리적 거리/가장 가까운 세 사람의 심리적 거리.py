import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    mbtiList = list(map(str, input().split()))
    minDist = float("inf")
    if N > 32:
        minDist = 0
    else:
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if i == j or j == k or i == k:
                        continue
                    dist = 0
                    for ch in range(4):
                        if mbtiList[i][ch] != mbtiList[j][ch]:
                            dist += 1
                        if mbtiList[j][ch] != mbtiList[k][ch]:
                            dist += 1
                        if mbtiList[k][ch] != mbtiList[i][ch]:
                            dist += 1
                    minDist = min(minDist, dist)
    print(minDist)
