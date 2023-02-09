import sys
input = sys.stdin.readline

N = int(input())
numList = [0 for _ in range(100000)]
nameList = [[] for _ in range(100000)]
for _ in range(N) :
    idx, name = input().split()
    numList[int(idx)] += 1
    nameList[int(idx)].append(name)

for idx, n in enumerate(numList) :
    if n != 0 :
        for name in nameList[idx] :
            print(idx, name)