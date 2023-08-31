import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(a, b):
    ab = a*b
    gcd = 0
    while True:
        if b == 0:
            gcd = a
            break
        r = a % b
        a, b = b, r
    lcm = ab // gcd
    return [lcm, gcd]

def main():
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())
        print(*solve(a, b))

if __name__ == "__main__":
    main()
