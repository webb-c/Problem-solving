import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    x, y = map(int, input().split())
    max_x, min_x = x, x
    max_y, min_y = y, y
    for _ in range(n-1):
        x, y = map(int, input().split())
        max_x = max(max_x, x)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        min_y = min(min_y, y)
    print((max_x - min_x) * (max_y - min_y))

if __name__ == "__main__":
    main()
