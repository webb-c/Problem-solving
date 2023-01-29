N = input()
length = len(N)
N = int(N)
MList = []
for i in range(-length*9, length*9+1):
    parse = 0
    n = N+i
    if n <= 0 : continue
    for ch in str(n):
        parse += int(ch)
    if n+parse == N :
        MList.append(n)
if len(MList)>0 :
    print(min(MList))
else :
    print("0")