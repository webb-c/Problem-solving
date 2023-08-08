from sys import stdin
input = stdin.readline

numList = []
for _ in range(5):
    n = int(input())
    if n in numList:
        idx = numList.index(n)
        numList.pop(idx)
    else:
        numList.append(n)

print(numList[0])