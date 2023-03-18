import sys
from collections import deque
input = sys.stdin.readline

# 그래프 탐색으로 풀어야지! 라고 아이디어를 떠올리기 어려운 문제...
MAXNUM = 10000
operList = ["D", "S", "L", "R"]
T = int(input())
for _ in range(T) :
    A, B = map(int, input().split())
    visit = [False] * MAXNUM
    queue = deque()
    visit[A] = True
    queue.append([A, []])
    while queue :
        n, order = queue.popleft()
        if n == B :
            print("".join(order))
            break
        for i in range(4):
            oper = operList[i]
            if oper == "D" : newN = (2*n)%MAXNUM
            elif oper == "S" : newN = (n-1)%MAXNUM
            elif oper == "L" : newN = (10*n+(n//1000))%MAXNUM
            else : newN = (n//10+(n%10)*1000)%MAXNUM
            if not visit[newN] :
                visit[newN] = True
                queue.append([newN, order+[oper]])