n = int(input())
for _ in range(n):
    case, d, a, b, f = map(float, input().split())
    t = d/(a+b) * f
    print(case,"{:.6f}".format(t))