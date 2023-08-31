import sys

def input():
    return sys.stdin.readline().rstrip()

def get_surplus_reciprocal(a, m):
    i = 0
    while True:
        if (i*m+1) % a == 0:
            return (i*m+1) // a
        i += 1

def main():
    a, m = map(int, input().split())
    print(get_surplus_reciprocal(a, m))

if __name__ == "__main__":
    main()
