import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nList = list(map(int, input().split()))
nList.sort()
visited = [False]*N
AllResult = []
result = []
def backTracking():
    # 출력 후 백트래킹
    if len(result) == M :
        strResult = ' '.join(map(str, result))
        if strResult not in AllResult :
            AllResult.append(strResult)
        return
    # DFS
    for i in range(N) :
        n = nList[i]
        if n in result and visited[i] : continue
        visited[i] = True
        result.append(n)
        backTracking()
        visited[i] = False
        result.pop()
backTracking()
for result in AllResult : print(result)