import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()

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
    witness_candidate = [2, 3, 5, 7, 11,]
    
    if (n < 2) or (n > 2 and n % 2 == 0): return False
    if n == 2: return True

    for a in witness_candidate:
        if n <= a :
            break
        ret = miller_rabin(n, a)
        if ret:
            return False
    return True


def solve():
    N = int(input())
    area_list = [int(input()) for _ in range(N)]
    ans = 0
    for area in area_list:
        if is_prime(2*area+1): ans += 1
    print(ans)

    

if __name__ == "__main__":
    solve()
