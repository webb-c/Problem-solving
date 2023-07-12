"""
BFS인데 1이었던 곳을 한번 지나가면 그 뒤에는 1을 지나갈 수 없도록 로직을 짜면 되나?
가능한 벽에 대해서 모두 테스트하면 시간복잡도가 오버됨
bfs 돌면서 한번에 확인하려면 visited로 해당 위치에 갔었는지 확인할 때, 이미 벽을 부섰는지 아닌지를 추가로 확인

"""
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, list(input().strip()))) for _ in range(N)]
# visited[x][y][0] 이면 아직 벽을 안 부숨, visited[x][y][1] 이면 벽을 부순 경우에 이동횟수
visited = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def bfs(x, y, wall):
    queue = deque()
    queue.append([x, y, wall])
    while queue:
        x, y, wall = queue.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][wall]
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            # 파괴 가능한 벽 -> 아직 방문 하지 않은게 보장 되는 상태
            if graph[nx][ny] == 1 and wall == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append([nx, ny, 1])
            # 벽이 아니고 방문 안한 상태
            elif graph[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                visited[nx][ny][wall] = visited[x][y][wall] + 1
                queue.append([nx, ny, wall])
    return -1


print(bfs(0, 0, 0))
