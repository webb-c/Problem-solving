T = int(input())
for _ in range(T):
    R, S = input().split()
    newS = ""
    for ch in S : newS += ch*int(R)
    print(newS)