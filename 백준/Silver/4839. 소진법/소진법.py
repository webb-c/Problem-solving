import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(n):
    nOrigin = n
    global primeList
    result = []
    pos = 0
    while n > 1:
        p = 1
        for i in range(10):
            p *= primeList[i]
            if p > n:
                break
        p //= primeList[i]
        a = n // p
        n %= p
        result.append([a])
        result[-1].extend(primeList[:i])
        pos += 1
    if n == 1:
        result.append([n])
    result.reverse()

    print(nOrigin, "= ", end="")
    for i, pList in enumerate(result):
        if 0 < i:
            print(" + ", end="")
        for j, p in enumerate(pList):
            print(p, end="")
            if j != len(pList)-1:
                print("*", end="")
    print()

def main():
    global primeList
    primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            solve(n)

if __name__ == "__main__":
    main()
