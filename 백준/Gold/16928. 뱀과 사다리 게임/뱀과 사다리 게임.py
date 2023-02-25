from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False] * 101
board = [0] * 101
move = {}
for _ in range(N+M) :
    s, e = map(int, input().split())
    move[s] = e

def bfs(i):
    queue = deque([i])
    while queue :
        x = queue.popleft()
        if x == 100 : break
        for dice in range(1, 7):
            nx = x+dice
            if nx < 101 :
                if nx in move.keys() : nx = move[nx] # 사다리 & 뱀
                if not visited[nx] :
                    visited[nx] = True
                    board[nx] = board[x] + 1
                    queue.append(nx)

bfs(1)
print(board[100])
