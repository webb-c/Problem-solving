import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

def bfs(x, y, d, graph):
    global N, M
    direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    queue = deque()
    cleaned = [[False for _ in range(M)] for _ in range(N)]
    queue.append([x, y])
    count = 0
    while queue:
        x, y = queue.popleft()
        if not cleaned[x][y]:
            cleaned[x][y] = True  # 1
            count += 1
        flag = False
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if graph[nx][ny] == 0 and not cleaned[nx][ny]:
                flag = True
        if flag:  # 3
            d = (4+d-1) % 4
            dx, dy = direct[d]
            nx, ny = x + dx, y + dy
            if graph[nx][ny] == 0 and not cleaned[nx][ny]:
                queue.append([nx, ny])
            else:
                queue.append([x, y])
        else:  # 2
            dx, dy = direct[d]
            nx, ny = x - dx, y - dy
            if graph[nx][ny] == 1:
                break
            else:
                queue.append([nx, ny])
    return count

def main():
    global N, M
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    print(bfs(r, c, d, graph))

if __name__ == "__main__":
    main()
