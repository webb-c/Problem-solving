import sys

def input():
    return sys.stdin.readline().rstrip()


def solve():
    string = list(input())
    stack = []
    lazer = False
    sum_parts = 0
    for ch in string:
        if ch == '(':
            stack.append(ch)
            lazer = True
        else:
            stack.pop()
            if lazer:
                sum_parts += len(stack)
            else:
                sum_parts += 1
            lazer = False
    
    print(sum_parts)
    
if __name__ == "__main__":
    solve()
    