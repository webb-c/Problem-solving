import sys

"""자연수 n이 주어졌을 때, GCD(n, k) = 1을 만족하는 자연수 1 ≤ k ≤ n 의 개수를 구하는 프로그램을 작성하시오.
"""

def input():
    return sys.stdin.readline().rstrip()
    
def euler_phi(n):
    result = n
    i = 2
    while True:
        if i*i > n: break
        if n%i == 0:
            while True:
                if n%i != 0: break
                n /= i
            result -= result / i
        i+=1
    if n > 1:
        result -= result / n
    return int(result)


def solve():
    n = int(input())
    print(euler_phi(n))


if __name__ == "__main__":
    solve()
