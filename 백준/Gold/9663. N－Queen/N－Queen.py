import sys
input = sys.stdin.readline

N = int(input())
count = 0
row = [0]*N

def is_possible(n):
    for i in range(n):
        if row[n] == row[i] or abs(row[n]-row[i]) == abs(n-i):
            return False
    return True

def backtrack(n):
    global count
    if n == N:
        count += 1
        return 1
    for i in range(N):
        row[n] = i
        if is_possible(n):
            backtrack(n+1)

backtrack(0)
print(count)