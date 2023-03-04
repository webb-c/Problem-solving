import sys
input = sys.stdin.readline

T = int(input())
testList = [ int(input()) for _ in range(T) ]
maxN = max(testList)
table = [[1, 0], [0, 1]]
for i in range(2, maxN+1) : table.append([table[i-1][0]+table[i-2][0], table[i-1][1]+table[i-2][1]])
for t in testList : print(table[t][0], table[t][1])