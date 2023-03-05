import sys
input = sys.stdin.readline

N = int(input())
dotList = list(map(int, input().split()))

setDotList = sorted(set(dotList))
compressSetDotList = {}
compressDotList = []
for idx, dot in enumerate(setDotList) :
    compressSetDotList[dot] = idx
for dot in dotList :
    compressDotList.append(str(compressSetDotList[dot]))
print(' '.join(compressDotList))