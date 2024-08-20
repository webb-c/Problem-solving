import sys

def input():
    return sys.stdin.readline()


def solve():
    string = list(input())
    MOD = 26
    code = string
    for i, ch in enumerate(string):
        if ch.isalpha():
            if ch.isupper():
                code[i] = chr(((ord(ch)+13 - ord('A')) % MOD) + ord('A'))    
            else:
                code[i] = chr(((ord(ch)+13 - ord('a')) % MOD) + ord('a'))
            
    print(''.join(code))
        
if __name__ == "__main__":
    solve()
    