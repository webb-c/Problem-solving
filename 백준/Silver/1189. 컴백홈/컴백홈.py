import sys

def input(): return sys.stdin.readline().rstrip()

def backtracking(x, y, k, graph):
    global R, C, K, count
    if k == K and x == 0 and y == C-1:
        count += 1
    else:
        graph[x][y] = "T"
        direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != "T":
                graph[nx][ny] = "T"
                backtracking(nx, ny, k+1, graph)
                graph[nx][ny] = "."

def main():
    global R, C, K, count
    R, C, K = map(int, input().split())
    graph = [list(input()) for _ in range(R)]
    count = 0
    backtracking(R-1, 0, 1, graph)
    print(count)

if __name__ == "__main__":
    main()
