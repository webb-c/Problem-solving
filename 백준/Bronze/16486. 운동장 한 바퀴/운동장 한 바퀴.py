import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    PI = 3.141592
    d1 = int(input())
    d2 = int(input())
    print(2*d1 + 2*PI*d2)

if __name__ == "__main__":
    main()
