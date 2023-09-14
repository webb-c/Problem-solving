import sys

def input():
    return sys.stdin.readline().rstrip()

def get_gcd(a, b):
    while True:
        if b == 0:
            return a
        r = a % b
        a, b = b, r

def solve(A, B, X):
    gcd = get_gcd(A, B)
    return X // gcd

def main():
    T = int(input())
    for _ in range(T):
        A, B, X = map(int, input().split())
        print(solve(A, B, X))

if __name__ == "__main__":
    main()
