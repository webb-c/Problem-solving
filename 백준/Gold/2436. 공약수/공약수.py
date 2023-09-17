import sys

def input():
    return sys.stdin.readline().rstrip()

def get_gcd(a, b):
    while True:
        if b == 0:
            return a
        r = a % b
        a, b = b, r

def main():
    gcd, lcm = map(int, input().split())
    # ab = lcm * gcd
    a_b_ = lcm // gcd
    a_, b_ = 1, a_b_
    for i in range(1, a_b_//2 + 1):
        if a_b_ % i != 0:
            continue
        a_temp = i
        b_temp = a_b_ // i
        if get_gcd(a_temp, b_temp) != 1:
            continue
        if a_temp + b_temp < a_+b_:
            a_, b_ = a_temp, b_temp
    a, b = a_*gcd, b_*gcd
    print(a, b)

if __name__ == "__main__":
    main()
