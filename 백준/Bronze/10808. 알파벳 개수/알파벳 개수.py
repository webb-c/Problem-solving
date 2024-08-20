import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


def solve():
    string = list(input())
    hash_map = {}
    
    for i in range(ord('a'), ord('z') + 1):
        hash_map[chr(i)] = 0
    
    for ch in string:
        hash_map[ch] += 1
        
    for value in hash_map.values():
        print(value, end=" ")
    
    
if __name__ == "__main__":
    solve()
    