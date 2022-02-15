T = int(input())

for t in range(1, T+1):
    
    max_val = 0
    N, M = map(int, input().split())
    board = []
    
    for _ in range(N):
        board.append(list(map(int, input().split())))
        
    for y in range(N-M+1):
        for x in range(N-M+1):
            sum_val = 0
            
            for dy in range(M):
                for dx in range(M):
                    ny = y + dy
                    nx = x + dx
                    sum_val += board[ny][nx]
                    
            max_val = sum_val if sum_val > max_val else max_val
    
    print(f'#{t} {max_val}')