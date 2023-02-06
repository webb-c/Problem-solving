n, m = map(int, input().split())
neven = False
meven = False

if n%2 == 0 : neven = True
if m%2 == 0 : meven = True
k = n//2 + m//2
print(k)

for i in range(2, m+1, 2) :
    print(1, i, n, i)
for j in range(2, n+1, 2) :
    print(j, 1, j, m)