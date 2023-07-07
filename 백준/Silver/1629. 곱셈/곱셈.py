"""
modulo 연산에 대한 분배법칙 :
(A + B) % p = ((A % p) + (B % p)) % p
(A * B) % p = ((A % p) * (B % p)) % p
(A - B) % p = ((A % p) - (B % p) + p) % p

나눗셈 연산은 페르마의 소정리를 적용해야한다. (추후 포스팅)
"""

import sys

input = sys.stdin.readline
A, B, C = map(int, input().split())

def modulo(A, B):
    if B == 1:
        return A % C
    else:
        ans = modulo(A, B // 2)
        if B % 2 == 0:
            return (ans * ans) % C
        else:
            return (ans * ans * A) % C

print(modulo(A, B))
