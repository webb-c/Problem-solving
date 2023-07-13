import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
visited = [False for _ in range(F+1)]
count = [0 for _ in range(F+1)]
direct = [U, -1*D]


def bfs(start):
    visited[start] = True
    queue = deque()
    queue.append(start)
    result = "use the stairs"
    while queue:
        x = queue.popleft()
        if x == G:
            result = count[x]
            break
        for w in direct:
            nx = x + w
            if nx < 1 or nx > F:
                continue
            if not visited[nx]:
                visited[nx] = True
                count[nx] = count[x] + 1
                queue.append(nx)
    return result


print(bfs(S))