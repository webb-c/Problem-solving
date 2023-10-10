import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    T = int(input())
    for _ in range(T):
        V, E = map(int, input().split())
        print(2 - (V - E))

if __name__ == "__main__":
    main()
