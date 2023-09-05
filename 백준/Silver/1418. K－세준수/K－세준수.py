import sys

def input():
    return sys.stdin.readline().rstrip()

def eratosthenes_sieve(N):
    isPrime = [False, False] + [True] * (N - 1)
    for i in range(2, int(N**0.5)+1):  
        if isPrime[i]:
            for m in range(2*i, N+1, i): 
                isPrime[m] = False
    return isPrime

def main():
    N = int(input())
    K = int(input())
    isPrime = eratosthenes_sieve(N)
    KList = [1] * (N+1)
    for i in range(2, N+1):
        if isPrime[i] and K < i:
            for j in range(i, N+1, i):
                KList[j] = 0
    print(sum(KList)-1)

if __name__ == "__main__":
    main()
