N, K = map(int, input().split())
weightList = []
valueList = []

for i in range(N) :
    w, v = map(int, input().split())
    weightList.append(w)
    valueList.append(v)

DP = [[0 for j in range(K+1)] for i in range(N+1)]

for i in range(N) :
    for j in range(K) :
        value = DP[i][j+1]
        if weightList[i] <= j+1 and value < DP[i][j+1-weightList[i]] + valueList[i] :
            value = DP[i][j+1-weightList[i]] + valueList[i]
        DP[i+1][j+1] = value

print(DP[N][K])