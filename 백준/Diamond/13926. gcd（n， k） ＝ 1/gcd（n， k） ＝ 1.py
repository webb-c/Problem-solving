import sys
import math
from random import randrange
# import statistics
# from itertools import combinations
# from fractions import Fraction
# import heapq
# from collections import Counter
# from collections import deque
# import operator as op
# from functools import reduce

sys.setrecursionlimit(10**5)

def input():
    return sys.stdin.readline().rstrip()


#################### Miller-Rabin ####################
def miller_rabin(n, a):
    """n이 합성수인지를 어떤 수 a를 사용하여 판정한다.
    Args:
        n (int): test number
        a (int, 0 < a < n): witness
    Returns:
        bool: 합성수라면 True, 합성수가 아니라면 False를 반환한다. 
    """
    # phase 1: n-1 = 2^s * d (d is odd) 를 만족하는 s와 d를 찾는 과정
    s, d = 0, n-1   
    while d % 2 == 0: 
        s += 1
        d //= 2
    
    # phase 2: 실제로 테스트를 진행하는 과정
    x = pow(a, d, n) # 파이선 내장함수. 내가 구현하는 분할정복보다 빠르다... (x = a^d * n)
    if (x == 1) or (x == n-1): # Eq 1을 만족하는가? 또는 r=0일 떄, Eq 2를 만족하는가?
        return False  
    for _ in range(s-1):
        x = pow(x, 2, n) 
        if x == n-1:     # Eq 2를 만족하는가?
            return False 
    return True           # Eq 1, 2를 둘 다 만족하지 않으므로 합성수이다.


def is_prime(n):
    """인자로 전달된 수가 소수인지를 판정해준다. (using det miller_rabin)
    Args:
        n (int): test number
    Returns:
        bool: 소수이면 True, 합성수이면 False를 반환한다. 
    """
    witness_candidate = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    
    if (n < 2) or (n > 2 and n % 2 == 0): return False
    if n == 2: return True

    for a in witness_candidate:
        if n <= a :
            break
        ret = miller_rabin(n, a)
        if ret:
            return False
    return True
######################################################


#################### Pollard-Rho Algorithm ####################
def g(x, c, n):
    """pollard-rho에서 수열을 만들기 위해 사용하는 연산을 수행합니다. 
    Args:
        - x (int): 입력
        - c (int): 상수값
        - n (int): modulo
    Returns:
        y (int): 출력; y = (x^2 +c mod n) mod n
    """
    return ((x**2 % n) + c) % n
    
    
def pollard_rho(n):
    """pollard-rho algorithm을 사용하여 n의 "소인수"를 반환합니다.
    Args:
        n (int): 소인수를 구할 수
    Returns:
        p (int): n의 랜덤한 소인수
    """
    if n == 1: return 1
    if n%2 == 0: return 2
    if is_prime(n): return n
    
    x, c = randrange(2, n), randrange(1, n)
    y = x
    while True:
        x = g(x, c, n)
        y = g(g(y, c, n), c, n)
        d = math.gcd(n, abs(x-y))
        if d != 1:
            if d == n: return pollard_rho(n)
            break
    
    if is_prime(d): return d
    else: return pollard_rho(d)


def factorization(n):
    """pollard-rho algorithm을 사용하여 구한 n의 소인수들을 반환합니다.
    Args:
        n (int): 소인수 분해를 할 수 
    """
    prime_divisors= []
    while True:
        d = pollard_rho(n)
        if d != 1:
            prime_divisors.append(d)
        n //= d
        if n == 1 :
            break
    
    return prime_divisors
###############################################################


def extend_euler_phi(n):
    """Euler_phi의 특징을 사용하여 euler_phi 함수 값을 계산하는 함수
    * phi(n) = phi(p^k) = p^{k-1} * (p-1)
    * phi(n) = phi(m * n) = phi(m) * phi(n)
    Args:
        n(int): 계산할 값
    Returns:
        phi: euler_phi함수의 값
    """
    prime_divisors = factorization(n)
    prime_divisors.sort()
    if len(prime_divisors) == 0:
        return 1
    
    phi = 1
    p, k = prime_divisors[0], 1
    for i in range(1, len(prime_divisors)):
        if prime_divisors[i] == p:
            k += 1
        else:
            # phi = phi * {p^{k-1} * (p-1)}
            phi *= (p**(k-1) * (p-1))
            k, p = 1, prime_divisors[i]
    phi *= (p**(k-1) * (p-1))
    return phi
    
    
def solve():
    n = int(input())
    print(extend_euler_phi(n))
    
if __name__ == "__main__":
    solve()
    