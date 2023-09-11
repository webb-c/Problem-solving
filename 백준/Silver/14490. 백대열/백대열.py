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
    n, m = map(int, input().split(":"))
    r = get_gcd(n, m)
    print(str(n//r)+":"+str(m//r))

if __name__ == "__main__":
    main()
