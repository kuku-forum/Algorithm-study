
direc_even = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 0)]
direc_odd = [(-1, 0), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
direc_center_1 = [(0, -1), (0, 1), (1, 0)]
direc_center_2 = [(0, -1), (1, -1), (1, 2)]


def dfs(r, c, n, ssum):
    global answer
    
    if n == 3:
        answer = max(answer, ssum)
        return
    
    if c%2 == 1: # odd
        for dr, dc in direc_odd:
            nr = r + dr
            nc = c + dc
            
            if H > nr >= 0 and W > nc >= 0 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                dfs(nr, nc, n+1, ssum + board[nr][nc])
                visited[nr][nc] = 0
    
    else:
        for dr, dc in direc_even:
            nr = r + dr
            nc = c + dc
            
            if H > nr >= 0 and W > nc >= 0 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                dfs(nr, nc, n+1, ssum + board[nr][nc])
                visited[nr][nc] = 0
    return


for t in range(int(input())):
    W, H = map(int, input().split())
    answer = 0
    board = [list(map(int, input().split())) for _ in range(H)]
    visited = [[0 for _ in range(W)] for _ in range(H)]
    
    for i in range(H):
        for j in range(W):
            visited[i][j] = 1
            dfs(i, j, 0, board[i][j])
            visited[i][j] = 0
    
    for i in range(H):
        for j in range(W):
            tmp = board[i][j]
            
            for di, dj in direc_center_1:
                ni = i + di
                nj = j + dj
                
                if H > ni >= 0 and W > nj >= 0:
                    tmp += board[ni][nj]
                else:
                    break
            else:
                answer = max(answer, tmp)
    
    print(f'#{t+1} {answer**2}')