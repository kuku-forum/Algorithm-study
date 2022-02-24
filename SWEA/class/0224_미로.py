from pprint import pprint

def dfs(N, board, start):
    stack = [start]
    direction_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[start[0]][start[1]] = 1
    
    while stack:
        r, c = stack.pop()
        pprint(visited)
        print()
        if board[r][c] == 3:
            return 1
        
        for dr, dc in direction_list:
            nr = r + dr
            nc = c + dc
            
            if N > nr >= 0 and N > nc >= 0 and visited[nr][nc] == 0 and board[nr][nc] != 1:
                visited[nr][nc] = 1
                stack.append([nr, nc])
                
    return 0

for t in range(1, int(input()) + 1):
    N = int(input())
    board_list = []
    start = (N, N)
    
    for r in range(N):
        row = []
        
        for c, num in enumerate(map(int, input())):
            if num == 2:
                start = (r, c)
                
            row.append(num)
        board_list.append(row)
        
    answer = dfs(N, board_list, start)
    print(f'#{t} {answer}')