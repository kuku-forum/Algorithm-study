from my_package.hjtc import swea_tc


def max_func(*args):
    max_val = -0xffff
    
    for num in args:
        max_val = num if num > max_val else max_val
        
    return max_val

for _ in range(1, 11):
    answer = -1
    N = 100
    board = []
    t = input()
    
    for _ in range(N):
        board.append(list(map(int, input().split())))
    
    
    row_max = -1
    col_max = -1
    dig_max = 0
    re_dig_max = 0
    flag = True
    
    for i in range(N):
        tmp_row_max = 0
        tmp_col_max = 0
    
        for j in range(N):
            
            tmp_row_max += board[i][j]
            tmp_col_max += board[j][i]
            
            if flag:
                dig_max += board[j][j]
                re_dig_max += board[j][-1-j]
        
        flag = False
        row_max = max_func(row_max, tmp_row_max)
        col_max = max_func(col_max, tmp_col_max)
        
    answer = max_func(row_max, col_max, dig_max, re_dig_max)
    print(f'#{t} {answer}')