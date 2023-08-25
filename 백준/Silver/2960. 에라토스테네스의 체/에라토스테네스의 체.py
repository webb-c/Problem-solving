import sys

def input():
    return sys.stdin.readline().rstrip()

def eratosthenes_sieve(N, K):
    isPrime = [True] * (N + 1)
    count = 0
    for i in range(2, N+1):
        for m in range(i, N+1, i):
            if isPrime[m]:
                isPrime[m] = False
                count += 1
                if count == K:
                    return m

def main():
    N, K = map(int, input().split())
    print(eratosthenes_sieve(N, K))

if __name__ == "__main__":
    main()
