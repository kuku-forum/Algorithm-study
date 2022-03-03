'''
 
 
물고기 방향: 8가지(왼쪽부터 8가지)
상어 방향: 4가지(상좌하우)

전처리로 -1
1. 물고기 이동(상어, 냄새, 밖 제외) -> 반시계 45도 -> 정지
2. 상어 무조건 3칸이동(물고기 제일 많은 곳, 사전순)
사전 -> 1234 중복순열
3. 물고기 냄새(2턴) 삭제
4. 처음 물고기 복제
'''
from re import L

from copy import deepcopy

def print_board(arr):
    for row in arr:
        print(row)
    print()
    
def permu_with_repet():
    arr = []
    
    for i in range(4):
        for j in range(4):
            for k in range(4):
                arr.append([i, j, k])                
    return arr

shark_dic = permu_with_repet()
fish_dir = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
shark_dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

scent = [[0 for _ in range(4)] for _ in range(4)]
def scent_down():
    for r in range(4):
        for c in range(4):
            if scent[r][c] > 0:
                scent[r][c] -= 1

'''
←, ↖, ↑, ↗, →, ↘, ↓, ↙
0,  1, 2, 3, 4,  5,  6, 7
'''

def fish_move(board, cur_pos):
    n_board = [[[] for _ in range(4)] for _ in range(4)]
    
    for r in range(4):
        for c in range(4):
            if board[r][c]:
                tmp = []
                
                while board[r][c]:
                    d_fish = board[r][c].pop()
                    for cc in range(8):
                        nd_fish = (d_fish - cc)%8
                        dr, dc = fish_dir[nd_fish]
                        nr = r + dr
                        nc = c + dc
                        
                        if 4 > nr >= 0 and 4 > nc >= 0 and scent[nr][nc] == 0 and (nr, nc) != cur_pos:
                            # print(d_fish, nd_fish)
                            n_board[nr][nc].append(nd_fish)
                            break
                    else:
                        # print('no')
                        tmp.append(d_fish)
                
                n_board[r][c].extend(tmp)
    return n_board

                
def shark_move(board, cur_pos):
    scent_down()
    
    tmp = []
    for i, move_case in enumerate(shark_dic):
        r, c = cur_pos
        cnt = 0
        visited = []
        for step in move_case:
            dr, dc = shark_dir[step]
            r += dr
            c += dc
            # if 4 > r >= 0 and 4 > c >= 0 and (r, c) not in visited:
            #     visited.append((r, c))
            #     if (r, c) != cur_pos:
            #         cnt += len(board[r][c])
                    
            if 4 > r >= 0 and 4 > c >= 0:
                if (r, c) not in visited:
                    visited.append((r, c))
                    cnt += len(board[r][c])
            else:
                break
        else:
            tmp.append((cnt, i, r, c))
            
    tmp.sort(key=lambda x: (-x[0], x[1]))
    _, fin_i, fin_r, fin_c = tmp[0]
    r, c = cur_pos
    
    for step in shark_dic[fin_i]:
        dr, dc = shark_dir[step]
        r += dr
        c += dc
        if board[r][c]:
            board[r][c] = []
            scent[r][c] = 2
        
    cur_pos = (fin_r, fin_c)
    return board, cur_pos


M, S = map(int, input().split())
board = [[[] for _ in range(4)] for _ in range(4)]

for _ in range(M):
    i, j, d = map(int, input().split())
    board[i-1][j-1].append(d-1)

si, sj = map(int, input().split())
shark_pos = (si-1, sj-1)

for _ in range(S):
    # print('1. init_board')
    # print_board(board)
    copy_fish = deepcopy(board)

    board = fish_move(board, shark_pos)
    # print('2. fish_move')
    # print_board(board)

    board, cur_pos = shark_move(board, shark_pos)
    # print('3. shark_move', shark_pos, cur_pos)
    # print_board(board)
    
    # print('scent_board')
    # print_board(scent)

    for r in range(4):
        for c in range(4):
            board[r][c].extend(copy_fish[r][c])
    
    # print('4. fish_copy')
    # print_board(board)
    
    shark_pos = cur_pos
    # print('shark_pos', shark_pos)
    # print()
    # print()
    
# print_board(board)
answer = 0

for i in range(4):
    for j in range(4):
        answer += len(board[i][j])
print(answer)


