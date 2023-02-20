import sys
input = sys.stdin.readline

N, M = map(int, input().split())
treeList = list(map(int, input().split()))

minHeight = 0
maxHeight = max(treeList)
while True :
    H = (minHeight + maxHeight) // 2
    heightSum = 0
    for i in range(N) :
        heightSum += max((treeList[i] - H), 0)
    if heightSum >= M : minHeight = H+1
    else : maxHeight = H-1
    if minHeight > maxHeight : break

print(maxHeight)