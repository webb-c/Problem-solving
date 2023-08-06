from sys import stdin
input = stdin.readline

equation = list(input().strip())
priority1 = ["+", "-", "*", "/"]
priority2 = ["*", "/"]
stack = []
postfix = ""

for ch in equation:
    if ch.isalpha():
        postfix += ch
    else:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            while stack and stack[-1] != "(":
                postfix += stack.pop()
            stack.pop()
        elif ch == "*" or ch == "/":
            if not stack:
                stack.append(ch)
            else:
                while stack and stack[-1] in priority2:
                    postfix += stack.pop()
                stack.append(ch)
        elif ch == "+" or ch == "-":
            if not stack:
                stack.append(ch)
            else:
                while stack and stack[-1] in priority1:
                    postfix += stack.pop()
                stack.append(ch)
while stack:
    postfix += stack.pop()

print(postfix)