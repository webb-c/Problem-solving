# 숫자카드 2
def binarySearch(array, left, right, num):
    if left > right : return 0
    mid = (left + right)//2
    if array[mid] == num : return array[left:right+1].count(num)
    elif array[mid] > num : return binarySearch(array, left, mid-1, num)
    else: return binarySearch(array, mid+1, right, num)

N = int(input())
A = sorted((list(map(int, input().split()))))
rangeA = len(A)-1
M = int(input())
B = list(map(int, input().split()))

answer = {}
for n in A :
    if n not in answer:
        answer[n] = binarySearch(A, 0, rangeA, n)
for m in B :
    if m in answer : print(answer[m], end=" ")
    else: print(0, end=" ")