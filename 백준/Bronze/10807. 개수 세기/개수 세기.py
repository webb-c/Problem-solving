import sys
input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().split()))
v = int(input())
print(numList.count(v))