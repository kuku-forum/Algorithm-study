from my_package.hjtc import swea_tc

def print_board(arr):
    for row in arr:
        print(row)
    print()
    
for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    black_stone = white_stone = 0
    board = [[0 for _ in range(N)] for _ in range(N)]
    board[N//2][N//2] = 2
    board[N//2-1][N//2-1] = 2
    board[N//2][N//2-1] = 1
    board[N//2-1][N//2] = 1
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), 
                  (-1, -1), (1, 1), (1, -1), (-1, 1)]
    
    for _ in range(M):
        r, c, stone = map(int, input().split())
        r -= 1
        c -= 1
        re_stone = 1
        
        if stone == 1:
            re_stone = 2
        
        # print(r, c, stone)
        board[r][c] = stone
        
        
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            ch_lst = []
            
            while N > nr >= 0 and N > nc >= 0 and board[nr][nc] == re_stone:
                ch_lst.append([nr, nc])
                nr += dr
                nc += dc
                
            # print(ch_lst)
            
            if N > nr >= 0 and N > nc >= 0 and board[nr][nc] == stone:
                for cr, cc in ch_lst:
                    board[cr][cc] = stone
        
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                black_stone += 1
            else:
                white_stone += 1
                    
        
    print(f'#{t} {black_stone} {white_stone}')
    