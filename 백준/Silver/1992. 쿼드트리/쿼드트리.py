import sys
input = sys.stdin.readline

N = int(input())
img = [ list(input().rstrip()) for _ in range(N) ]

def quadtree(img) :
    n = len(img)
    if n == 1 : return img[0][0]
    if all(img[i][j] == img[0][0] for i in range(n) for j in range(n)) : return img[0][0]
    else :
        mid = n//2
        part1 = [row[:mid] for row in img[:mid]]
        part2 = [row[mid:] for row in img[:mid]]
        part3 = [row[:mid] for row in img[mid:]]
        part4 = [row[mid:] for row in img[mid:]]
        return "("+quadtree(part1)+quadtree(part2)+quadtree(part3)+quadtree(part4)+")"

print(quadtree(img))