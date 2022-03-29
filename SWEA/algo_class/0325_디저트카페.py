from my_package.hjtc import swea_tc

from copy import deepcopy

direction_dic = {0: (1, 1), 1: (1, -1), 
                 2: (-1, -1), 3: (-1, 1)}

def dfs(root, visited, used, i):
    global answer
    nr, nc = root
    dr, dc = direction_dic[i]
    nr += dr
    nc += dc
    
    if nr == sr and nc == sc and used > 1:
        answer = max(answer, used)
        return
        
    if N > nr >= 0 and N > nc >= 0 and board[nr][nc] not in visited:
         
        if i == 0:
            dfs((nr, nc), visited + [board[nr][nc]], used + 1, 0)
            dfs((nr, nc), visited + [board[nr][nc]], used + 1, 1)
        elif i == 1:
            dfs((nr, nc), visited + [board[nr][nc]], used + 1, 1)
            dfs((nr, nc), visited + [board[nr][nc]], used + 1, 2)
        elif i == 2:
            dfs((nr, nc), visited + [board[nr][nc]], used + 1, 2)
            dfs((nr, nc), visited + [board[nr][nc]], used + 1, 3)
        elif i == 3:
            dfs((nr, nc), visited + [board[nr][nc]], used + 1, 3)
    else:
        return

for t in range(1, int(input()) + 1):
    
    answer = -1
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    for sr in range(N):
        for sc in range(N):
            dfs((sr, sc), [board[sr][sc]], 1, 0)
        
    print(f'#{t} {answer}')
