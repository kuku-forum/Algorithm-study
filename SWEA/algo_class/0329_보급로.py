from my_package.hjtc import swea_tc

for t in range(1, int(input()) + 1):
    N = int(input())
    answer = 0
    
    board = [list(map(int, input())) for _ in range(N)]
    
    stack = [(0, 0)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    INF = 0xffff
    visited = [[INF for _ in range(N)] for _ in range(N)]
    visited[0][0] = 0
    
    while stack:
        r, c = stack.pop(0)
        
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            
            if N > nr >= 0 and N > nc >= 0:
                if visited[nr][nc] > board[nr][nc] + visited[r][c]:
                    visited[nr][nc] = board[nr][nc] + visited[r][c]
                    stack.append((nr, nc))
                    
    print(f'#{t} {visited[-1][-1]}')