from cgitb import reset
from my_package.hjtc import swea_tc 
    
def print_board(arr):
    for row in arr:
        print(row)
    print(row)
    
def bfs(pos_list, board):
    min_val = 100*100
    result = -1
    
    while pos_list:
        pos = pos_list.pop()
        y, x = 0, pos
        cnt = 0
        reset_idx = []
        
        while 100 > y:
            if x - 1 >= 0 and board[y][x - 1] == 1:
                board[y][x] = 2
                x -= 1
            elif 100 > x + 1 and board[y][x + 1] == 1:
                board[y][x] = 2
                x += 1
            else:
                board[y][x] = 2
                y += 1
                
            reset_idx.append([y, x])
            cnt += 1
            
        if min_val > cnt:
            min_val = cnt
            result = pos
            
        for ry, rx in reset_idx[:-1]:
            board[ry][rx] = 1
        
    return  result

for _ in range(10):
    t = int(input())
    board = []
    for _ in range(100):
        board.append(list(map(int, input().split())))
    
    pos_list = list(filter(lambda x: board[0][x] == 1 , range(len(board[0]))))
    answer = bfs(pos_list, board)
    swea_tc(f'#{t} {answer}')
    