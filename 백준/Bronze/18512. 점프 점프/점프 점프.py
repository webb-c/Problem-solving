import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    X, Y, P1, P2 = map(int, input().split())
    remindList = []
    n = 0
    while True:
        remind = (n*Y + P2 - P1) % X
        if remind == 0:
            result = n*Y + P2
            if result < max(P1, P2):
                remindList = []
            else:
                print(result)
                break
        elif len(remindList) != 0 and remindList[0] == remind:
            print("-1")
            break
        elif len(remindList) == 0 :
            remindList.append(remind)
        n += 1


if __name__ == "__main__":
    main()
