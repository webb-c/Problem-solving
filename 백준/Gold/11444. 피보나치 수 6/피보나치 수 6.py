import sys
input = sys.stdin.readline

def power(mat, n) :
    if n==1 : return mat
    elif n%2 : return matmul(power(mat, n-1), mat)
    else : return power(matmul(mat, mat), n//2)

def matmul(A, B) :
    AB = [[0]*len(B[0]) for _ in range(2)]
    for i in range(2) :
        for j in range(len(B[0])) :
            total = 0
            for k in range(2) :
                total += A[i][k]*B[k][j]
            AB[i][j] = total%1000000007
    return AB

n = int(input())
fibo = [[1],[1]]
adj = [[1,1],[1,0]]
if n < 3 : print(1)
else : print(matmul(power(adj, n-2), fibo)[0][0])