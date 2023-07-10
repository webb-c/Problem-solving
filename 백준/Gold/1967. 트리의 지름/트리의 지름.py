"""
그래프 탐색 [최장 경로]
- 각각의 리프 노드에 대해 dfs 해서 최장거리 저장?
- 루트 기준 가장 멀리 떨어진 노드 2개, 같은 경로 겹치면 그 가중치 제거 -> 제거가 어려움
- 임의의 노드 기준 가장 멀리 떨어진 노드 => 그 노드에서 가장 멀리 떨어진 노드
    *왜 되는가?
    가설) 어떤 노드에서 가장 멀리 떨어진 노드는 항상 트리의 지름을 이루는 두 노드 중 하나가 된다.
    증명) 귀류법 : 가장 단순한 트리구조에서 가장 멀리 떨어진 노드를 포함하지 않으면서 지름을 만드는 경우에 대해 모두 모순임을 보이면된다.
    이후 더 큰 형태의 트리는 각각의 서브트리를 노드로 보고 증명할 수 있기 때문
"""
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)  # 재귀제약

n = int(input())
tree = [[] for _ in range(n+1)]

def get_diameter():
    dist = [0 for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    visited[1] = True
    dfs(1, dist, visited)

    u = dist.index(max(dist))
    dist = [0 for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    visited[u] = True
    dfs(u, dist, visited)
    return max(dist)

# u번째 노드에 대한 dfs
def dfs(u, dist, visited):
    for v, w in tree[u]:
        if not visited[v]:
            dist[v] = dist[u] + w
            visited[v] = True
            dfs(v, dist, visited)

for _ in range(n-1):
    p, c, w = map(int, input().split())
    tree[p].append([c, w])
    tree[c].append([p, w])
print(get_diameter())
