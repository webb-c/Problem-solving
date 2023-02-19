import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
mIdx = N//2
numList = []
for _ in range(N) :
    numList.append(int(input()))
numList.sort()

print(round(sum(numList) / N))
print(numList[mIdx])
frequent = Counter(numList).most_common()
if len(frequent) > 1 and frequent[0][1] == frequent[1][1] : print(frequent[1][0])
else : print(frequent[0][0])
print(max(numList) - min(numList))