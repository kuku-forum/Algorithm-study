from collections import deque, defaultdict
from copy import deepcopy

N, M, K = map(int, input().split())
board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

# deque
'''
  2
4 1 3
  5
  6
'''
dice_row = deque([4, 1, 3])
dice_col = deque([2, 1, 5, 6])
# dice_dir[0] 나의 방향 rot90: eswn -> swne  rot-90 eswn -> nesw
dice_dir = deque(['E', 'S', 'W', 'N'])
foward_pos = {'E': (0, 1), 
              'S': (1, 0), 
              'W': (0, -1), 
              'N': (-1, 0)}

# 진행하는 방향
def dice_run(ch_dir):
    # east
    if ch_dir == 'E':
        dice_row.rotate(1)
        dice_col[1] = dice_row[1]
        dice_col[-1], dice_row[0] = dice_row[0], dice_col[-1] 
        
    # west
    elif ch_dir == 'W':
        dice_row.rotate(-1)
        dice_col[1] = dice_row[1]
        dice_col[-1], dice_row[-1] = dice_row[-1], dice_col[-1] 
        
    # south
    elif ch_dir == 'S':
        dice_col.rotate(1)
        dice_row[1] = dice_col[1]
        
    # north
    elif ch_dir == 'N':
        dice_col.rotate(-1)
        dice_row[1] = dice_col[1]
    
# 현재위치, 나아갈 방향 E, (0, 0)
def play_game(cur_dir, cur_pos):
    dy, dx = foward_pos[cur_dir]
    y, x = cur_pos
    
    # map 안에 있는거
    if N > y + dy >= 0 and M > x + dx >= 0:
        ny, nx = y + dy, x + dx
        board_num = board[ny][nx]
        dice_run(cur_dir)
        
    # map 밖으로 갈 경우
    else:
        dice_dir.rotate(2)
        new_cur_dir = dice_dir[0]
        dy, dx = foward_pos[new_cur_dir]
        ny, nx = y + dy, x + dx
        board_num = board[ny][nx]
        dice_run(new_cur_dir)
        
    dice_num = dice_col[-1]
    
    if dice_num > board_num:
        dice_dir.rotate(-1)
    elif dice_num < board_num:
        dice_dir.rotate(1)
    
    return board_num, (ny, nx)
        



def board_calc(board_list):
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visited[i][j] == True:
                continue
            
            que = deque([[i, j]])
            cnt = 1
            visited[i][j] = True
            score = board_list[i][j]
            chk_lst = [(i, j)]
            
            while que:
                y, x = que.popleft()
                for dy, dx in foward_pos.values():
                    ny = y + dy
                    nx = x + dx
                    
                    if N > ny >= 0 and M > nx >= 0 and visited[ny][nx] == False:
                        if board[ny][nx] == score:
                            cnt += 1
                            que.append((ny, nx))
                            visited[ny][nx] = True
                            chk_lst.append((ny, nx))
            
            for chk_i, chk_j in chk_lst:
                board_list[chk_i][chk_j] = score*cnt
    
    return board_list
    
score_board = board_calc(deepcopy(board))
answer = 0 
pos = (0, 0) # 시작위치
for _ in range(K):
    num, pos = play_game(dice_dir[0], pos)
    # answer += calc_score(num, pos)
    answer += score_board[pos[0]][pos[1]]
print(answer)



def calc_score(score, root):
    visited = [[False for _ in range(M)] for _ in range(N)]
    que = deque([root])
    cnt = 1
    visited[root[0]][root[1]] = True
    
    while que:
        y, x = que.popleft()
        for dy, dx in foward_pos.values():
            ny = y + dy
            nx = x + dx
            
            if N > ny >= 0 and M > nx >= 0 and visited[ny][nx] == False:
                if board[ny][nx] == score:
                    cnt += 1
                    que.append((ny, nx))
                    visited[ny][nx] = True
    return score * cnt


# 초기에 한거
def calc_score(score, root):
    visited = defaultdict(int) # 선언되지 않은 key가 들어오면 그냥 0이다
    que = deque([root])
    cnt = 1
    visited[str(root[0]) + str(root[1])] = 1
    '''
    key [0, 1] -> str(0) + str(1) key='01'
    '''
    while que:
        y, x = que.popleft()
        for dy, dx in foward_pos.values():
            ny = y + dy
            nx = x + dx
            
            if N > ny >= 0 and M > nx >= 0 and visited[str(ny) + str(nx)] == 0:
                if board[ny][nx] == score:
                    cnt += 1
                    que.append((ny, nx))
                    visited[str(ny) + str(nx)] = 1
    
    return score * cnt
 