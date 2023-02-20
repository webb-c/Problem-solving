import sys
input = sys.stdin.readline

K, N = map(int, input().split())
LanList = [ 0 for _ in range(K) ]
for i in range(K) : LanList[i] = int(input())

minLength = 1
maxLength = max(LanList) 
while True :
    mid = (minLength + maxLength) // 2
    count = 0
    for i in range(K) :
        count += LanList[i] // mid
    if count >= N : minLength = mid + 1
    else : maxLength = mid -1
    if minLength > maxLength : break

print(maxLength)