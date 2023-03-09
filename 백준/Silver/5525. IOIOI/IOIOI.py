import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()
pattern = 'I'
for _ in range(N): pattern += 'OI'

count = 0
for i in range(M-len(pattern)+1):
    if S[i:i+len(pattern)] == pattern:
        count += 1
print(count)