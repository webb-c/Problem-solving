from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    p = list(input().rstrip())
    n = int(input())
    numList = deque(input().rstrip()[1:-1].split(","))
    if n == 0 : numList = deque()
    rev = 0
    IsError = False
    for cmd in p :
        if cmd == 'R' : rev += 1
        else :
            if len(numList) == 0 :
                IsError = True
                break
            else :
                if rev%2 == 0 : numList.popleft()
                else : numList.pop()
    if not IsError :
        if rev % 2 != 0 : numList.reverse()
        print("["+",".join(numList)+"]")
    else : print("error")