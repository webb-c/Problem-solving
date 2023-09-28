import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    n = input()
    nList = list(map(int, list(n)))
    if 0 in nList and sum(nList) % 3 == 0:
        nList.sort()
        result = 0
        i = 1
        for n in nList:
            result += i*n
            i *= 10
        print(result)
    else:
        print(-1)

if __name__ == "__main__":
    main()
