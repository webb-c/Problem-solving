import sys
input = sys.stdin.readline

N = int(input())
fac = 1
for i in range(1, N+1) :
    fac *= i
facStr = list(str(fac))
for idx, ch in enumerate(reversed(facStr)) :
    if ch != '0' :
        print(idx)
        break