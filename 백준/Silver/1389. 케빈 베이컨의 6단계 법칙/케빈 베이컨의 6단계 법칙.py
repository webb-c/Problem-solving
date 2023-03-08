import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
friend = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M) :
    A, B = map(int, input().split())
    friend[A][B] = friend[B][A] = True

def bfs(v) :
    visited = [v]
    num = [0]*(N+1)
    queue = deque()
    queue.append(v)
    while queue :
        n = queue.popleft()
        visited.append(n)
        for i in range(1, N+1) :
            if i not in visited and friend[n][i]:
                queue.append(i)
                visited.append(i)
                num[i] = num[n] + 1
    return sum(num)

answer = -1
minValue = 999999
for idx in range(1, N+1) :
    term = bfs(idx)
    if term < minValue :
        minValue = term
        answer = idx
print(answer)