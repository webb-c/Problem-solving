# [Gold 5] 최소 회의실 개수 - 19598 🌟
# 그리디 : 빠른 시작시간 작업 우선배정 (Earliest start time first)
# "시간초과" -> sys이용, list의 min함수가 아니라 heapq 사용

import sys, heapq

n = int(sys.stdin.readline())
meetList = []
for _ in range(n) :
    meetList.append(list(map(int, sys.stdin.readline().split())))
meetList = sorted(meetList)

roomList = []
for start, end in meetList :
    if len(roomList) != 0 and roomList[0] <= start :
        heapq.heappop(roomList)
    heapq.heappush(roomList, end)
print(len(roomList))