for t in range(1, int(input()) + 1):
    
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    i, j = 0, 0
    length = N - 1
    cnt = 2
    board[i][j] = 1
    direct = 0
    direct_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    flag = 3
    
    while length > 0:
        for _ in range(length):
            di, dj = direct_list[direct]
            i += di
            j += dj
            board[i][j] = cnt
            cnt += 1
            
        flag -= 1
        direct = (direct + 1)%4
        
        if flag == 0:
            flag = 2
            length -= 1
            
            
    print(f'#{t}')
    for row in board:
        print(' '.join(map(str, row)))
            
    