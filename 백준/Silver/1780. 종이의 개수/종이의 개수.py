import sys
input = sys.stdin.readline

N = int(input())
paper = [ list(map(int, input().split())) for _ in range(N) ]

def getPaper(paper) :
    n = len(paper)
    number = paper[0][0]
    if n == 1 :
        if number == -1 : return 1, 0, 0 # -1 0 1
        elif number == 0 : return 0, 1, 0
        else : return 0, 0, 1
    if all(paper[i][j] == paper[0][0] for i in range(n) for j in range(n)) :
        if number == -1:
            return 1, 0, 0  # -1 0 1
        elif number == 0:
            return 0, 1, 0
        else:
            return 0, 0, 1
    else :
        point1 = n//3
        point2 = n//3*2
        n1, z1, p1 = getPaper([row[:point1] for row in paper[:point1]])
        n2, z2, p2 = getPaper([row[point1:point2] for row in paper[:point1]])
        n3, z3, p3 = getPaper([row[point2:] for row in paper[:point1]])
        n4, z4, p4 = getPaper([row[:point1] for row in paper[point1:point2]])
        n5, z5, p5 = getPaper([row[point1:point2] for row in paper[point1:point2]])
        n6, z6, p6 = getPaper([row[point2:] for row in paper[point1:point2]])
        n7, z7, p7 = getPaper([row[:point1] for row in paper[point2:]])
        n8, z8, p8 = getPaper([row[point1:point2] for row in paper[point2:]])
        n9, z9, p9 = getPaper([row[point2:] for row in paper[point2:]])
        return (n1+n2+n3+n4+n5+n6+n7+n8+n9), (z1+z2+z3+z4+z5+z6+z7+z8+z9), (p1+p2+p3+p4+p5+p6+p7+p8+p9)

n, z, p = getPaper(paper)
print(n)
print(z)
print(p)