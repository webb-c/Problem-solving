import sys

def input():
    return sys.stdin.readline().rstrip()

def eratosthenes_sieve(n):
    isPrime = [0, 1] + [1] * (n - 1)
    for i in range(2, n+1):
        for m in range(i, n+1, i):
            if isPrime[m] == 0:
                isPrime[m] = 1
            else:
                isPrime[m] = 0
    return sum(isPrime)

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        print(eratosthenes_sieve(n))

if __name__ == "__main__":
    main()
