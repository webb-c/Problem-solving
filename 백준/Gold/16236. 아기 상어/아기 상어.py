import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]

move = [[-1, 0], [0, -1], [0, 1], [1, 0]]
def bfs(x, y, size):
    queue = deque()
    queue.append((x, y))
    visited = set()
    visited.add((x, y))
    dist = [[-1] * N for _ in range(N)]
    dist[x][y] = 0
    fish = []
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+move[i][0], y+move[i][1]
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                visited.add((nx, ny))
                if sea[nx][ny] == 0 or sea[nx][ny] == size:
                    queue.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
                elif sea[nx][ny] < size:
                    queue.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
                    fish.append((dist[nx][ny], nx, ny))
    if not fish: return None
    else:
        fish.sort()
        return fish[0]
#main
shark_size = 2
shark_x, shark_y = 0, 0
eat_count = 0
time = 0
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            shark_x, shark_y = i, j
            sea[i][j] = 0
            break
while True:
    result = bfs(shark_x, shark_y, shark_size)
    if result is None: break

    dist, fish_x, fish_y = result
    eat_count += 1
    sea[fish_x][fish_y] = 0
    shark_x, shark_y = fish_x, fish_y
    if eat_count == shark_size:
        shark_size += 1
        eat_count = 0
    time += dist
print(time)
