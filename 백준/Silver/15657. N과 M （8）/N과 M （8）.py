import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nList = list(map(int, input().split()))
nList.sort()
result = []

def backTracking(index):
    # 출력 후 백트래킹
    if len(result) == M :
        print(' '.join(map(str, result)))
        return
    # DFS
    check = 0
    for i in range(index, N) :
        n = nList[i]
        if check == n : continue
        result.append(n)
        check = nList[i]
        backTracking(i)
        result.pop()
backTracking(0)