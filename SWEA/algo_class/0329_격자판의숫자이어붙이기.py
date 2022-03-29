from my_package.hjtc import swea_tc


directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(r, c, line, n):
    if n == 6:
        answer.add(line)
        return
    
    for dr, dc in directions:
        nr = r + dr
        nc = c + dc
        
        if 4 > nr >= 0 and 4 > nc >= 0:
            dfs(nr, nc, line + board[nr][nc], n+1)
        
    
    
for t in range(1, int(input()) + 1):
    
    answer = set()
    board = [list(input().split()) for _ in range(4)]

    for i in range(4):
        for j in range(4):        
            dfs(i, j, board[i][j], 0)
            
    print(f'#{t} {len(answer)}')
