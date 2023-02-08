import sys
input = sys.stdin.readline
T = int(input())
kList = []
sumList = []
for _ in range(T) : kList.append(int(input()))
kMax = max(kList)

pre = 0
while True :
    temp = pre + 23
    sumList.append(temp)
    pre = temp
    if len(sumList) > kMax : break

for k in kList :
    print(sumList[k-1])