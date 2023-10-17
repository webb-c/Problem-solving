import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    x1, y1, r1 = map(int, input().split())
    x2, y2, r2 = map(int, input().split())
    if abs(x1-x2) >= r1+r2 or abs(y1-y2) >= r1+r2 :
        print("NO")
    elif ((x1-x2)**2 + (y1-y2)**2)**0.5 > r1+r2:
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    main()
