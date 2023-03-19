import sys
input = sys.stdin.readline

#UNION-FIND
def find(lst, x):
    if lst[x] != x:
        lst[x] = find(lst, lst[x])
    return lst[x]

def union(lst, a, b):
    a = find(lst, a)
    b = find(lst, b)
    if a < b: lst[b] = a
    else: lst[a] = b

N = int(input())
planetList = [list(map(int, input().split()))+[i] for i in range(N)]
edgeList = []
# 메모리 초과 수정
for axis in range(3) :
    planetList.sort(key=lambda v : v[axis])
    for i in range(1, N) :
        edgeList.append([planetList[i-1][3], planetList[i][3], abs(planetList[i][axis]-planetList[i-1][axis])])
edgeList.sort(key=lambda v : v[2]) # dist 기준 정렬

result = 0
tree = [i for i in range(N)]
for a, b, weight in edgeList :
    if find(tree, a) != find(tree, b) :
        union(tree, a, b)
        result += weight
print(result)