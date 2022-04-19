from collections import deque


def upstair():    
    for r in range(N-2, -1, -1):
        for c in range(M):
            
            if board[r][c] > 0:
                nr = r+1
                cnt = 1
                while N > nr >= 0:
                    
                    if board[nr][c] > 0:
                        board[r][c] = max(board[nr][c], cnt)
                        break
                    nr += 1
                    cnt += 1


def downstair():
    for r in range(1, N, 1):
        for c in range(M):
            if board[r][c] > 0:
                nr = r-1
                cnt = 1
                while N > nr >= 0:
                    
                    if board[nr][c] > 0:
                        board[r][c] = max(board[nr][c], cnt)
                        break
                    nr -= 1
                    cnt += 1
                    

def connect_chk():
    visited = [[0 for _ in range(M)] for _ in range(N)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for r in range(N):
        for c in range(M):
            if board[r][c] > 0:
                visited[r][c] = 1
                que = deque([[r, c]])
                same_lst = [(r, c)]
                min_val = board[r][c]
                
                while que:
                    sr, sc = que.popleft()
                    
                    for dr, dc in directions:
                        nr = sr + dr
                        nc = sc + dc
                        
                        if N > nr >= 0 and M > nc >= 0 and board[nr][nc] > 0 and visited[nr][nc] == 0:
                            visited[nr][nc] = 1
                            que.append([nr, nc])
                            same_lst.append([nr, nc])
                            min_val = min(min_val, board[nr][nc])
                            
                for mr, mc in same_lst:
                    board[mr][mc] = min_val
          


for t in range(int(input())):
    
    N, M = map(int, input().split())
    board = []
    goal = []
    
    for i in range(N):
        row = []
        for j, e in enumerate(map(int, input().split())):
            if e == 2:
                row.append(1)
            elif e == 3:
                goal = [i, j]
                row.append(1)
            else:
                row.append(e)
        board.append(row)
        
    upstair()           
    connect_chk()
    downstair()
    connect_chk()
    
    print(f'#{t+1} {board[goal[0]][goal[1]]}')