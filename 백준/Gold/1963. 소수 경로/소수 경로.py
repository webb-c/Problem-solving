import sys
import math
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def bfs(start, end, visited):
    global isPrime
    queue = deque()
    queue.append([start, 0])
    while queue:
        u, count = queue.popleft()
        if u == end:
            return count
        for i in range(4):
            for j in range(10):
                uStr = str(u)
                v = int(uStr[:i] + str(j) + uStr[i+1:])
                if v < 1000:
                    continue
                if isPrime[v] and not visited[v]:
                    visited[v] = True
                    queue.append([v, count+1])
    return "Impossible"

def eratosthenes_sieve(n):
    global isPrime
    isPrime = [False, False] + [True] * (n - 1)
    for i in range(2, int(n**0.5)+1):
        if isPrime[i]:
            for j in range(i*i, n+1, i):
                isPrime[j] = False

def solve(a, b, N):
    visited = [False for _ in range(N)]
    visited[a] = True
    return bfs(a, b, visited)

def main():
    T = int(input())
    eratosthenes_sieve(100000)
    for _ in range(T):
        a, b = map(int, input().split())
        print(solve(a, b, 100000))

if __name__ == "__main__":
    main()
