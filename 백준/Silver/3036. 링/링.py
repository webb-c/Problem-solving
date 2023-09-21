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
    N = int(input())
    rList = list(map(int, input().split()))
    firstR = rList[0]
    for r in rList[1:]:
        gcd = get_gcd(firstR, r)
        print(str(firstR//gcd)+"/"+str(r//gcd))

if __name__ == "__main__":
    main()
