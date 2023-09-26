import sys

def input():
    return sys.stdin.readline().rstrip()

def find(x):
    global parent
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    global parent
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def main():
    global parent
    N, M = map(int, input().split())
    knowTrueList = list(map(int, input().split()))[1:]
    parent = list(range(N+1))
    for p in knowTrueList:
        parent[p] = 0    # TRUE << 아이디어
    partyList = []
    for _ in range(M):
        party = list(map(int, input().split()))[1:]
        for i in range(len(party)-1):
            union(party[i], party[i+1])
        partyList.append(party)
    result = 0
    for party in partyList:
        partyKnow = False
        for i in range(len(party)):
            if find(party[i]) == 0:
                partyKnow = True
                break
        if not partyKnow:
            result += 1
    print(result)

if __name__ == "__main__":
    main()
