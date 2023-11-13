import sys

def input():
    return sys.stdin.readline().rstrip()

def is_prime(n):
    isPrime = True
    if n < 2:
        isPrime = False
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                isPrime = False
                break
            i += 1
    return isPrime

def get_pow_with_mod(C, n, mod):
    if n == 0:
        return 1
    if n == 1:
        return C % mod
    temp = get_pow_with_mod(C, n // 2, mod)
    if n % 2 == 1:
        return (temp * temp * C) % mod
    else:
        return (temp * temp) % mod

def solve():
    while True:
        p, a = map(int, input().split())
        if p == 0:
            break
        if is_prime(p):
            print("no")
            continue
        if get_pow_with_mod(a, p, p) == a:
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    solve()
