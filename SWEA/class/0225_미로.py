def bfs(board, root):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[root[0]][root[1]] = 1
    que = [root]
    
    while que:
        r, c = que.pop(0)
        if board[r][c] == 3:
            return 1
        
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            
            if N > nr >= 0 and N > nc >= 0 and board[nr][nc] != 1 and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                que.append([nr, nc])    
    return 0
    
    
for t in range(1, int(input()) + 1):
    N = int(input())
    board = []
    s_pos = []
    for i in range(N):
        row = []
        for j, k in enumerate(map(int, input())):
            if k == 2:
                s_pos = [i, j]
            row.append(k)
        board.append(row)
    
    answer = bfs(board, s_pos)
    print(f'#{t} {answer}')