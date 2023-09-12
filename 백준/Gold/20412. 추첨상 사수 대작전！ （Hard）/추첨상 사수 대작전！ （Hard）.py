import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    m, seed, x1, x2 = map(int, input().split())
    if x1 == seed:
        c = x1
        a = (x2-c)*pow(x1, -1, m) % m
    else:
        a = ((x2-x1)*pow(x1-seed, -1, m)) % m
        c = (x1-a*seed) % m
    print(a, c)

if __name__ == "__main__":
    main()
