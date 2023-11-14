import sys
import math

def input():
    return sys.stdin.readline().rstrip()

def get_gcd(a, b):
    while True:
        if b == 0:
            return a
        r = a % b
        a, b = b, r

def extend_euclid(a, b):
    if b == 0: return (1, 0)
    s, t = extend_euclid(b, a % b)
    temp = t
    t = s - (a // b) * t
    s = temp
    if s <= 0:
        s += b
        t -= a
    return (s, t)

def get_mod_inverse(a, mod):
    if get_gcd(a, mod) != 1:
        return -1
    else:
        s, t = extend_euclid(a, mod)
        return s

def solve():
    n, a = map(int, input().split())
    reverse_plus = n - a
    reverse_mul = get_mod_inverse(a, n)
    print(reverse_plus, reverse_mul)


if __name__ == "__main__":
    solve()
