import sys
input = sys.stdin.readline

T = int(input())
answer = "NO"
for _ in range(T):
    string = list(input())
    stack = []
    for ch in string:
        if ch == '\n': break
        if ch == '(' : stack.append(ch)
        else :
            if stack : stack.pop()
            else :
                stack.append(ch)
                break
    if len(stack) == 0 : answer = "YES"
    else : answer = "NO"
    print(answer)