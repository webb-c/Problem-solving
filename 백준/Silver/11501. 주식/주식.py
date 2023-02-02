import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    N = int(input())
    moneyList = list(map(int, input().split()))
    high = total = 0
    for m in moneyList[::-1] :
        if high < m : high = m
        else : total = total + (high - m)
    print(total)