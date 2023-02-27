import sys
import heapq as h
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N) :
    x = int(input())
    if x > 0 :
        h.heappush(heap, -x) #maxHeap
    else :
        if len(heap) == 0 : print(0)
        else : print(-h.heappop(heap))