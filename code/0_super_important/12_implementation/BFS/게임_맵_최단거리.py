from collections import deque

def solution(maps):
    cLen, rLen = len(maps[0]), len(maps)
    visited = [[0] * cLen for _ in range(rLen)]
    visited[0][0] = 1
    
    next_path = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque()
    queue.append((0, 0))
    
    while queue:
        r, c = queue.popleft()
        
        for path in next_path:
            nr = r + path[0]
            nc = c + path[1]
            
            if (nr >= 0) and (nc >= 0) and (nr < rLen) and (nc < cLen):
                if (maps[r][c] == 1 and visited[nr][nc] == 0):
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1
                
    return visited[rLen - 1][cLen - 1] or -1

