import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []
def backTracking(indexA):
    # 출력 후 백트래킹
    if len(result) == M :
        print(' '.join(map(str, result)))
        return
    # DFS
    for i in range(indexA, N+1) :
        if i in result : continue
        result.append(i)
        backTracking(i)
        result.pop()
backTracking(1)