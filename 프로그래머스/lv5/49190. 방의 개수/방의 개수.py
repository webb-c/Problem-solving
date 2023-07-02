from collections import defaultdict

def solution(arrows):
    answer = 0
    x, y = 0, 0
    visited = defaultdict(list)
    direct = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    for d in arrows :
        for _ in range(2) : 
            nx, ny = x + direct[d][0], y + direct[d][1]
            if (nx,ny) in visited and (x,y) not in visited[(nx,ny)]:    
                answer += 1
                visited[(x,y)].append((nx,ny))
                visited[(nx,ny)].append((x,y))
            elif (nx,ny) not in visited:                  
                visited[(x,y)].append((nx,ny))            
                visited[(nx,ny)].append((x,y))
            x, y = nx, ny
    return answer