'''
하나의 말 위에 다른 말을 올릴 수 있다
흰색, 빨간색, 파란색
이동 방향도 미리 정해져 있다. 이동 방향은 위, 아래, 왼쪽, 오른쪽 4가지

턴 한 번은 1번 말부터 K번 말까지 순서대로 이동시키는 것
말이 4개 이상 쌓이는 순간 게임이 종료

흰색인 경우에는 그 칸으로 이동한다
D, E +  A, B, C = D, E, A, B, C
 
빨간색인 경우에는 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다
E, C, B + A, D, F, G =  E, C, B, G, F, D, A
 
파란색인 경우에는 A번 말의 이동 방향을 반대로 하고 한 칸 이동
이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다
체스판을 벗어나는 경우에는 파란색과 같은 경우

1. 보드별 이동 방법 제시
0 흰 extend
1 빨 pop()
2 파 방향 변경(rotate(-2)) -> 또 벽, 파란일경우, 빨강, 흰색

2. 끝나지 않을 경우 확인(1000보다 커질 경우), 루프를 돌아도 그대로인 경우
3. 쌓였을때 종료

# pprint(board)
# print(board[1][0][0]) #  색상
# print(board[1][1][1]) # player

'''
from pprint import pprint

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

# 오, 왼, 위, 아래
direct_lst = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def move_chk(y, x):
    if len(board[y][x][1]) >= 4:
        return True
    return False

def convert_direct(idx, conv_dic):
    if conv_dic == 0: 
        conv_dic = 1
        
    elif conv_dic == 1: 
        conv_dic = 0
        
    elif conv_dic == 2: 
        conv_dic = 3
        
    elif conv_dic == 3: 
        conv_dic = 2
        
    player_list[idx][-1] = conv_dic
    return conv_dic

def play(board):
    for player in range(K):
        y, x, dirc = player_list[player]
        dy, dx = direct_lst[dirc]
        
        ny = y + dy
        nx = x + dx
        
        if N > ny >= 0 and N > nx >= 0:
            color = board[ny][nx][0][0]
            # print(color)
            
            if color == 0: # 흰
                # print(board[y][x][1], board[y][x][1][-1])
                
                tmp_list = []
                # print('#1', tmp_list)
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
                # print('#2', tmp_list)
                board[ny][nx][1].extend(reversed(tmp_list))
                if move_chk(player_list[player][0], player_list[player][1]): return True
    

            elif color == 1: # 빨
                # print(y, x, board[y][x][1])
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
                if move_chk(player_list[player][0], player_list[player][1]): return True
                
            elif color == 2: # 파
                
                dirc = convert_direct(player, dirc)
                dy, dx = direct_lst[dirc]
                ny = y + dy
                nx = x + dx
                
                if N > ny >= 0 and N > nx >= 0 and color != 2:
                    color = board[ny][nx][0][0]
                    if color == 0: # 흰
                        # print(y, x, board[y][x][1])
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

                    elif color == 1: # 빨
                        # print(y, x, board[y][x][1])
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
                if move_chk(player_list[player][0], player_list[player][1]): return True
            
        else:
            dirc = convert_direct(player, dirc)
            dy, dx = direct_lst[dirc]
            ny = y + dy
            nx = x + dx
            color = board[ny][nx][0][0]
            
            if N > ny >= 0 and N > nx >= 0 and color != 2:
                if color == 0: # 흰
                    # print(y, x, board[y][x][1])
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

                elif color == 1: # 빨
                    # print(y, x, board[y][x][1])
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
                        
            if move_chk(player_list[player][0], player_list[player][1]): return True
                    
                    
        # pprint(board)
        # print(player, player_list, player_list[player])
        # print()
        
        if move_chk(player_list[player][0], player_list[player][1]): return True
        
    return False
# print('----------------------')
answer = 0
while True:
    flag = play(board)
    # flag = play(board)
    # break
    answer += 1
    if flag:
        break
    # print(answer)
    if answer > 1000:
        answer = -1
        break
    
print(answer)