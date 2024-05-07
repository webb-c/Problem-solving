import sys

sys.setrecursionlimit(10**5)


def input():
    return sys.stdin.readline().rstrip()


def partition(A, p, r):
    global K, count
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            count += 1
            if count == K:
                print(A[i], A[j])
                return -1
    if i+1 != r:
        A[i+1], A[r] = A[r], A[i+1]
        count += 1
        if count == K:
            print(A[i+1], A[r])
            return -1
    return i+1


def select(A, p, r, q):
    global K, count
    if p == r: return A[p]
    t = partition(A, p, r)
    if t == -1: return
    
    k = t - p + 1
    if q < k: return select(A, p, t-1, q)
    elif q == k: return A[p]
    else: return select(A, t+1, r, q-k)


def solve():
    global K, count
    count = 0
    N, Q, K = map(int, input().split())
    A = list(map(int, input().split()))
    select(A, 0, N-1, Q)
    if count < K:
        print(-1)


    
if __name__ == "__main__":
    solve()
