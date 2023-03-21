import sys
input = sys.stdin.readline

# 메모리 사용량 낮추는 기법 : 슬라이딩 윈도우 (쓰이지 않는값 버림)
N = int(input())
temp = list(map(int, input().split()))
maxDP = minDP = temp
for _ in range(N-1) :
    a, b, c = map(int, input().split())
    maxDP = [a+max(maxDP[0], maxDP[1]), b+max(maxDP), c+max(maxDP[1], maxDP[2])]
    minDP = [a+min(minDP[0], minDP[1]), b+min(minDP), c+min(minDP[1], minDP[2])]
print(max(maxDP), min(minDP))