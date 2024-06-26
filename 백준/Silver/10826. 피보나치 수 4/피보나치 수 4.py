import sys
import math
sys.setrecursionlimit(10**5)


def input():
    return sys.stdin.readline().rstrip()


def get_matrix_pow(M, n):
    """주어진 행렬를 분할정복을 사용하여 계산합니다.
    Args:
        M (list): 밑
        n (int): 지수
    Returns:
        list: 연산 결과
    """
    if n == 0:
        return [[1, 1],[1, 1]]
    if n == 1:
        return M
    if n == 2:
        return matrix_mul(M, M)

    T = get_matrix_pow(M, n // 2)
    TT = matrix_mul(T, T)
    if n % 2 == 1:
        TTM = matrix_mul(TT, M)
        return TTM
    else:
        return TT


def matrix_mul(A, B):
    """주어진 두 행렬의 곱을 계산합니다. (A^{T}M)
    Args:
        A (list): 행렬 1
        B (list): 행렬 2
    Returns:
        list: 행렬곱 연산 결과
    """
    ret = [[0, 0], [0, 0]]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ret[i][j] += A[i][k] * B[k][j]
                
    return ret


def solve():
    n = int(input())
    M = [[1, 1], [1, 0]]
    if n == 0: 
        print(0)
    else:
        Fn = get_matrix_pow(M, n-1)
        print(Fn[0][0])
    
    
if __name__ == "__main__":
    solve()
    