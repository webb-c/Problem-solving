import sys

def input():
    return sys.stdin.readline().rstrip()


def count_prime(n, p):
    count = 0
    while n > 0:
        n //= p
        count += n
    return count


def main():
    n, m = map(int, input().split())
    count5 = count_prime(n, 5) - (count_prime(m, 5) + count_prime(n - m, 5))
    count2 = count_prime(n, 2) - (count_prime(m, 2) + count_prime(n - m, 2))
    print(min(count5, count2))


if __name__ == "__main__":
    main()
