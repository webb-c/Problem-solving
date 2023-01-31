# [Silver 1] 튜터-튜티 관계의 수
# 서로 친분이 있는 사람끼리 엣지로 연결을 한다.
# 친분이 아예 존재하지 않는다면 서로 다른 연결 그래프에 속할 것이다.
# 하나의 연결그래프는 그 그래프를 구성하는 하나의 노드로부터 다른 모든 노드에 방문할 수 있다.
# 따라서,
# - 최소로 전달해야하는 사람의 수 : 연결그래프의 수
# 시간초과... -> 하나하나 비교하지 말고 친분관계를 받아둔 다음 그래프 탐색

import sys
import collections
input = sys.stdin.readline

def search(n, graph, visit):
    cnt = 1
    visit[n] = True
    notVisit = collections.deque([n]) # 시작노드가 n인 미방문 큐
    # 미방문이 존재하는 경우 반복
    while notVisit :
        current = notVisit.pop()
        for next in graph[current]:
            if visit[next] : continue
            visit[next] = True
            notVisit.append(next)
            cnt += 1
    return cnt

count = 1
MOD = 1000000007
N, M = map(int, input().split())
graphDict = collections.defaultdict(list) # 자료형 지정
visitList = [False for _ in range(N+1)]

for _ in range(M) :
    u, v = map(int, input().split())
    graphDict[u].append(v) # 양방향
    graphDict[v].append(u)

for n in range(1, N+1):
    if not visitList[n] :
        count *= search(n, graphDict, visitList)

print(count%MOD)