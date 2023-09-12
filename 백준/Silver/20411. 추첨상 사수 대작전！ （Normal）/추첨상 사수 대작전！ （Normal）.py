import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    m, seed, x1, x2 = map(int, input().split())
    for a in range(m):
        c = (x1 - a * seed) % m
        if (a * x1 + c) % m == x2:
            print(a, c)
            break

if __name__ == "__main__":
    main()
