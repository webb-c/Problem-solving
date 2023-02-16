import sys
import heapq
input = sys.stdin.readline

# maxC <= (N+1)//2 라는 조건만 만족하면 항상 성립하는 이유 증명 추가

N, K = map(int, input().split())
cList = list(map(int, input().split()))
MaxHeap = []
okList = [ 0 for _ in range(N) ]

for i in range(K) :
    heapq.heappush(MaxHeap, [-cList[i], i+1])

constrain = (N+1)//2
if -MaxHeap[0][0] > constrain :
    print(-1)

else :
    oe = 0
    while MaxHeap :
        c, idx = heapq.heappop(MaxHeap)
        for j in range(-c) :
            okList[oe] = str(idx)
            oe += 2
            if oe > N-1 : oe = 1
    print(" ".join(okList))