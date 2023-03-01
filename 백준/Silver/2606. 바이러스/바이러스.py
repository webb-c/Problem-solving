import sys
from collections import deque
input = sys.stdin.readline

V = int(input())
E = int(input())
visited = [ False for _ in range(V) ]
linkList = [ [] for _ in range(V) ]
for _ in range(E) :
    s, e = map(lambda x : int(x)-1, input().split())
    linkList[s].append(e)
    linkList[e].append(s)

visited[0] = True

def bfs(i) :
    count = 0
    queue = deque([i])
    while queue :
        n = queue.popleft()
        link = linkList[n]
        for ni in link :
            if not visited[ni] :
                visited[ni] = True
                queue.append(ni)
                count += 1
    return count
print(bfs(0))