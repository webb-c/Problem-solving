import sys
import heapq
input = sys.stdin.readline

minHeap = []
flag = False
N = int(input())
for _ in range(N) :
    x = int(input())
    if x != 0 :
        if x < 0 :
            x = -x
            flag = False
        else : flag = True
        heapq.heappush(minHeap, (x, flag))
    else :
        a = 0
        if len(minHeap) != 0:
            a, f = heapq.heappop(minHeap)
            if not f : a = -a
        print(a)