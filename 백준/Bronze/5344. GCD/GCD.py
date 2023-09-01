import sys

def input():
    return sys.stdin.readline().rstrip()

def get_gcd(a, b):
    if b < a:
        a, b = b, a
    while True:
        if b == 0:
            return a
        r = a % b
        a, b = b, r

def main():
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())
        print(get_gcd(a, b))

if __name__ == "__main__":
    main()
