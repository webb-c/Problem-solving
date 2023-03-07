import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
dist = [0] * 100001
def bfs() :
    queue = deque()
    queue.append(N)
    while queue :
        x = queue.popleft()
        if x == K: return dist[x]
        move = [x-1, x+1, x*2]
        for nx in move :
            if 0 <= nx <= 100000 and not dist[nx] :
                dist[nx] = dist[x]+1
                queue.append(nx)
print(bfs())