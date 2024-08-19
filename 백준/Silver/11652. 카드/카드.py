import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    hash_map = dict()
    for _ in range(N):
        val = input()
        if val not in hash_map:
            hash_map[val] = 0
        hash_map[val] += 1
    
    max_value = max(hash_map.values())
    smallest_key = min(int(key) for key, value in hash_map.items() if value == max_value)

    print(smallest_key)

    
if __name__ == "__main__":
    solve()
    