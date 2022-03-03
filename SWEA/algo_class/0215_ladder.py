def move(pos, board):
    y, x = pos[0], pos[1]
    while y >= 0:
        if x - 1 >= 0 and board[y][x - 1] == 1:
            board[y][x] = 2
            x -= 1
        elif 100 > x + 1 and board[y][x + 1] == 1:
            board[y][x] = 2
            x += 1
        else:
            board[y][x] = 2
            y -= 1
            
    return  x

for _ in range(10):
    t = int(input())
    board = []
    for _ in range(100):
        board.append(list(map(int, input().split())))
        
    start_j = -1
    
    for j in range(100):
        if board[99][j] == 2:
            start_j = j
            break
    pos = (99, start_j)
    
    print(f'#{t} {move(pos, board)}')