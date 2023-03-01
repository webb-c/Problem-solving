import sys
input = sys.stdin.readline

def makeDP(n) :
    DPTable = [1, 2, 4]
    for i in range(3, n) :
        # DP 점화식 (=각 case에 1을 추가 / 2를 추가 / 3을 추가하여 만들 수 있기 때문)
        DPTable.append(DPTable[i-1] + DPTable[i-2] + DPTable[i-3])
    return DPTable

T = int(input())
nList = [ int(input()) for _ in range(T) ]
maxN = max(nList)
DP = makeDP(maxN)
for n in nList :
    print(DP[n-1])