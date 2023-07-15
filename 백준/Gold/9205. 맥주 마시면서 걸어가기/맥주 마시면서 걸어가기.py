"""
2023 펜타포드 락 페스티벌 많은 관심 부탁드립니다.
https://pentaport.co.kr/index
"""
import sys
from collections import deque

input = sys.stdin.readline

def get_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def bfs():
    queue = deque()
    queue.append([homeX, homeY])
    result = "sad"
    while queue:
        x, y = queue.popleft()
        if get_distance(x, y, rockX, rockY) <= 1000:
            result = "happy"
            break
        for i in range(n):
            if not visited[i]:
                nx, ny = shopList[i]
                if get_distance(x, y, nx, ny) <= 1000:
                    visited[i] = True
                    queue.append([nx, ny])
    return result

t = int(input())
for _ in range(t):
    n = int(input())
    homeX, homeY = map(int, input().split())
    shopList = [list(map(int, input().split())) for _ in range(n)]
    rockX, rockY = map(int, input().split())
    visited = [False for _ in range(n)]
    print(bfs())