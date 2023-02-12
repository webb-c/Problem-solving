import sys
input = sys.stdin.readline

def binarySearch(array, left, right, num):
    if left > right : return 0
    mid = (left + right)//2
    if array[mid] == num : return 1
    elif array[mid] > num : return binarySearch(array, left, mid-1, num)
    else: return binarySearch(array, mid+1, right, num)

N = int(input())
A = sorted((list(map(int, input().split()))))
rangeA = len(A)-1
M = int(input())
B = list(map(int, input().split()))
for i in range(M) :
    print(binarySearch(A, 0, rangeA, B[i]))