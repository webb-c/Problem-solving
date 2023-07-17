# 파이썬 내장함수 round의 특이한 동작과정...

import sys

input = sys.stdin.readline

tier = 0
n = int(input())
if n != 0:
    tierList = [int(input()) for _ in range(n)]
    tierList.sort()
    cutNum = round(n*0.15+0.0000001)
    tierList = tierList[cutNum:n-cutNum]
    tier = round((sum(tierList)/len(tierList))+0.0000001)

print(tier)