import sys
input = sys.stdin.readline

numToName = {}
nameToNum = {}
N, M = map(int, input().split())
for i in range(1, N+1) :
    name = input().rstrip()
    numToName[i] = name
    nameToNum[name] = i
for _ in range(M) :
    query = input().rstrip()
    if query.isdigit() :
        query = int(query)
        print(numToName[query])
    else :
        print(nameToNum[query])