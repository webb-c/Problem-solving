import sys
import math
sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


def get_matrix_pow_with_mod(M, n, m):
    """주어진 행렬를 분할정복을 사용하여 C^n \mod m를 계산합니다.
    Args:
        M (list): 밑
        n (int): 지수
        m (int): 모듈로
    Returns:
        int: 거듭제곱 연산 결과
    """
    if n == 0:
        return [[1, 1],[1, 1]]
    if n == 1:
        return M
    if n == 2:
        return matrix_mul_with_mod(M, M, m)


    T = get_matrix_pow_with_mod(M, n // 2, m)
    
    TT = matrix_mul_with_mod(T, T, m)
    if n % 2 == 1:
        TTM = matrix_mul_with_mod(TT, M, m)
        return TTM
    else:
        return TT


def matrix_mul_with_mod(A, B, m):
    """주어진 두 행렬의 곱을 계산하며, 각 원소는 mod m을 취하여 표현됩니다. (A^{T}M)
    Args:
        A (list): 행렬 1
        B (list): 행렬 2
        m (int): 모듈로
    Returns:
        list: 행렬곱 연산 결과
    """
    ret = [[0, 0], [0, 0]]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ret[i][j] += A[i][k] * B[k][j]
            ret[i][j] = ret[i][j] % m
    
    # print(ret)
    return ret


def solve():
    n = int(input())
    m = 1000000
    M = [[1, 1], [1, 0]]
    Fn = get_matrix_pow_with_mod(M, n-1, m)
    
    print(Fn[0][0])
    
    
if __name__ == "__main__":
    solve()
    