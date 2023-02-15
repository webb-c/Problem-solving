import sys
input = sys.stdin.readline

S = input()
answer = 0
count = 0
for ch in S :
    if ch == '[' : count += 3
    elif ch == '{' : count += 2
    elif ch == '(' : count += 1
    elif ch == ')' : count -= 1
    elif ch == '}' : count -= 2
    elif ch == ']' : count -= 3
    else :
        if count > answer :
            answer = count
print(answer)