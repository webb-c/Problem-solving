import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
segmentTree = [0 for _ in range(4 * N)]
numberList = [int(input()) for _ in range(N)]


# 세그먼트 트리 만들기
def make(idx, left, right):
    if left == right:
        segmentTree[idx] = numberList[left]
        return segmentTree[idx]
    mid = left + (right - left) // 2
    leftVal = make(idx * 2, left, mid)
    rightVal = make(idx * 2 + 1, mid + 1, right)
    segmentTree[idx] = (
        leftVal + rightVal
    )  # 구간합이 아닌 최댓값이라면 max(leftVal, rightVal)같은 형식으로 응용할 수 있다.
    return segmentTree[idx]


# 구간합 구하기 (left, right : 노드의 구간) (start, end : 주어진 구간)
def find(idx, left, right, start, end):
    # 구간이 포함 안되는 경우
    if end < left or start > right:
        return 0

    # 쿼리 구간안에 노드가 담당하는 구간이 포함된 경우
    if start <= left and right <= end:
        return segmentTree[idx]

    # 노드 담당 구간안에 쿼리 구간이 있는 경우
    mid = left + (right - left) // 2
    leftVal = find(idx * 2, left, mid, start, end)
    rightVal = find(idx * 2 + 1, mid + 1, right, start, end)
    return leftVal + rightVal


# 세그먼트 트리의 원소 값 변경하기
def change(idx, left, right, targetIdx, newVal):
    # 구간안에 없는 경우
    if targetIdx < left or targetIdx > right:
        return segmentTree[idx]
    if left == right:
        segmentTree[idx] = newVal
        return segmentTree[idx]
    mid = left + (right - left) // 2
    leftVal = change(idx * 2, left, mid, targetIdx, newVal)
    rightVal = change(idx * 2 + 1, mid + 1, right, targetIdx, newVal)
    segmentTree[idx] = leftVal + rightVal
    return segmentTree[idx]


make(1, 0, N - 1)
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        change(1, 0, N - 1, b - 1, c)
    else:
        print(find(1, 0, N - 1, b - 1, c - 1))
