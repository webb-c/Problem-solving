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
    numList = list(map(int, input().split()))
    numerator = 0
    divider = 1
    for i in range(N):
        divider *= numList[i]
    for i in range(N):
        n = numList[i]
        temp = divider // n
        numerator += temp
    gcd = get_gcd(numerator, divider)
    print(str(divider//gcd)+"/"+str(numerator//gcd))

if __name__ == "__main__":
    main()
