import sys

def input(): return sys.stdin.readline().rstrip()

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return (gcd, x, y)

def factorize(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return i, n // i

def solve(n, e):
    p, q = factorize(n)
    phi = (p-1) * (q-1)
    _, x, _ = extended_gcd(e, phi)
    d = x % phi
    return d

def main():
    T = int(input())
    for _ in range(T):
        n, e = map(int, input().split())
        print(solve(n, e))


if __name__ == "__main__":
    main()
