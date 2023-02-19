import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    N, M = map(int, input().split())
    prior = deque(list((map(int, input().split()))))
    count = 0
    while prior :
        maxValue = max(prior)
        ret = prior.popleft()
        M -= 1
        if ret == maxValue :
            count += 1
            if M < 0 :
                print(count)
                break
        else :
            prior.append(ret)
            if M < 0 : M = len(prior) - 1