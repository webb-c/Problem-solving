import sys
input = sys.stdin.readline

N, M = map(int, input().split())
minN = minM = 100000
idxI = idxJ = -1
for i in range(N-1) :
    n = int(input())
    if n < minN :
        minN = n
        idxI = i+1
jList = list(map(int, input().split()))
for j, m in enumerate(jList) :
    if m < minM :
        minM = m
        idxJ = j+1

r = idxI
c = idxJ
if minM == 0 : r = N
print(r, c)