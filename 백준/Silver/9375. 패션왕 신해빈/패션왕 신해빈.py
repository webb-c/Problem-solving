import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    clothes = {}
    answer = 1
    N = int(input())
    for _ in range(N) :
        n, k = input().split()
        if k in clothes : clothes[k] += 1
        else : clothes[k] = 1
    for k in clothes :
        answer *= (clothes[k]+1)
    print(answer-1)