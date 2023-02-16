import sys
from collections import deque
input = sys.stdin.readline

string = "init"
while True :
    string = input()
    if string[0] == '.' : break
    temp = deque([])
    flag = "yes"
    for ch in string :
        if ch == "\n" : break
        if ch == "(" : temp.append("(")
        elif ch == "[" : temp.append("[")
        elif ch == ")" or ch == "]":
            if not temp :
                flag = "no"
                break
            ch2 = temp.pop()
            if (ch == ")" and ch2 != "(") or (ch == "]" and ch2 != "["):
                flag = "no"
                break
        else : continue
    if temp : flag = "no"
    print(flag)