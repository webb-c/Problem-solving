import sys

def input():
    return sys.stdin.readline().rstrip()

def get_gcd(a, b):
    while True:
        if b == 0:
            return a
        r = a % b
        a, b = b, r

def multi_get_gcd(numList):
    a = numList[0]
    for i in range(1, len(numList)):
        a = get_gcd(a, numList[i])
    return a

def main():
    N = int(input())
    gapList = []
    prev = int(input())
    for _ in range(N-1):
        cur = int(input())
        gapList.append(cur - prev)
        prev = cur
    gcd = multi_get_gcd(gapList)
    result = 0
    for gap in gapList:
        result += gap // gcd - 1
    print(result)

if __name__ == "__main__":
    main()
