import sys
input = sys.stdin.readline

N = int(input())
repeat = True
num5 = N//5
re = N%5
if re == 0:
    print(num5)
    repeat = False
elif re == 3:
    print(num5+1)
    repeat = False
while repeat:
    num5 -= 1
    re += 5
    if num5 < 0 :
        print(-1)
        break
    if re % 3 == 0:
        print(num5+re//3)
        break