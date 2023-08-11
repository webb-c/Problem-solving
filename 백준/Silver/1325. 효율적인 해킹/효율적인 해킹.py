import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

def bfs(u, graph, visited):
    count = 1
    queue = deque([u])
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                count += 1
                visited[v] = True
                queue.append(v)
    return count

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        A, B = map(int, input().split())
        graph[B].append(A)
    maxCount = 1
    comList = []
    for start in range(1, N+1):
        visited = [False for _ in range(N+1)]
        visited[start] = True
        count = bfs(start, graph, visited)
        if count > maxCount:
            comList = []
            maxCount = count
        if count == maxCount:
            comList.append(start)
    print(*comList)

if __name__ == "__main__":
    main()
