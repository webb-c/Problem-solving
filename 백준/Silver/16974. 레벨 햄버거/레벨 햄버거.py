# [Silver 1] 레벨 햄버거 - 16974

N, X = map(int, input().split())
aNum = [1]
pNum = [1]
for i in range(1, N+1) :
    aNum.append(3 + 2*aNum[i-1])
    pNum.append(1 + 2*pNum[i-1])

def patty(n, x):
    if n == 0 :
        if x == 0 : return 0
        else : return 1
    elif x == 1 : return 0
    else :
        if x <= 1+aNum[n-1] : # B(N-1버거)에 위치
            return patty(n-1, x-1)
        elif x == 2+aNum[n-1] : # B(N-1버거)P와 동일
            return pNum[n-1]+1
        elif x > 2+aNum[n-1] : #B(N-1버거)P**(N-1버거)B**에서 위쪽 버거에 위치
            return pNum[n-1]+1+patty(n-1, x-(2+aNum[n-1]))
        else : # 전체 레이어==x
            return pNum[n]

print(patty(N, X))