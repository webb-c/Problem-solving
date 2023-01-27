# [Bronze 1] 평균 - 1546
N = int(input())
sList = list(map(int, input().split()))
nList = list(map(lambda s: s/max(sList)*100, sList))
print(sum(nList)/N)