import sys
input = sys.stdin.readline

N = int(input())
paper = [ list(map(int, input().split())) for _ in range(N) ]

def getPaper(paper) :
    n = len(paper)
    color = paper[0][0]
    if n == 1 :
        if color == 1 : return 0, 1
        else : return 1, 0
    if all(paper[i][j] == paper[0][0] for i in range(n) for j in range(n)) :
        if color == 1 : return 0, 1
        else : return 1, 0
    else :
        mid = n//2
        w1, b1 = getPaper([row[:mid] for row in paper[:mid]])
        w2, b2 = getPaper([row[mid:] for row in paper[:mid]])
        w3, b3 = getPaper([row[:mid] for row in paper[mid:]])
        w4, b4 = getPaper([row[mid:] for row in paper[mid:]])
        return (w1+w2+w3+w4), (b1+b2+b3+b4)

w, b = getPaper(paper)
print(w)
print(b)