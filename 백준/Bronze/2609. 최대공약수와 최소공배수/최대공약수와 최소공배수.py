def get(a, b) :
    m = min(a,b)
    if m == 1 :
        return a, b, 0
    for mn in range(m, 1, -1):
        if a % mn == b % mn == 0 :
            return int(a/mn), int(b/mn), mn
    return a, b, 0

a, b = map(int, input().split())
MN = 0
mx = 1
while True:
    a2, b2, mn = get(a,b)
    if MN == 0 : MN = mn #최대공약수
    if mn == 0 :
        mx = mx*a2*b2
        break
    else :
        mx *= mn
        a = a2
        b = b2
if MN == 0 : MN=1
print(MN)
print(mx)