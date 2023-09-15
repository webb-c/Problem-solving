import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(a, b):
    if b % a == 0 and b // a > 1:
        return 1
    return 0

def main():
    Q = int(input())
    for _ in range(Q):
        a, b = map(int, input().split())
        print(solve(a, b))

if __name__ == "__main__":
    main()
