import sys
from collections import deque
input = sys.stdin.readline
size = 100000

N, K = map(int, input().split())
visited = [False for _ in range(size+1)]
timeList = [0 for _ in range(size+1)]


def bfs():
    queue = deque()
    queue.append(N)
    while queue:
        u = queue.popleft()
        # actions = [2*u, u+1, u-1]
        actions = [2*u, u-1, u+1]
        if u == K:
            return timeList[u]
        for v in actions:
            if v < 0 or size < v:
                continue
            if not visited[v]:
                visited[v] = True
                if v == 2*u:
                    if v == 0:
                        continue
                    timeList[v] = timeList[u]
                    queue.appendleft(v)  # 우선순위
                else:
                    timeList[v] = timeList[u]+1
                    queue.append(v)
    return -1


print(bfs())
