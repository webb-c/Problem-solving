int(input())
treeList = list(map(int, input().split()))
treeList.sort(reverse=True)
endList = []
for i, t in enumerate(treeList) :
    endList.append(t + i + 1)
print(max(endList)+1)