import sys
input = sys.stdin.readline

N = int(input())
check = [0 for _ in range(10000)]
for _ in range(N) :
    n = int(input())
    check[n-1]+=1

for idx in range(10000):
    for _ in range(check[idx]):
        print(idx+1)