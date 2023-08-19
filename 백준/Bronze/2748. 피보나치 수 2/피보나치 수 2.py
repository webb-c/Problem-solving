import sys

def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())

    if n == 1:
        print(1)
    else:
        a = 0
        b = 1
        for _ in range(n-1):
            c = a + b
            a = b
            b = c

        print(b)


if __name__ == "__main__":
    main()
