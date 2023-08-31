import sys

def input():
    return sys.stdin.readline().rstrip()

def is_prime(n):
    isPrime = True
    if n < 2:
        isPrime = False
    else:
        for p in range(2, int(n**0.5)+1):
            if n % p == 0:
                isPrime = False
    return isPrime

def main():
    oriNum, add = map(int, input().split())
    newNum = oriNum + 1000000*add
    if is_prime(oriNum) and is_prime(newNum):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
