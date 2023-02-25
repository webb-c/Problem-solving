import sys
input = sys.stdin.readline

N = int(input())
pList = list(map(int, input().split()))
pList.sort(reverse=True)
result = 0
for i, p in enumerate(pList):
    result += (i+1)*p
print(result)