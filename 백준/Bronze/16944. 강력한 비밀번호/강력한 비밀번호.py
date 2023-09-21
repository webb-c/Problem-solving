import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    S = input()
    rule = [1] * 4
    for ch in S:
        if "a" <= ch <= "z":
            rule[0] = 0
        elif "A" <= ch <= "Z":
            rule[1] = 0
        elif ch.isdigit():
            rule[2] = 0
        elif ch in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"]:
            rule[3] = 0
    if len(S) < 6:
        gap = 6-len(S)
        if gap >= sum(rule):
            print(gap)
        else:
            print(sum(rule))
    else:
        print(sum(rule))

if __name__ == "__main__":
    main()
