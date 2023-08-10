import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

def bfs(x, y, tx, ty, I):
    direct = [[-2, -1], [-1, -2], [1, -2],
              [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]
    count = [[0 for _ in range(I)] for _ in range(I)]
    queue = deque()
    queue.append([x, y])
    count[x][y] = 0
    while queue:
        x, y = queue.popleft()
        if x == tx and y == ty:
            return count[x][y]
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx > I - 1 or ny < 0 or ny > I - 1:
                continue
            if count[nx][ny] == 0:
                count[nx][ny] = count[x][y] + 1
                queue.append([nx, ny])

def solve():
    I = int(input())
    i, j = map(int, input().split())
    ni, nj = map(int, input().split())
    return bfs(i, j, ni, nj, I)

def main():
    T = int(input())
    for _ in range(T):
        print(solve())

if __name__ == "__main__":
    main()
