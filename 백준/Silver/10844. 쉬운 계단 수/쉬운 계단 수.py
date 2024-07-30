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

sys.setrecursionlimit(10**6)

MOD = 1000000000

def get_step(N, DP):
    for n in range(2, N+1):
        for i in range(10):
            if i == 0 :
                DP[n][i+1] += DP[n-1][i]
                DP[n][i+1] = DP[n][i+1] % MOD
            elif i == 9:
                DP[n][i-1] += DP[n-1][i]
                DP[n][i-1] = DP[n][i-1] % MOD
            else:
                DP[n][i+1] += DP[n-1][i]
                DP[n][i-1] += DP[n-1][i]
                DP[n][i+1], DP[n][i-1] = DP[n][i+1] % MOD, DP[n][i-1] % MOD
            
    return sum(DP[N]) % 1000000000
    

def input():
    return sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    DP = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(N+1)]
    DP[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(get_step(N, DP))
    
    
if __name__ == "__main__":
    solve()
    