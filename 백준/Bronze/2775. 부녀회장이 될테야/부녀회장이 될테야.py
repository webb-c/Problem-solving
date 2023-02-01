import sys
input = sys.stdin.readline
T = int(input())
testList = []
kMax = 0
nMax = 0
for _ in range(T):
    k = int(input())
    n = int(input())
    if k > kMax : kMax = k
    if n > nMax : nMax = n
    testList.append((k, n))

table = []
for i in range(kMax+1):
    table.append([])
    for j in range(nMax):
        if i == 0 : table[i].append(j+1)
        else :
            if j == 0 : table[i].append(1)
            else : table[i].append(table[i-1][j] + table[i][j-1])

for k, n in testList :
    print(table[k][n-1])