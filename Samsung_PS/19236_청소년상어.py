'''
> 물고기를 dict에 넣고, 삭제시 del

> 물고기 이동 함수
> ↑, ↖, ←, ↙, ↓, ↘, →, ↗
> 시계방향으로 list 만들고 하나씩 증가 시키면서 전방 탐색
> 이동 가능할 경우 서로 위치 바꾸기


> 상어 이동
 DFS로 구성
 1. 방향에 따라 접근 가능한 board위치 list로 추출
 2. list가 없을경우 return
 3. 있을경우 해당 물고기를 먹고 재귀 dfs, deepcopy로 진행
'''
from pprint import pprint
def print_board(arr):
    for row in arr:
        print(row)
    print()


from copy import deepcopy

board = []
fish_dic = {}

for i in range(4):
    arr = list(map(int, input().split()))
    row = []
    for j in range(0, 7, 2):
        row.append([arr[j], arr[j + 1] - 1])
        fish_dic[arr[j]] = (i, j//2, arr[j + 1] - 1)
    board.append(row)

direction_list = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


def fish_wave(tmp_fish_dic, tmp_board, sr, sc):
    
    for fish in range(1, 17):
        
        if fish not in tmp_fish_dic:
            continue
        
        r, c, d = tmp_fish_dic[fish]
        
        for i in range(8):
            
            nd = (d + i)%8
            dr, dc = direction_list[nd]
            nr, nc = r + dr, c + dc
            
            if 4 > nr >= 0 and 4 > nc >= 0 and (nr, nc) != (sr, sc):
                
                if tmp_board[nr][nc][0] > 0:
                    
                    another_fish = tmp_board[nr][nc][0]
                    _, _, ad = tmp_fish_dic[another_fish]
                
                    tmp_board[nr][nc], tmp_board[r][c] = tmp_board[r][c], tmp_board[nr][nc]
                    tmp_board[nr][nc][1] = nd
                    
                    tmp_fish_dic[fish] = (nr, nc, nd)
                    tmp_fish_dic[another_fish] = (r, c, ad)
                    break
                
                elif tmp_board[nr][nc][0] == 0:
                    tmp_board[nr][nc], tmp_board[r][c] = tmp_board[r][c], tmp_board[nr][nc]
                    tmp_board[nr][nc][1] = nd
                    tmp_fish_dic[fish] = (nr, nc, nd)
                    break
                    
            
    return tmp_board, tmp_fish_dic
        
        
def shark_wave(d_fish_dic, d_board, root, total_score):
    
    global answer
    sr, sc = root
    
    rm_fish = d_board[sr][sc][0]
    sd = d_board[sr][sc][1]
    
    total_score += rm_fish
    del d_fish_dic[rm_fish]
    dr, dc = direction_list[sd]
    
    d_board[sr][sc] = [0, 0]
    fish_pos = []
    
    n_board, n_fish_dic = fish_wave(deepcopy(d_fish_dic), deepcopy(d_board), sr, sc)
    sr += dr
    sc += dc
    
    while 4 > sr >= 0 and 4 > sc >= 0:
        
        if n_board[sr][sc][0] > 0:
            fish_pos.append([sr, sc])
        sr += dr
        sc += dc
    
    if not fish_pos:
        answer = max(answer, total_score)
        return

    for nr, nc in fish_pos:
        shark_wave(deepcopy(n_fish_dic), deepcopy(n_board), (nr, nc), total_score)
                
    return

answer = score = 0

shark_wave(deepcopy(fish_dic), deepcopy(board), (0, 0), score)
print(answer)