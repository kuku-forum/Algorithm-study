N, K = map(int, input().split())
board = [[[[],[]] for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j, val in enumerate(map(int, input().split())):
        board[i][j][0].append(val)

player_list = []

for i in range(K):
    y, x, direc = map(int, input().split())
    player_list.append([y - 1, x - 1, direc - 1])
    board[y - 1][x - 1][1].append(i)

def move_chk(y, x):
    if len(board[y][x][1]) >= 4:
        return True
    return False

direct_lst = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def convert_direct(idx, conv_dic):
    if conv_dic == 0: conv_dic = 1
    elif conv_dic == 1: conv_dic = 0
    elif conv_dic == 2: conv_dic = 3
    elif conv_dic == 3: conv_dic = 2
    player_list[idx][-1] = conv_dic
    return conv_dic

def white_board(player, ny, nx, y, x):
    tmp_list = []
    while board[y][x][1][-1] != player:
        tmp_player = board[y][x][1].pop()
        tmp_list.append(tmp_player)
        
        player_list[tmp_player][0] = ny
        player_list[tmp_player][1] = nx
    else:
        tmp_player = board[y][x][1].pop()
        tmp_list.append(tmp_player)
        player_list[tmp_player][0] = ny
        player_list[tmp_player][1] = nx
    
    board[ny][nx][1].extend(reversed(tmp_list))


def red_board(player, ny, nx, y, x):

    while board[y][x][1][-1] != player:
        tmp_player = board[y][x][1].pop()
        board[ny][nx][1].append(tmp_player)
        player_list[tmp_player][0] = ny
        player_list[tmp_player][1] = nx
    else:
        tmp_player = board[y][x][1].pop()
        board[ny][nx][1].append(tmp_player)
        player_list[tmp_player][0] = ny
        player_list[tmp_player][1] = nx


def blue_board(player, ny, nx, y, x, dirc):
    dirc = convert_direct(player, dirc)
    dy, dx = direct_lst[dirc]
    ny = y + dy
    nx = x + dx
    
    if N > ny >= 0 and N > nx >= 0:
        color = board[ny][nx][0][0]
        if color == 0: # 흰
            white_board(player, ny, nx, y, x)

        elif color == 1: # 빨
            red_board(player, ny, nx, y, x)
            
        if move_chk(ny, nx): return True   
        
    else:
        if move_chk(y, x): return True
        

def play(board):
    for player in range(K):
        y, x, dirc = player_list[player]
        dy, dx = direct_lst[dirc] 
        ny = y + dy
        nx = x + dx
        
        if N > ny >= 0 and N > nx >= 0:
            color = board[ny][nx][0][0]
            
            if color == 0: # 흰
                white_board(player, ny, nx, y, x)
                if move_chk(ny, nx): return True

            elif color == 1: # 빨
                red_board(player, ny, nx, y, x)
                if move_chk(ny, nx): return True
                
            elif color == 2: # 파
                if blue_board(player, ny, nx, y, x, dirc):
                    return True
        else: 
            if blue_board(player, ny, nx, y, x, dirc):
                return True
            
    return False

answer = 0

while True:
    flag = play(board)
    answer += 1
    
    if flag: break
    
    if answer > 1000:
        answer = -1
        break
    
print(answer)