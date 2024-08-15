import sys
 

def input():
    return sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    data_list = [list(input().split()) for _ in range(N)]
    sorted_data_list = sorted(data_list, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
    
    for i in range(N):
        print(sorted_data_list[i][0])
    

if __name__ == "__main__":
    solve()
    