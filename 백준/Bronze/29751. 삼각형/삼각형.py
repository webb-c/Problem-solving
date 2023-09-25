import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    W, H = map(int, input().split())
    print(H*W*0.5)

if __name__ == "__main__":
    main()
