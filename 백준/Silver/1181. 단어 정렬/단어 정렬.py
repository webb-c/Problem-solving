import sys
input = sys.stdin.readline

N = int(input())
wordList = []
for _ in range(N):
    wordList.append(input().strip())
newWordList = list(set(wordList))
newWordList.sort()        # 알파벳 순 후순위 정렬
newWordList.sort(key=len) # 길이 순 정렬
for word in newWordList :
    print(word)