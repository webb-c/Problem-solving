import sys
import heapq as hp

N = int(sys.stdin.readline())
maxHeap = []  # 중간값 왼쪽 부분
minHeap = []  # 중간값 오른쪽 부분

for i in range(N):
    n = int(sys.stdin.readline())

    if len(maxHeap) == len(minHeap): hp.heappush(maxHeap, -n)   # 두 힙의 크기가 같다면 왼쪽에 push
    else: hp.heappush(minHeap, n) # 다르다면(=왼쪽이 더 큰 상태) 오른쪽에 push

    if minHeap and minHeap[0] < -maxHeap[0]:  # 정렬이 잘못된 상태면 swap
        leftNum = hp.heappop(maxHeap)
        rightNum = hp.heappop(minHeap)
        hp.heappush(maxHeap, -rightNum)
        hp.heappush(minHeap, -leftNum)

    print(-maxHeap[0]) #왼쪽 부분에서 가장 큰 값이 중간값