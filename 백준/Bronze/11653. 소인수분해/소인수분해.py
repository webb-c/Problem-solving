import sys

def input():
    return sys.stdin.readline().rstrip()

def find_prime(n):
    if n == 1:
        return []
    elif n == 2:
        return [n]
    for i in range(2, n):
        if n % i == 0:
            ret1 = find_prime(i)
            ret2 = find_prime(int(n/i))
            return ret1 + ret2
    return [n]

def main():
    N = int(input())
    primeList = find_prime(N)
    for p in primeList:
        print(p)

if __name__ == "__main__":
    main()
