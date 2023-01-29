T = int(input())
for _ in range(T) :
    H, W, N = map(int, input().split())
    x = int(N / H) + 1
    y = N % H
    if N % H == 0 :
        x -= 1
        y = H
    if x < 10 : x = "0"+str(x)
    else : x = str(x)
    print(str(y)+x)