import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [ list(map(int, list(input().split()))) for _ in range(N) ]
maxValue = max(map(max, board))
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visited = [[False]*M for _ in range(N)]

def dfs(x, y, step, value) :
    global answer
    if value+maxValue*(4-step) <= answer : return
    if step == 4 :
        answer = max(answer, value)
        return
    for i in range(4) :
        nx, ny = x+move[i][0], y+move[i][1]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] :
            if step == 2 : # ㅗ 모양 (원 위치에서 탐색)
                visited[nx][ny] = True
                dfs(x, y, step+1, value+board[nx][ny])
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx, ny, step+1, value+board[nx][ny])
            visited[nx][ny] = False

answer = 0
for i in range(N) :
    for j in range(M) :
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
print(answer)