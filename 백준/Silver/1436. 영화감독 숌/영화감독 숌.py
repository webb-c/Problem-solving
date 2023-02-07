import sys
input = sys.stdin.readline
N = int(input())
name = 666 # init
count = 0
while True :
    if '666' in str(name) :
        count += 1
        if count == N : break
    name += 1
print(name)