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
    A, B = map(int, input().split())
    gcd = get_gcd(A, B)
    print(''.join(['1']*gcd))

if __name__ == "__main__":
    main()
