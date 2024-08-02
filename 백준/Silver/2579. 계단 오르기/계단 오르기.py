import sys

def get_max_step_score(n, scores):
    DP = [0] * n
    DP[0], DP[1], DP[2] = scores[0], scores[0]+scores[1], max(scores[1]+scores[2], scores[0]+scores[2])
    
    for i in range(3, n):
        DP[i] = max(DP[i-2], DP[i-3]+scores[i-1]) + scores[i]
        
    return DP[-1]


def input():
    return sys.stdin.readline().rstrip()


def solve():
    n = int(input())
    scores = [int(input()) for _ in range(n)]
    
    if n == 1:
        print(sum(scores))
    elif n == 2:
        print(sum(scores))
    else:
        print(get_max_step_score(n, scores))
    


if __name__ == "__main__":
    solve()
    