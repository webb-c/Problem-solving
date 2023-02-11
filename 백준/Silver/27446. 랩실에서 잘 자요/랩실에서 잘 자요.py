import sys
input = sys.stdin.readline

N, M = map(int, input().split())
okList = list(map(int, input().split()))
noList = []
inkList = []
for no in range(1, N+1):
    if no not in okList : noList.append(no)
lenNo = len(noList)
for i in range(lenNo) :
    inkList.append([])
    for j in range(lenNo) :
        if j >= i : inkList[i].append(5+(noList[j]-noList[i]+1)*2)
        else : inkList[i].append(0)

for L in range(1, lenNo) :
    for i in range(lenNo-L) :
        j = i+L
        for k in range(i, j) :
            temp = inkList[i][k] + inkList[k+1][j]
            if temp < inkList[i][j] : inkList[i][j] = temp
if lenNo > 0 :
    print(inkList[0][lenNo-1])
else :
    print(0)