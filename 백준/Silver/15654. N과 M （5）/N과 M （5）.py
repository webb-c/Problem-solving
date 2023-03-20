import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nList = list(map(int, input().split()))
nList.sort()
result = []
def backTracking():
    # 출력 후 백트래킹
    if len(result) == M :
        print(' '.join(map(str, result)))
        return
    # DFS
    for i in range(N) :
        n = nList[i]
        if n in result : continue
        result.append(n)
        backTracking()
        result.pop()
backTracking()