import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
maze = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[False for _ in range(M)] for __ in range(N)]
visited[0][0] = True

def bfs(x, y) :
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+move[i][0], y+move[i][1]
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[N-1][M-1]

print(bfs(0, 0))