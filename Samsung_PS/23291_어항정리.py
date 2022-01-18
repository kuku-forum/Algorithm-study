from collections import defaultdict, deque
from copy import deepcopy

N, K = map(int, input().split())



def fish_input(board):
    fish_pos = defaultdict(list)
    min_val = 0xffff
    
    for i in range(N):
        for j in range(N):
            if board[i][j] != bin_sign:
                fish_pos[board[i][j]].append([i, j])
                if min_val >= board[i][j]:
                    min_val = board[i][j]
                    
    for rm_i, rm_j in fish_pos[min_val]:
        board[rm_i][rm_j] += 1
    
def organize_fir(board):
    board[-1][0], board[-2][1] = bin_sign, board[-1][0]
    
def organize_sec(board_copy):
    global board
    
    tmp_arr = deque([])
    stack_chk = []
    
    for j in range(N):
        if board_copy[-2][j] != bin_sign:
            stack_chk.append(j)
    
    for stack_j in stack_chk:
        tmp_row = []
        for i in range(N-1, -1 ,-1):
            if board_copy[i][stack_j] == bin_sign:
                break
            tmp_row.append(board_copy[i][stack_j])
            board_copy[i][stack_j] = bin_sign
        tmp_arr.appendleft(tmp_row)
    stack_len = len(tmp_arr[0])
    bottom_len = -1
    
    for j in range(N):
        if board_copy[-1][j] != bin_sign:
            bottom_len = N - j
            break
    
    if stack_len > bottom_len:
        return 'stop'
    
    for ti, i in enumerate(range(N-2, N-2-len(tmp_arr), -1)):
        for tj, j in enumerate(range(N-bottom_len, N-bottom_len+stack_len)):
            board_copy[i][j] = tmp_arr[ti][tj]
    
    board = deepcopy(board_copy)
    return 'go'
    
def fish_dist(board):
    direc_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    rm_dic = defaultdict(set)
    
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == bin_sign:
                continue
            
            for dy, dx in direc_list:
                ny, nx = y + dy, x + dx
                if len(board) > ny >= 0 and len(board[0]) > nx >= 0 and board[ny][nx] != bin_sign:
                    d = abs(board[ny][nx] - board[y][x]) // 5
                    if d > 0:
                        if board[ny][nx] > board[y][x]:
                            rm_dic[(ny, nx)].add((y, x, d))
                        else:
                            rm_dic[(y, x)].add((ny, nx, d))
                            
    for sy, sx in rm_dic.keys():
        for ey, ex, d in rm_dic[(sy, sx)]:
            board[sy][sx] -= d
            board[ey][ex] += d
                

def re_span(board):
    tmp_row = deque([[]])
    
    for x in range(len(board[0])):
        if board[-1][x] != bin_sign:
            for y in range(len(board)-1, -1, -1):
                if board[y][x] == bin_sign:
                    break
                tmp_row[0].append(board[y][x])
                board[y][x] = bin_sign
    return tmp_row


def half_stack(board):
    
    for row in board:
        tmp_row = []
        for _ in range(N//2):
            tmp_row.append(row.pop())
    
    board[0] = deque(board[0][::-1])
    tmp_row = deque(tmp_row[::-1])
    board.append(tmp_row)
    tmp_board = deque([])
    
    for i, row in enumerate(reversed(board)):
        tmp_row = deque([])
        for _ in range(N//4):
            tmp_row.appendleft(row.popleft())
        tmp_board.append((tmp_row))
    
    for row in board:
        tmp_board.append((row))
    
    return tmp_board

    
bin_sign = 'x'
answer = 1

# 패딩해서 큰 네모에 물고기 집어넣기
board = [[bin_sign for _ in range(N)] for _ in range(N)]
board[-1] = list(map(int, input().split()))

while True:
    
    # 작은 수의 어항 물고기 더해주기
    fish_input(board)
    
    # 한칸만 쌓기
    organize_fir(board)
    
    # 반복해서 쌓기
    while True:
        stop_sign = organize_sec(deepcopy(board))
        if stop_sign == 'stop':
            break
    
    # 물고기 분배하기
    fish_dist(board) 
    
    # 어항 쭉 펼치기  
    board = re_span(board)
    
    # 어항 절반씩 쌓기
    board = half_stack(board)
    
    # 물고기 분배하기
    fish_dist(board)
    
    # 여항 쭉 펼치기
    last_board = re_span(board)

    if K >= max(last_board[0]) - min(last_board[0]):
        break
    
    # 리셋을 위해 다시 패딩해주기
    board = [[bin_sign for _ in range(N)] for _ in range(N)]
    board[-1] = list(last_board[0])
    answer += 1
    
print(answer)




'''
정리 과정
1. 가장 적은 어항 물고기 투입(중복)
2. 가장 왼쪽, 그 오른쪽 위에 쌓기

3. 2개 이상 어항 모두 분해 후 rot90 위에 쌓기(반복)

4. 인접한 물고기 수 조절(차이를 5로 나누고 0 초과면 많은 곳에서 d마리를 적은 곳으로 이동)
5. 일렬로 펼치기, 가장 왼쪽 아래 부터 위로 하나씩 추출


6. 왼쪽 절반 rot180 오른쪽 절반 위에 쌓기(두번반복)

7. 일렬로 펼치기, 가장 왼쪽 아래 부터 위로 하나씩 추출
8. 가장 많은 어항과 적은 어항의 차이가 K이하가 되게 설정
'''

'''
구현 과정
1. 
'''