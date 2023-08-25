import sys

def input():
    return sys.stdin.readline().rstrip()

def get_gcd(a, b):
    while True:
        if b == 0:
            return a
        r = a % b
        a, b = b, r

def get_lcm(a, b):
    gcd = get_gcd(a, b)
    return a*b // gcd

def main():
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        print(get_lcm(A, B))

if __name__ == "__main__":
    main()
