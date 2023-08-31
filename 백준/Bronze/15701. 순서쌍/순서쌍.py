import sys

def input():
    return sys.stdin.readline().rstrip()

def find_divisors_sum(n):
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    return len(list(divisors))

def main():
    N = int(input())
    print(find_divisors_sum(N))

if __name__ == "__main__":
    main()
