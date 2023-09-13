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
    result = N+1
    while True:
        ret = find_prime(result)
        flag = True
        if len(ret) == 2 and ret[0] != ret[1]:
            for n in range(min(ret)+1, max(ret)):
                if is_prime(n):
                    flag = False
            if flag:
                print(result)
                break
        result += 1

if __name__ == "__main__":
    main()
