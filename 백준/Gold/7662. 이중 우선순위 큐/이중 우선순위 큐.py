import sys
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    maxHeap, minHeap = [], []  # nlargest쓰면 시간초과
    visited = [False] * k
    for i in range(k):
        cmd, n = input().split()
        n = int(n)
        if cmd == 'I':
            heapq.heappush(maxHeap, (-n, i))
            heapq.heappush(minHeap, (n, i))
            visited[i] = True
        else:
            if n == 1 :
                while maxHeap and not visited[maxHeap[0][1]] :
                    heapq.heappop(maxHeap)
                if maxHeap :
                    visited[maxHeap[0][1]] = False
                    heapq.heappop(maxHeap)
            else :
                while minHeap and not visited[minHeap[0][1]] :
                    heapq.heappop(minHeap)
                if minHeap :
                    visited[minHeap[0][1]] = False
                    heapq.heappop(minHeap)
        while minHeap and not visited[minHeap[0][1]] :
            heapq.heappop(minHeap)
        while maxHeap and not visited[maxHeap[0][1]] :
            heapq.heappop(maxHeap)
    if minHeap or maxHeap:
        print(-heapq.heappop(maxHeap)[0], heapq.heappop(minHeap)[0])
    else:
        print("EMPTY")