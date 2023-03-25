import sys
input = sys.stdin.readline

A, B = map(int, input().split())
# 역으로 계산 하면 그리디 가능
# B가 홀수인데 마지막 숫자가 1이 아니면 만들 수 없음
# 마지막 숫자가 1이면 거기서 뺌, 아니면 2로 나눔
n = B
answer = 1
while True :
    if n == A :
        print(answer)
        break
    if n < A :
        print(-1)
        break
    if n%2 == 0 :
        n //= 2
    else :
        if str(n)[-1] == '1':
            n = int(str(n)[:-1])
        else :
            print(-1)
            break
    answer += 1