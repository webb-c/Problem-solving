import sys

def input():
    return sys.stdin.readline().rstrip()


def eratosthenes_sieve(n):
    global isPrime
    isPrime = [0, 0] + [1] * (n - 1)
    for i in range(2, int(n**0.5)+1):
        if isPrime[i]:
            for j in range(i*i, n+1, i):
                isPrime[j] = 0


def get_super_prime():
    global isPrime, superPrime
    superPrime = []
    k = 0
    for n in range(1000000):
        if isPrime[n]:
            k += 1
            if isPrime[k]:
                superPrime.append(n)


def solve():
    global isPrime, superPrime
    T = int(input())
    eratosthenes_sieve(1000000)
    get_super_prime()

    for _ in range(T):
        print(superPrime[int(input())-1])


if __name__ == "__main__":
    solve()
