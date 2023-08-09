import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

def year_later(graph):
    global N, M
    direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    newGraph = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(1, N-1):
        for j in range(1, M-1):
            height = graph[i][j]
            if height != 0:
                for di, dj in direct:
                    if graph[i+di][j+dj] == 0:
                        height -= 1
                newGraph[i][j] = max(0, height)
    return newGraph

def get_segment(graph):
    global N, M
    visited = [[False for _ in range(M)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and not visited[i][j]:
                visited[i][j] = True
                bfs(i, j, graph, visited)
                count += 1
    return count

def bfs(x, y, graph, visited):
    global N, M
    direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        if x == N - 1 and y == M - 1:
            return
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            if graph[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny])

def main():
    global N, M
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    year = 0
    while True:
        year += 1
        graph = year_later(graph)
        segmentNum = get_segment(graph)
        if segmentNum >= 2:
            print(year)
            break
        if segmentNum == 0:
            print("0")
            break

if __name__ == "__main__":
    main()
