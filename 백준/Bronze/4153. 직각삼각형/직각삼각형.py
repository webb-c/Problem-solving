while True:
    a, b, c = map(int, input().split())
    if a==b==c==0 : break
    dis = sorted([a, b, c])
    if dis[0]**2 + dis[1]**2 == dis[2]**2 : print("right")
    else : print("wrong")