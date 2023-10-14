import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    dist = 0
    initx, inity = map(int, input().split())
    prex, prey = initx, inity
    for _ in range(N-1):
        curx, cury = map(int, input().split())
        dist += (abs(prex - curx) + abs(prey - cury))
        prex, prey = curx, cury
    dist += (abs(prex - initx) + abs(prey - inity))
    print(dist)

if __name__ == "__main__":
    main()
