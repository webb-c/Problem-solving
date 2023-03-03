import sys
from collections import deque
input = sys.stdin.readline


move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def bfs(arr, x, y):
    queue = deque()
    queue.append([x,y])
    arr[x][y] = False
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx, ny = x+move[i][0], y+move[i][1]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] :
                arr[nx][ny] = False
                queue.append([nx, ny])
    return 1

T = int(input())
for i in range(T) :
    answer = 0
    N, M, K = map(int, input().split())
    farm = [[0]*M for _ in range(N)]
    for _ in range(K) :
        i, j = map(int, input().split())
        farm[i][j] = True
    for i in range(N) :
        for j in range(M) :
            if farm[i][j] :
                answer += bfs(farm, i, j)
    print(answer)