import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()


def solve():
    hash_map = {}
    hash_map["small"] = 0
    hash_map["big"] = 0
    hash_map["int"] = 0
    hash_map[" "] = 0
    
    while True:
        string = list(input())
        if len(string) == 0:
            break
        hash_map = hash_map.fromkeys(hash_map, 0)
        for ch in string:
            if ch == " ":
                hash_map[" "] += 1
            elif '0' <= ch <= '9':
                hash_map["int"] += 1
            elif 'a' <= ch <= 'z':
                hash_map["small"] += 1
            elif 'A' <= ch <= 'Z':
                hash_map["big"] += 1
            
        print(hash_map["small"], hash_map["big"], hash_map["int"], hash_map[" "])

        
if __name__ == "__main__":
    solve()
    