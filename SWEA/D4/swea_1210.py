from my_package.hjtc import swea_tc 
    
def bfs(pos, board):
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
        
    
    pos = [99, board[99].index(2)]
    # print(pos)
    answer = bfs(pos, board)
    print(f'#{t} {answer}')
    