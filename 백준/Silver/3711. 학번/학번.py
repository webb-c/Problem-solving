import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(G, numList):
    if G == 1:
        return 1
    else:
        m = 0
        while True:
            m += 1
            if len({i % m for i in numList}) == G:
                return m

def main():
    N = int(input())
    for _ in range(N):
        G = int(input())
        numList = [int(input()) for _ in range(G)]
        print(solve(G, numList))

if __name__ == "__main__":
    main()
