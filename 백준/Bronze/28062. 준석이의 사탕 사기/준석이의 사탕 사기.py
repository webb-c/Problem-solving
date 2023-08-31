import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    candyList = list(map(int, input().split()))
    candyList.sort()
    if N == 1:
        if candyList[0] % 2 != 0:
            print(0)
        else:
            print(candyList[0])
    else:
        result = sum(candyList)
        if result % 2 != 0:
            for c in candyList:
                if c % 2 != 0:
                    result -= c
                    print(result)
                    break
        else:
            print(result)

if __name__ == "__main__":
    main()
